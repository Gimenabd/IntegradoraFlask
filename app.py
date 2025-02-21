from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
import binascii

# Crear la aplicación Flask
app = Flask(__name__)

# Clave secreta para usar en sesiones
app.secret_key = binascii.hexlify(os.urandom(24)).decode()  # Generar una clave secreta segura

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Dirección del servidor MySQL
app.config['MYSQL_USER'] = 'root'  # Cambia esto por tu usuario de MySQL
app.config['MYSQL_PASSWORD'] = 'root'  # Cambia esto por tu contraseña de MySQL
app.config['MYSQL_DB'] = 'libreria'  # Nombre de la base de datos

mysql = MySQL(app)


# Ruta principal
@app.route('/')
def index():
    return redirect(url_for('login'))


# Ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        email = request.form['email']
        password = request.form['password']
        
        # Conectar a la base de datos
        conn = mysql.connect
        cursor = conn.cursor()

        # Verificar si el email existe en la base de datos
        cursor.execute("SELECT Id_usuarios, Contrasenia, Tipo_de_Usuario FROM Usuarios WHERE Email = %s", (email,))
        user = cursor.fetchone()

        if user:
            user_id, stored_password, user_type = user
            # Comprobar si la contraseña proporcionada es correcta (sin seguridad)
            if password == stored_password:
                # Si la contraseña es correcta, almacenamos el ID de usuario en la sesión
                session['usuario'] = user_id
                session['tipo_usuario'] = user_type

                if user_type == 'Administrador':
                    return redirect(url_for('admin_dashboard'))
                elif user_type == 'Cliente':
                    return redirect(url_for('client_dashboard'))
                else:
                    flash('Tipo de usuario desconocido', 'danger')
            else:
                flash('Contraseña incorrecta', 'danger')
        else:
            flash('Email no registrado', 'danger')

    return render_template('login.html')


# Ruta para el panel de administración
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'usuario' not in session or session.get('tipo_usuario') != 'Administrador':
        return redirect(url_for('login'))
    return "Bienvenido al panel de administración."

# Ruta para registrar un nuevo libro (solo para Administradores)
@app.route('/register_book', methods=['GET', 'POST'])
def register_book():
    # Verificar que el usuario esté logueado y sea administrador
    if 'usuario' not in session or session.get('tipo_usuario') != 'Administrador':
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        estado = request.form['estado']  # Debe ser 'Disponible' o 'Vendido'
        existencia = request.form['existencia']
        costo = request.form['costo']
        editorial = request.form['editorial']
        autor = request.form['autor']

        # Conectar a la base de datos y ejecutar la consulta
        conn = mysql.connect
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Libros (Nombre, Estado, Existencia, Costo, Editorial, Autor)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre, estado, existencia, costo, editorial, autor))
        conn.commit()

        flash('Libro registrado correctamente', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('register_book.html')


# Ruta para el panel de cliente
@app.route('/client_dashboard')
def client_dashboard():
    if 'usuario' not in session or session.get('tipo_usuario') != 'Cliente':
        return redirect(url_for('login'))
    return "Bienvenido al panel de cliente."


# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('tipo_usuario', None)
    return redirect(url_for('login'))


# Ruta para registrar un nuevo usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre_completo = request.form['nombre_completo']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        tipo_usuario = request.form['tipo_usuario']  # 'Cliente' o 'Administrador'

        # Conectar a la base de datos
        conn = mysql.connect
        cursor = conn.cursor()

        # Insertar el nuevo usuario en la base de datos
        cursor.execute("INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia) VALUES (%s, %s, %s, %s, %s)", 
                       (tipo_usuario, nombre_completo, email, telefono, password))
        conn.commit()

        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
