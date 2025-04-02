# 📚 Sistema de Gestión de Biblioteca con Flask y MySQL 🚀


Este proyecto implementa una base de datos relacional en MySQL para gestionar los datos clave de una biblioteca: libros, usuarios y préstamos. A continuación, se detalla su estructura y funcionamiento.

## Como se crea una rama

Crear una rama 

![image](https://github.com/user-attachments/assets/600c5ff9-59e6-45d1-9f7c-7a696de8d53c)

 
Usa este comando para hacer ambas acciones a la vez (crear y cambiar):
![image](https://github.com/user-attachments/assets/98108c51-6aae-46fd-a5ec-839d441fdcd0)

 
Salida esperada:

![image](https://github.com/user-attachments/assets/e2e4da2c-423d-4afd-a6c0-955954b29c2a)

 

Verifica que estás en la rama correcta
 
![image](https://github.com/user-attachments/assets/a321ecca-5155-46fa-b012-c0f7517502f6)

Trabajar en la rama y subir cambios
![image](https://github.com/user-attachments/assets/551b76bd-022e-4c3e-aa3f-3ab95b110713)



## Requisitos de Instalación:

Python 3.6+

Lenguaje base del sistema

Paquetes PIP

![Imagen1](https://github.com/user-attachments/assets/15b100f1-4f95-43bb-9af5-b36d97c257b5)




## 📖 Diseño de la Base de Datos

Se crearon tres tablas principales en la base de datos biblioteca:

productos: Almacena información de los libros (nombre, precio, cantidad disponible).

usuarios: Registra datos de los miembros (nombre, email, teléfono).

prestamos: Relaciona libros con usuarios mediante claves foráneas (user_id, product_id) y registra fechas de préstamo y devolución.


## estructura del proyecto 

![image](https://github.com/user-attachments/assets/b4eb310f-10f0-444f-a4ae-7cff6aeb7620)


## 🗂️ Archivos Principales

### 1. app.py

🔧 Controla todas las funciones de la biblioteca.

📌 Gestiona:

📖 Libros: agregar, editar, eliminar.

👥 Usuarios: registrar, modificar, borrar.

🔄 Préstamos: gestionar y cancelar.

🔗 Conecta la interfaz con la base de datos MySQL.

### 2. database.py (Conexión a MySQL)

Configura el acceso a MySQL.

Define los datos de conexión: servidor local, usuario root, base de datos biblioteca.

Maneja errores en caso de fallos de conexión.



🌐 Configura el acceso a MySQL.

🔑 Define los datos de conexión: servidor local, usuario root, base de datos biblioteca.

⚠️ Maneja errores en caso de fallos de conexión.

### 3. 📌 Modelos (Clases)

product.py: Define la estructura de los libros (nombre, autor, ejemplares).

usuario.py: Describe los usuarios (nombre, email, teléfono).

loan.py: Registra los préstamos (usuario, libro, fechas).

## 🔄 Funcionamiento del Sistema

1️⃣ El usuario interactúa con la interfaz web.
2️⃣ app.py recibe las solicitudes del usuario.
3️⃣ La información es procesada y enviada a MySQL mediante database.py.
4️⃣ Los modelos organizan los datos.
5️⃣ Los resultados se reflejan en tiempo real en la interfaz web.

## 📊 Datos de Ejemplo (JSON)

📌 Representación estructurada de los datos:

📚 Libros: Incluyen título, autor y disponibilidad.

👥 Usuarios: Contienen información personal y préstamos.

🔄 Préstamos: Registran fechas y estado.

🚀 Tecnologías Utilizadas

🔹 Flask: Framework para el desarrollo web.

🔹 MySQL: Para almacenamiento de datos.

🔹 Python: Lenguaje de programación principal.

🔹 HTML/CSS: Para la interfaz web.

📌 ¡Este sistema es una solución robusta, moderna y eficiente para la gestión de bibliotecas! 🎯📚✨

