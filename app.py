from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['biblioteca']

@app.route('/')
def home():
    products = db['productos'].find()
    users = db['usuarios'].find()
    loans = db['prestamos'].find()
    return render_template('index.html', products=products, users=users, loans=loans)

# Agregar Producto
@app.route('/productos', methods=['POST'])
def addProduct():
    name = request.form['name']
    price = request.form['price']
    cuantity = request.form['cuantity']

    if name and price and cuantity:
        db['productos'].insert_one({
            'name': name,
            'price': price,
            'cuantity': cuantity
        })
    return redirect(url_for('home'))

# Editar Producto
@app.route('/edit-product/<product_id>', methods=['GET', 'POST'])
def editProduct(product_id):
    if request.method == 'POST':
        updated_name = request.form['name']
        updated_price = request.form['price']
        updated_cuantity = request.form['cuantity']

        db['productos'].update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {'name': updated_name, 'price': updated_price, 'cuantity': updated_cuantity}}
        )
        return redirect(url_for('home'))
    
    product = db['productos'].find_one({'_id': ObjectId(product_id)})
    return render_template('edit_product.html', product=product)

# Eliminar Producto
@app.route('/delete-product/<product_id>', methods=['GET'])
def deleteProduct(product_id):
    db['productos'].delete_one({'_id': ObjectId(product_id)})
    return redirect(url_for('home'))

# Agregar Usuario
@app.route('/usuarios', methods=['POST'])
def addUser():
    name = request.form['user-name']
    email = request.form['user-email']
    phone = request.form['user-phone']

    if name and email and phone:
        db['usuarios'].insert_one({
            'name': name,
            'email': email,
            'phone': phone
        })
    return redirect(url_for('home'))

# Editar Usuario
@app.route('/edit-user/<user_id>', methods=['GET', 'POST'])
def editUser(user_id):
    if request.method == 'POST':
        updated_name = request.form['user-name']
        updated_email = request.form['user-email']
        updated_phone = request.form['user-phone']

        db['usuarios'].update_one(
            {'_id': ObjectId(user_id)},
            {'$set': {'name': updated_name, 'email': updated_email, 'phone': updated_phone}}
        )
        return redirect(url_for('home'))

    user = db['usuarios'].find_one({'_id': ObjectId(user_id)})
    return render_template('edit_user.html', user=user)

# Eliminar Usuario
@app.route('/delete-user/<user_id>', methods=['GET'])
def deleteUser(user_id):
    db['usuarios'].delete_one({'_id': ObjectId(user_id)})
    return redirect(url_for('home'))

# Agregar Préstamo
@app.route('/prestamo', methods=['POST'])
def addLoan():
    user_name = request.form['user-name']
    book_name = request.form['book-name']
    loan_date = request.form['loan-date']
    return_date = request.form['return-date']

    if user_name and book_name and loan_date and return_date:
        db['prestamos'].insert_one({
            'user_name': user_name,
            'book_name': book_name,
            'loan_date': loan_date,
            'return_date': return_date
        })
    return redirect(url_for('home'))

# Eliminar Préstamo
@app.route('/delete-loan/<loan_id>', methods=['GET'])
def deleteLoan(loan_id):
    db['prestamos'].delete_one({'_id': ObjectId(loan_id)})
    return redirect(url_for('home'))

# Editar Préstamo
@app.route('/edit-loan/<loan_id>', methods=['GET', 'POST'])
def editLoan(loan_id):
    if request.method == 'POST':
        updated_loan_date = request.form['loan-date']
        updated_return_date = request.form['return-date']

        db['prestamos'].update_one(
            {'_id': ObjectId(loan_id)},
            {'$set': {'loan_date': updated_loan_date, 'return_date': updated_return_date}}
        )
        return redirect(url_for('home'))

    loan = db['prestamos'].find_one({'_id': ObjectId(loan_id)})
    return render_template('edit_loan.html', loan=loan)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
