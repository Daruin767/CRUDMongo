📚 Sistema de Gestión de Biblioteca con Flask y MongoDB 🚀
🌟 Descripción del Proyecto
Este sistema ofrece una solución integral para la administración de bibliotecas, permitiendo un control eficiente de libros, usuarios y préstamos. Gracias a una interfaz web desarrollada con Flask y el almacenamiento en MongoDB, la gestión se vuelve rápida, organizada y accesible desde cualquier dispositivo.
________________________________________
🔹 Componentes Principales
📂 Modelos de Datos
1.	📖 Product (Producto): Representa los libros disponibles en la biblioteca, incluyendo:
o	📌 Nombre del libro
o	✍️ Autor
o	📚 Ejemplares disponibles
2.	👤 User (Usuario): Gestiona la información de los miembros de la biblioteca:
o	🏷️ Nombre del usuario
o	✉️ Correo electrónico
o	📞 Número de teléfono
3.	🔄 Loan (Préstamo): Controla los préstamos realizados, almacenando:
o	👤 Usuario asociado
o	📖 Producto prestado
o	📅 Fecha del préstamo
________________________________________
⚡ Funcionalidades Implementadas
📚 Para Productos (Libros)
✅ Creación: Añadir nuevos libros al catálogo. ✅ Edición: Modificar detalles de libros existentes. ✅ Eliminación: Retirar libros del sistema. ✅ Listado: Visualizar todos los libros disponibles.
👥 Para Usuarios
✅ Registro: Agregar nuevos miembros a la biblioteca. ✅ Actualización: Editar la información de los usuarios. ✅ Borrado: Eliminar usuarios. ✅ Consulta: Ver la lista completa de usuarios registrados.
🔄 Para Préstamos
✅ Creación: Registrar nuevos préstamos. ✅ Modificación: Actualizar fechas de préstamos. ✅ Cancelación: Eliminar registros de préstamos. ✅ Visualización: Consultar préstamos activos.
________________________________________
🏗️ Arquitectura Técnica
🔧 Backend
•	💻 Desarrollado en Python con el framework Flask.
•	🔀 Sistema de rutas para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).
•	📌 Implementación del patrón MVC (Modelo-Vista-Controlador) para mantener una arquitectura bien organizada.
🗄️ Base de Datos
•	💾 MongoDB como sistema de almacenamiento principal.
•	📂 Tres colecciones principales:
1.	📚 productos: Almacena la información de los libros.
2.	👥 usuarios: Guarda los datos de los miembros.
3.	🔄 prestamos: Registra los préstamos realizados.
🔗 Conexión a MongoDB
•	🔍 Configuración centralizada en database.py.
•	🌐 URI de conexión: mongodb://localhost:27017/.
•	⚠️ Manejo de errores para garantizar la estabilidad de la conexión.
•	🔌 Uso de PyMongo, el driver oficial para interactuar con MongoDB.
________________________________________
🔄 Flujo de la Aplicación
1️⃣ El usuario accede a la interfaz principal (index.html). 2️⃣ Navega entre las diferentes secciones (productos, usuarios, préstamos). 3️⃣ Realiza operaciones a través de formularios web. 4️⃣ Flask procesa las solicitudes y actualiza MongoDB. 5️⃣ Los cambios se reflejan inmediatamente en la interfaz.
________________________________________
📁 Estructura de Archivos
1.	app.py
o	🚀 Archivo principal de la aplicación Flask.
o	📌 Contiene todas las rutas y controladores.
o	🔄 Gestiona las operaciones CRUD.
o	🔗 Coordina la interacción con la base de datos.
2.	product.py
o	📖 Modelo que representa los productos/libros.
o	✍️ Define la estructura de datos: nombre, autor y ejemplares.
o	🔄 Convierte objetos a formato compatible con MongoDB.
3.	usuario.py
o	👥 Modelo para gestionar los usuarios.
o	🏷️ Contiene campos: nombre, email y teléfono.
o	🗄️ Formato optimizado para almacenamiento en la base de datos.
4.	loan.py
o	🔄 Modelo para manejar los préstamos.
o	🔗 Relaciona usuarios con productos.
o	📅 Registra fechas de préstamo y asegura la persistencia en MongoDB.
5.	database.py
o	🔌 Configuración de conexión con MongoDB.
o	🌐 Define los parámetros de conexión.
o	⚠️ Maneja la creación del cliente y la conexión a la base de datos.
________________________________________
📚 Sistema de Gestión de Biblioteca con Flask y MySQL 🚀
🗂️ Archivos Principales
1.	app.py
o	🔧 Controla todas las funciones de la biblioteca.
o	📌 Gestiona:
	📖 Libros: agregar, editar, eliminar.
	👥 Usuarios: registrar, modificar, borrar.
	🔄 Préstamos: gestionar y cancelar.
o	🔗 Conecta la interfaz con la base de datos MySQL.
2.	database.py (Conexión a MySQL)
o	🌐 Configura el acceso a MySQL.
o	🔑 Datos de conexión: servidor local, usuario root, base biblioteca.
o	⚠️ Maneja errores en caso de fallos de conexión.
3.	📌 Modelos (Clases)
o	product.py: Define la estructura de los libros (nombre, autor, ejemplares).
o	usuario.py: Describe los usuarios (nombre, email, teléfono).
o	loan.py: Registra los préstamos (quién, qué libro, fechas).
________________________________________
🔄 Cómo Funciona el Sistema
1️⃣ El usuario interactúa con la interfaz web. 2️⃣ app.py recibe las solicitudes del usuario. 3️⃣ La información es procesada y enviada a MySQL mediante database.py. 4️⃣ Los modelos organizan los datos. 5️⃣ Los resultados se reflejan en tiempo real en la interfaz web.
________________________________________
📊 Datos de Ejemplo (JSON)
📌 Representación estructurada de los datos:
•	📚 Libros: Incluyen título, autor y disponibilidad.
•	👥 Usuarios: Contienen información personal y préstamos.
•	🔄 Préstamos: Registran fechas y estado.
________________________________________
🚀 Tecnologías Utilizadas
🔹 Flask: Framework para el desarrollo web. 🔹 MongoDB / MySQL: Para almacenamiento de datos. 🔹 Python: Lenguaje de programación principal. 🔹 HTML/CSS: Para la interfaz web.
📌 ¡Este sistema es una solución robusta, moderna y eficiente para la gestión de bibliotecas! 🎯📚✨

