class Producto():
    def __init__(self) -> None:
        pass
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
        return (query,id)