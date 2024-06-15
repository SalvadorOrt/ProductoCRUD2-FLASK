class Producto():
    def __init__(self,nombre = None,precio = None,categoria = None):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def insertarProducto(self):
        query = '''
                insert into Productos(nombre,precio,categoria_id) values(?,?,?)
                '''
        datos = (self.nombre,self.precio,self.categoria)
        return(query,datos)
    def listarProducto(self):
        query = '''
                select Productos.producto_id,Productos.nombre,Productos.precio,Categorias.nombre
                from Productos
                inner join Categorias
                on Productos.categoria_id  = Categorias.categoria_id
                '''
        return query
    def listarProductoID(self,id):
        query = '''
                select Productos.producto_id,Productos.nombre,Productos.precio,Categorias.nombre
                from Productos
                inner join Categorias
                on Productos.categoria_id  = Categorias.categoria_id 
                where  Productos.producto_id = ?
                '''
        datos  = (id,)
        return (query,datos)
    def actualizarProducto(self,nombre,precio,categoria,id):
        query = '''
                  update Productos set nombre = ?, precio = ?, categoria_id = ? where producto_id = ?
                '''
        datos  = (nombre,precio,categoria,id)
        return (query,datos)