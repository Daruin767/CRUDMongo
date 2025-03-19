from flask import Flask, render_template, request, jsonify, redirect, url_for
import database as dbase  
from usuario import User  # Asegúrate de que 'usuario.py' contenga la clase 'User'
from loan import Loan  # Asegúrate de que 'loan.py' contenga la clase 'Loan'
from product import Product  # Asegúrate de que 'product.py' contenga la clase 'Product'

db = dbase.dbConnection()

app = Flask(__name__)

# Ruta principal para mostrar productos, usuarios y préstamos
@app.route('/')
def home():
    products = db['products']
    users = db['users']
    loans = db['loans']
    
    productsReceived = products.find()
    usersReceived = users.find()
    loansReceived = loans.find()
    
    return render_template('index.html', products=productsReceived, users=usersReceived, loans=loansReceived)

# Método POST para agregar un producto
@app.route('/products', methods=['POST'])
def addProduct():
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        product = Product(name, price, quantity)
        products.insert_one(product.toDBCollection())  # Asegúrate de que 'toDBCollection' esté definido en 'Product'
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home', message="Error: Todos los campos son requeridos"))

# Método POST para agregar un usuario
@app.route('/users', methods=['POST'])
def addUser():
    users = db['users']
    user_name = request.form['user_name']
    user_email = request.form['user_email']
    user_phone = request.form['user_phone']

    if user_name and user_email and user_phone:
        user = User(user_name, user_email, user_phone)
        users.insert_one(user.toDBCollection())  # Asegúrate de que 'toDBCollection' esté definido en 'User'
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home', message="Error: Todos los campos son requeridos"))

# Método POST para registrar un préstamo
@app.route('/loans', methods=['POST'])
def addLoan():
    loans = db['loans']
    user_name = request.form['user_name']
    book_name = request.form['book_name']
    loan_date = request.form['loan_date']
    return_date = request.form['return_date']

    if user_name and book_name and loan_date and return_date:
        loan = Loan(user_name, book_name, loan_date, return_date)
        loans.insert_one(loan.toDBCollection())  # Asegúrate de que 'toDBCollection' esté definido en 'Loan'
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home', message="Error: Todos los campos son requeridos"))

# Método DELETE para eliminar un producto
@app.route('/delete/<string:product_name>')
def delete(product_name):
    products = db['products']
    products.delete_one({'name' : product_name})
    return redirect(url_for('home'))

# Método PUT para editar un producto
@app.route('/edit/<string:product_name>', methods=['POST'])
def edit(product_name):
    products = db['products']
    name = request.form['name']
    price = request.form['price']
    quantity = request.form['quantity']

    if name and price and quantity:
        products.update_one({'name' : product_name}, {'$set' : {'name' : name, 'price' : price, 'quantity' : quantity}})
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home', message="Error: Todos los campos son requeridos"))

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=4000)
