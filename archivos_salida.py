class salida:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        
        
    def tabla_productos(self,nombre_archivo, datos):
        productos = []
        productos = datos
        contenido_tabla = ""
        
        if len(productos) != 0:
            for i in productos:
                
               contenido_tabla += self.contenido_producto(i[0], i[1], i[2], i[3], i[4])
        else:
            print("No hay productos")
            return    
            
        contenido_archivo = self.encabezado("Reporte de Productos", "Productos")
        contenido_archivo += self.inicio_tabla_producto() 
        contenido_archivo += contenido_tabla + self.cierre_tabla()
                
        
        nombre = nombre_archivo + ".html"
        
        archivo = open(nombre, 'w')
        archivo.write(contenido_archivo)
        archivo.close()
        

        
        
    def errores(self,nombre_archivo, datos):
        errores = []
        errores = datos
        contenido_tabla = ""
        
        if len(errores) != 0:
            for i in errores:
                contenido_tabla += self.contenido_errores(i[0], i[1], i[2], i[3])
        
        else:
            print("No hay errores")
            return
        
        contenido_archivo = self.encabezado("Reporte de Errores", "Errores")
        contenido_archivo += self.inicio_tabla_errores()
        contenido_archivo += contenido_tabla + self.cierre_tabla()
        
        nombre = nombre_archivo + ".html"
        archivo = open(nombre, 'w')
        archivo.write(contenido_archivo)
        archivo.close()
        

        
    def tokens(self, nombre_archivo, datos):
        tokens = []
        tokens = datos
        
        contenido_tabla = ""
        
        if len(tokens) != 0:
            for i in tokens:
                contenido_tabla += self.contenido_tokens(i.palabra, i.token, i.linea, i.col)
        else:
            print("No hay tokens")
            return
        
        contenido_archivo = self.encabezado("Reporte de Tokens", "Tokens")
        contenido_archivo += self.inicio_tabla_tokens()
        contenido_archivo += contenido_tabla + self.cierre_tabla()
        
        nombre = nombre_archivo + ".html"
        archivo = open(nombre, 'w')
        archivo.write(contenido_archivo)
        archivo.close()   
            
        
        
    def encabezado(self, titulo_pagina, titulo_tabla):
        titulo = "<!DOCTYPE html>\n"
        titulo += "<html>\n<head>\n"
        titulo += "<title>"+ str(titulo_pagina) + "</title>\n"
        titulo += "</head>\n<body>\n\n<h1>"+ str(titulo_tabla) + "</h1>\n"
        return  titulo

    def inicio_tabla_producto(self):
        cadena = "<table border=\"1\">\n"
        cadena += "<tr>\n"
        cadena += "<th>Codigo</th>\n"
        cadena += "<th>Producto</th>\n"
        cadena += "<th>Precio_compra</th>\n"
        cadena += "<th>Precio_venta</th>\n"
        cadena += "<th>Stock</th>\n"
        cadena += "</tr>\n"
        
        return cadena
        
        
    def inicio_tabla_errores(self):
        cadena = "<table border=\"1\">\n"
        cadena += "<tr>\n"
        cadena += "<th>Caracter</th>\n"
        cadena += "<th>Descripcion</th>\n"
        cadena += "<th>Fila</th>\n"
        cadena += "<th>Columna</th>\n"
        cadena += "</tr>\n"
        
        return cadena  
            
            
    def inicio_tabla_tokens(self):
        cadena = "<table border=\"1\">\n"
        cadena += "<tr>\n"
        cadena += "<th>Token</th>\n"
        cadena += "<th>Lexema</th>\n"
        cadena += "<th>Fila</th>\n"
        cadena += "<th>Columna</th>\n"
        cadena += "</tr>\n"
        
        return cadena
        
     
    def contenido_producto(self, codigo, producto, precio_compra, precio_venta, stock):
        cadena = "<tr>\n"
        cadena += "<td>"+ str(codigo) +"</td>\n"
        cadena += "<td>"+ str(producto) +"</td>\n"
        cadena += "<td>"+ str(precio_compra) +"</td>\n"
        cadena += "<td>"+ str(precio_venta) +"</td>\n"
        cadena += "<td>"+ str(stock) +"</td>\n"
        cadena += "</tr>\n"
        
        return cadena   
   
    def contenido_errores(self, caracter, descripcion, fila, columna):
        cadena = "<tr>\n"
        cadena += "<td>"+ str(caracter) +"</td>\n"
        cadena += "<td>"+ str(descripcion) +"</td>\n"
        cadena += "<td>"+ str(fila) +"</td>\n"
        cadena += "<td>"+ str(columna) +"</td>\n"
        cadena += "</tr>\n"
        
        return cadena
    
    def contenido_tokens(self, token, lexema, fila, columna):
        cadena = "<tr>\n"
        cadena += "<td>"+ str(token) +"</td>\n"
        cadena += "<td>"+ str(lexema) +"</td>\n"
        cadena += "<td>"+ str(fila) +"</td>\n"
        cadena += "<td>"+ str(columna) +"</td>\n"
        cadena += "</tr>\n"
        
        return cadena
    
    def cierre_tabla(self):
        cadena = "</table>\n"
        cadena
        return cadena
        
   
        
    def celdas_producto(self):
        pass
    
    
    
if __name__ == '__main__':
    ta = salida("salida.html")
    
    fila1 = [1, "producto1", 10, 15, 20]
    fila2 = [2, "producto2", 10, 15, 20]
    fila3 = [3, "producto3", 10, 15, 20]
    fila4 = [4, "producto4", 10, 15, 20]
    fila5 = [5, "producto5", 10, 15, 20]
    
    productos = []
    productos.append(fila1)
    productos.append(fila2)
    productos.append(fila3)
    productos.append(fila4)
    productos.append(fila5)
    
    
    ta.tabla_productos("salida", productos)
    
    
   