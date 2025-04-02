# 📚 Sistema de Gestión de Biblioteca con Flask y MongoDB 🚀
## 🌟 Descripción del Proyecto

Este sistema ofrece una solución integral para la administración de bibliotecas, permitiendo un control eficiente de libros, usuarios y préstamos. Gracias a una interfaz web desarrollada con Flask y el almacenamiento en MongoDB, la gestión se vuelve rápida, organizada y accesible desde cualquier dispositivo.
________________________________________

## Tecnologías instaladas requeridas

### Para que este sistema funcione, se necesitan las siguientes instalaciones:

Python (como lenguaje base)

Flask (framework web): pip install flask

PyMongo (conector a MongoDB): pip install pymongo

MongoDB (base de datos): Instalado localmente en el puerto 27017

## Diagrama de casos de uso

![image](https://github.com/user-attachments/assets/1831fad5-7a99-421a-ba77-6cab656e3ece)



## 🔹 Componentes Principales

## 📂 Modelos de Datos

### 1.	📖 Product (Producto): Representa los libros disponibles en la biblioteca, incluyendo:
   
o	📌 Nombre del libro
o	✍️ Autor
o	📚 Ejemplares disponibles

### 2.	👤 User (Usuario): Gestiona la información de los miembros de la biblioteca:
   
o	🏷️ Nombre del usuario
o	✉️ Correo electrónico
o	📞 Número de teléfono

### 3.	🔄 Loan (Préstamo): Controla los préstamos realizados, almacenando:
   
o	👤 Usuario asociado
o	📖 Producto prestado
o	📅 Fecha del préstamo
________________________________________
## ⚡ Funcionalidades Implementadas

### 📚 Para Productos (Libros)

✅ Creación: Añadir nuevos libros al catálogo. 
✅ Edición: Modificar detalles de libros existentes. 
✅ Eliminación: Retirar libros del sistema. 
✅ Listado: Visualizar todos los libros disponibles.

### 👥 Para Usuarios

✅ Registro: Agregar nuevos miembros a la biblioteca.
✅ Actualización: Editar la información de los usuarios. 
✅ Borrado: Eliminar usuarios. 
✅ Consulta: Ver la lista completa de usuarios registrados.

### 🔄 Para Préstamos

✅ Creación: Registrar nuevos préstamos. 
✅ Modificación: Actualizar fechas de préstamos. 
✅ Cancelación: Eliminar registros de préstamos.
✅ Visualización: Consultar préstamos activos.
________________________________________

## 🗄️ Base de Datos
•	💾 MongoDB como sistema de almacenamiento principal.
•	📂 Tres colecciones principales:
1.	📚 productos: Almacena la información de los libros.
2.	👥 usuarios: Guarda los datos de los miembros.
3.	🔄 prestamos: Registra los préstamos realizados.
## 🔗 Conexión a MongoDB
•	🔍 Configuración centralizada en database.py.
•	🌐 URI de conexión: mongodb://localhost:27017/.
•	⚠️ Manejo de errores para garantizar la estabilidad de la conexión.
•	🔌 Uso de PyMongo, el driver oficial para interactuar con MongoDB.
________________________________________
## 🔄 Flujo de la Aplicación
1️⃣ El usuario accede a la interfaz principal (index.html).
2️⃣ Navega entre las diferentes secciones (productos, usuarios, préstamos). 
3️⃣ Realiza operaciones a través de formularios web.
4️⃣ Flask procesa las solicitudes y actualiza MongoDB.
5️⃣ Los cambios se reflejan inmediatamente en la interfaz.
________________________________________
## 📁 Estructura de Archivos
### 1.	app.py
o	🚀 Archivo principal de la aplicación Flask.
o	📌 Contiene todas las rutas y controladores.
o	🔄 Gestiona las operaciones CRUD.
o	🔗 Coordina la interacción con la base de datos.
### 2.	product.py
o	📖 Modelo que representa los productos/libros.
o	✍️ Define la estructura de datos: nombre, autor y ejemplares.
o	🔄 Convierte objetos a formato compatible con MongoDB.
### 3.	usuario.py
o	👥 Modelo para gestionar los usuarios.
o	🏷️ Contiene campos: nombre, email y teléfono.
o	🗄️ Formato optimizado para almacenamiento en la base de datos.
### 4.	loan.py
o	🔄 Modelo para manejar los préstamos.
o	🔗 Relaciona usuarios con productos.
o	📅 Registra fechas de préstamo y asegura la persistencia en MongoDB.
### 5.	database.py
o	🔌 Configuración de conexión con MongoDB.
o	🌐 Define los parámetros de conexión.
o	⚠️ Maneja la creación del cliente y la conexión a la base de datos.
________________________________________
