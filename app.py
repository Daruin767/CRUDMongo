from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection
from book import Book
from user import User
from loan import Loan

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flask'

def execute_query(query, params=None, fetch=False, fetch_one=False):
    conn = get_db_connection()
    if not conn:
        flash('Error de conexión con la base de datos', 'danger')
        return None
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        
        if fetch:
            result = cursor.fetchall()
        elif fetch_one:
            result = cursor.fetchone()
        else:
            conn.commit()
            result = True
        
        return result
    except Exception as e:
        conn.rollback()
        flash(f'Error en la base de datos: {str(e)}', 'danger')
        return None
    finally:
        if 'cursor' in locals(): cursor.close()
        if conn: conn.close()

@app.route('/')
def home():
    libros = execute_query("SELECT * FROM libros", fetch=True) or []
    usuarios = execute_query("SELECT * FROM usuarios", fetch=True) or []
    prestamos = execute_query("""
        SELECT p.*, u.user_name, l.title 
        FROM prestamos p
        JOIN usuarios u ON p.user_id = u.id
        JOIN libros l ON p.book_id = l.id
        ORDER BY p.loan_date DESC LIMIT 5
    """, fetch=True) or []
    
    return render_template('index.html', 
                        products=libros,  # Cambiado para coincidir con el template
                        usuarios=usuarios,
                        prestamos=prestamos)

# Libros
@app.route('/productos', methods=['GET', 'POST'])
def listar_libros():
    if request.method == 'POST':
        try:
            if execute_query(
                "INSERT INTO libros (title, author, available_copies, total_copies) VALUES (%s, %s, %s, %s)",
                (request.form['name'], request.form['price'], request.form['cuantity'], request.form['cuantity'])
            ):
                flash('Libro agregado correctamente', 'success')
        except Exception as e:
            flash(f'Error al agregar libro: {str(e)}', 'danger')
        return redirect(url_for('listar_libros'))
    
    libros = execute_query("SELECT id as _id, title as name, author as price, available_copies as cuantity FROM libros ORDER BY title", fetch=True) or []
    return render_template('index.html', products=libros)

@app.route('/delete-product/<int:id>')
def eliminar_libro(id):
    if execute_query("DELETE FROM libros WHERE id = %s", (id,)):
        flash('Libro eliminado correctamente', 'success')
    else:
        flash('Error al eliminar libro', 'danger')
    return redirect(url_for('listar_libros'))

# Usuarios
@app.route('/usuarios', methods=['GET', 'POST'])
def view_users():
    if request.method == 'POST':
        try:
            if execute_query(
                "INSERT INTO usuarios (user_name, user_email, user_phone) VALUES (%s, %s, %s)",
                (request.form['user-name'], request.form['user-email'], request.form['user-phone'])
            ):
                flash('Usuario agregado correctamente', 'success')
        except Exception as e:
            flash(f'Error al agregar usuario: {str(e)}', 'danger')
        return redirect(url_for('view_users'))
    
    usuarios = execute_query("SELECT id as _id, user_name as name, user_email as email, user_phone as phone FROM usuarios ORDER BY user_name", fetch=True) or []
    return render_template('usuario.html', users=usuarios)

@app.route('/delete-user/<int:id>')
def eliminar_usuario(id):
    if execute_query("DELETE FROM usuarios WHERE id = %s", (id,)):
        flash('Usuario eliminado correctamente', 'success')
    else:
        flash('Error al eliminar usuario', 'danger')
    return redirect(url_for('view_users'))

# Préstamos
@app.route('/prestamo', methods=['GET', 'POST'])
def view_loans():
    if request.method == 'POST':
        try:
            # Obtener IDs de usuario y libro basados en nombres
            usuario = execute_query(
                "SELECT id FROM usuarios WHERE user_name = %s", 
                (request.form['user-name'],), 
                fetch_one=True
            )
            libro = execute_query(
                "SELECT id FROM libros WHERE title = %s AND available_copies > 0", 
                (request.form['book-name'],), 
                fetch_one=True
            )
            
            if not usuario or not libro:
                flash('Usuario o libro no encontrado/disponible', 'warning')
                return redirect(url_for('view_loans'))
            
            if execute_query(
                "INSERT INTO prestamos (user_id, book_id, loan_date, return_date) VALUES (%s, %s, %s, %s)",
                (usuario['id'], libro['id'], request.form['loan-date'], request.form['return-date'])
            ):
                execute_query(
                    "UPDATE libros SET available_copies = available_copies - 1 WHERE id = %s",
                    (libro['id'],)
                )
                flash('Préstamo registrado correctamente', 'success')
        except Exception as e:
            flash(f'Error al registrar préstamo: {str(e)}', 'danger')
        return redirect(url_for('view_loans'))
    
    prestamos = execute_query("""
        SELECT p.id as _id, u.user_name as user_name, l.title as book_name, 
               p.loan_date as loan_date, p.return_date as return_date
        FROM prestamos p
        JOIN usuarios u ON p.user_id = u.id
        JOIN libros l ON p.book_id = l.id
        ORDER BY p.loan_date DESC
    """, fetch=True) or []
    
    return render_template('prestamo.html', loans=prestamos)

@app.route('/delete-loan/<int:id>')
def eliminar_prestamo(id):
    prestamo = execute_query("SELECT book_id FROM prestamos WHERE id = %s", (id,), fetch_one=True)
    if prestamo:
        execute_query("UPDATE libros SET available_copies = available_copies + 1 WHERE id = %s", (prestamo['book_id'],))
        if execute_query("DELETE FROM prestamos WHERE id = %s", (id,)):
            flash('Préstamo eliminado correctamente', 'success')
        else:
            flash('Error al eliminar préstamo', 'danger')
    else:
        flash('Préstamo no encontrado', 'danger')
    return redirect(url_for('view_loans'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)