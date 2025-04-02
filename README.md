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


4.	📌 Modelos (Clases)

   
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

