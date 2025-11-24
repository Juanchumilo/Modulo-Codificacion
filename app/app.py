from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
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
        cursor.execute("INSERT INTO usuarios(nombre, correo) VALUES (%s, %s)", (nombre, correo))
        conn.commit()
        conn.close()
        return redirect('/listar')

    return render_template('crear.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']

        cursor.execute("UPDATE usuarios SET nombre=%s, correo=%s WHERE id=%s",(nombre, correo, id))
        conn.commit()
        conn.close()
        return redirect('/listar')

    cursor.execute("SELECT * FROM usuarios WHERE id=%s", (id,))
    usuario = cursor.fetchone()
    conn.close()

    return render_template('editar.html', usuario=usuario)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    return redirect('/listar')

#Error 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__=='__main__':
    app.run(debug=True)