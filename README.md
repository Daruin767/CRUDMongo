📚 Sistema de Gestión de Biblioteca con Flask y MySQL 🚀

Este proyecto implementa una base de datos relacional en MySQL para gestionar los datos clave de una biblioteca: libros, usuarios y préstamos. A continuación, se detalla su estructura y funcionamiento.

📖 Diseño de la Base de Datos

Se crearon tres tablas principales en la base de datos biblioteca:

productos: Almacena información de los libros (nombre, precio, cantidad disponible).

usuarios: Registra datos de los miembros (nombre, email, teléfono).

prestamos: Relaciona libros con usuarios mediante claves foráneas (user_id, product_id) y registra fechas de préstamo y devolución.

🗂️ Archivos Principales

1. app.py

🔧 Controla todas las funciones de la biblioteca.

📌 Gestiona:

📖 Libros: agregar, editar, eliminar.

👥 Usuarios: registrar, modificar, borrar.

🔄 Préstamos: gestionar y cancelar.

🔗 Conecta la interfaz con la base de datos MySQL.

2. database.py (Conexión a MySQL)

🌐 Configura el acceso a MySQL.

🔑 Define los datos de conexión: servidor local, usuario root, base de datos biblioteca.

⚠️ Maneja errores en caso de fallos de conexión.

3. 📌 Modelos (Clases)

product.py: Define la estructura de los libros (nombre, autor, ejemplares).

usuario.py: Describe los usuarios (nombre, email, teléfono).

loan.py: Registra los préstamos (usuario, libro, fechas).

🔄 Funcionamiento del Sistema

1️⃣ El usuario interactúa con la interfaz web.
2️⃣ app.py recibe las solicitudes del usuario.
3️⃣ La información es procesada y enviada a MySQL mediante database.py.
4️⃣ Los modelos organizan los datos.
5️⃣ Los resultados se reflejan en tiempo real en la interfaz web.

📊 Datos de Ejemplo (JSON)

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

