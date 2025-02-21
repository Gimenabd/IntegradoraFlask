from flask import Flask, session, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import os
import binascii
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de la clave secreta
app.secret_key = os.getenv("SECRET_KEY", binascii.hexlify(os.urandom(24)).decode())

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Libreria'

mysql = MySQL(app)
bcrypt = Bcrypt(app)

# Ruta principal redirige a login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Ruta para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

<<<<<<< HEAD
        # Verificar si el email existe en la base de datos
        cursor.execute("SELECT Id_usuarios, Contrasenia, Tipo_de_Usuario FROM Usuarios WHERE Email = %s", (email,))
=======
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Contrasenia, Tipo_de_Usuario FROM Usuarios WHERE Email = %s", (email,))
>>>>>>> 995d84e1dbb5bfabcef1a63f9e172a2e3c818b1d
        user = cursor.fetchone()

        if user:
            user_id, stored_password, user_type = user
            # Comparar contraseña usando bcrypt
            if bcrypt.check_password_hash(stored_password, password):
                session['usuario'] = user_id
                session['tipo_usuario'] = user_type

                if user_type == 'Administrador':
                    return redirect(url_for('admin_dashboard'))
                elif user_type == 'Cliente':
                    return redirect(url_for('client_dashboard'))
            else:
                flash('Contraseña incorrecta', 'danger')
        else:
            flash('Email no registrado', 'danger')

    return render_template('login.html')

# Ruta para panel de administración
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'usuario' not in session or session.get('tipo_usuario') != 'Administrador':
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

<<<<<<< HEAD
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
=======
# Ruta para panel de cliente
>>>>>>> 995d84e1dbb5bfabcef1a63f9e172a2e3c818b1d
@app.route('/client_dashboard')
def client_dashboard():
    if 'usuario' not in session or session.get('tipo_usuario') != 'Cliente':
        return redirect(url_for('login'))
    return render_template('client_dashboard.html')

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
        nombre_completo = request.form['nombre_completo']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        tipo_usuario = request.form['tipo_usuario']

        # Encriptar la contraseña con bcrypt
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuarios (Tipo_de_Usuario, Nombre_completo, Email, Telefono, Contrasenia) VALUES (%s, %s, %s, %s, %s)", 
            (tipo_usuario, nombre_completo, email, telefono, hashed_password)
        )
        conn.commit()

        flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
