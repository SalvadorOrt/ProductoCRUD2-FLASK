from flask import Flask,request,render_template
from models.Producto import Producto
import pyodbc as sql
cadena_conexion = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I5UU64Q\SQLEXPRESS;DATABASE=prueba_flask;UID=usuario;PWD=12345'
app = Flask(__name__)
def ListaCategorias():
    conexion = sql.connect(cadena_conexion)
    cursor = conexion.cursor()
    query = '''
            SELECT categoria_id,nombre
             FROM Categorias
            '''
    lista = cursor.execute(query).fetchall()
    return lista
@app.route('/',methods = ['GET','POST'])
def root():
    if request.method == 'GET':
        conexion = sql.connect(cadena_conexion)
        cursor = conexion.cursor()
        producto = Producto()
        lista = cursor.execute(producto.listarProducto()).fetchall()
        print(lista)
        return render_template('index.html',lista = lista)
@app.route('/edit/<int:id>',methods = ['GET','POST'])
def edit(id):
    if request.method == 'POST':
        nombreREC = request.form["nombre_valor"]
        precioREC = request.form["precio_valor"]
        categoriaREC = request.form["categoria_valor"]
    elif request.method == 'GET':

        conexion = sql.connect(cadena_conexion)
        cursor = conexion.cursor()
        producto = Producto()
        lista = ListaCategorias()
        listado = cursor.execute(*producto.listarProductoID(id)).fetchall()
        nombre = listado[0][1]
        precio = listado[0][2]
        categoria = listado[0][3]
        print(nombre,precio)
        return render_template('edit.html',item = id,nombre = nombre,precio = precio,lista = lista,categoria = categoria)
        

if __name__ == '__main__':
    app.run(debug=True)





