from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    conn.close()
    return render_template("listar.html", usuarios=datos)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios(nombre,correo) VALUES (%s,%s)", (nombre, correo))
        conn.commit()
        conn.close()

        return redirect('/')
    return render_template('crear.html')
