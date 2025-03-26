from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from database import dbConnection as get_db_connection
from product import Product
from usuario import User
from loan import Loan

app = Flask(__name__)

@app.route('/')
def home():
    conn = get_db_connection()
    if not conn:
        return "Error de conexión con la base de datos", 500
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute('SELECT * FROM productos')
    products = cursor.fetchall()
    
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    
    cursor.execute('''SELECT prestamos.id, usuarios.user_name, productos.name AS product_name, prestamos.loan_date, prestamos.return_date 
                      FROM prestamos 
                      JOIN usuarios ON prestamos.user_id = usuarios.id 
                      JOIN productos ON prestamos.product_id = productos.id''')
    loans = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', products=products, users=users, loans=loans)

# Agregar Producto
@app.route('/productos', methods=['POST'])
def add_product():
    name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    
    if not all([name, price, quantity]):
        return "Faltan datos en el formulario", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (name, price, quantity) VALUES (%s, %s, %s)', (name, price, quantity))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Editar Producto
@app.route('/edit-product/<int:product_id>', methods=['POST'])
def edit_product(product_id):
    name = request.form.get('name')
    price = request.form.get('price')
    quantity = request.form.get('quantity')
    
    if not all([name, price, quantity]):
        return "Faltan datos en el formulario", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE productos SET name=%s, price=%s, quantity=%s WHERE id=%s', (name, price, quantity, product_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Eliminar Producto
@app.route('/delete-product/<int:product_id>', methods=['GET'])
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id=%s', (product_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Agregar Usuario
@app.route('/usuarios', methods=['POST'])
def add_user():
    name = request.form.get('user-name')
    email = request.form.get('user-email')
    phone = request.form.get('user-phone')
    
    if not all([name, email, phone]):
        return "Faltan datos en el formulario", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (user_name, user_email, user_phone) VALUES (%s, %s, %s)', (name, email, phone))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Editar Usuario
@app.route('/edit-user/<int:user_id>', methods=['POST'])
def edit_user(user_id):
    name = request.form.get('user-name')
    email = request.form.get('user-email')
    phone = request.form.get('user-phone')
    
    if not all([name, email, phone]):
        return "Faltan datos en el formulario", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET user_name=%s, user_email=%s, user_phone=%s WHERE id=%s', (name, email, phone, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Eliminar Usuario
@app.route('/delete-user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=%s', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Agregar Préstamo
@app.route('/prestamo', methods=['POST'])
def add_loan():
    user_id = request.form.get('user-id')
    product_id = request.form.get('product-id')
    loan_date = request.form.get('loan-date')
    return_date = request.form.get('return-date')
    
    if not all([user_id, product_id, loan_date, return_date]):
        return "Faltan datos en el formulario", 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO prestamos (user_id, product_id, loan_date, return_date) VALUES (%s, %s, %s, %s)', (user_id, product_id, loan_date, return_date))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

# Eliminar Préstamo
@app.route('/delete-loan/<int:loan_id>', methods=['GET'])
def delete_loan(loan_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM prestamos WHERE id=%s', (loan_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)