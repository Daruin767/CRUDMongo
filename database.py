import mysql.connector
from mysql.connector import Error

def dbConnection():
    try:
        Connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='biblioteca'
        )
        return Connection
    except mysql.connector.Error as err:
        print(f'Error de conexión con la base de datos: {err}')
        return None
