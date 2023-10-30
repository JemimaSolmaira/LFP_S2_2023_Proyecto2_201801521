from archivos_salida import salida
import copy

class informacion:
    def __init__(self, claves, registros):
        self.claves = []
        print("Claves ingresadas")
        print(claves)
        self.registros = []
        print("Registros ingresados")
        print(registros)
        self.claves = claves
        self.registros = registros
        
    def conteo(self):
        return len(self.registros)
    
    def promedio(self, parametro):
        
        suma = self.suma(parametro)
        if suma == "No se encontro el parametro":
            return suma

        conteo = self.conteo()
        promedio = suma/conteo
        
        return promedio
    
    def contar_si(self, parametro, condicion):
        i = self.buscar_clave(parametro)
        if i == None:
            return "No se encontro la clave"
        else:
            enviar = self.registros[condicion-1]
            enviar = enviar[i]
        
        print("el archivo enviado es" + str(enviar))       
        return enviar   
    
    def datos(self):

        encabezados = self.claves
        lista = self.registros  
        encabezados_formateados = [encabezado.ljust(15) for encabezado in encabezados]
        
        separador = '-' * (15 * 5)

        resultado = ' '.join(encabezados_formateados) + '\n' + separador + '\n'

        for fila in lista:
            fila_formateada = [str(dato).ljust(15) for dato in fila]
            resultado += ' '.join(fila_formateada) + '\n'
        
        return resultado
            
    
    def suma(self, parametro): 
        i = self.buscar_clave(parametro)

        suma = 0
        if i == None:
            return "No se encontro el parametro"
        else:
            for j in self.registros:
                suma += int(j[i])
            
        return suma    
        
    def maximo(self, parametro):
        i = self.buscar_clave(parametro)
        maximo = 0
        if i == None:
            return "No se encontro el parametro"
        else:
        
            for j in self.registros:
                if j[i] > maximo:
                    maximo = j[i]
                
        return maximo
    
    def minimo(self, parametro):
        i = self.buscar_clave(parametro)
        if i == None:
            return "No se encontro el parametro"
        else:
            minimo = self.maximo(parametro)
            for j in self.registros:
                if j[i] < minimo:
                    minimo = j[i]
                
        return minimo
    
    def exportar_reporte(self, nombre_archivo):
        s = salida(nombre_archivo)
        
        s.tabla_productos(nombre_archivo, self.registros, self.claves)
        

    def buscar_clave(self, clave):
        indice = None
        for i in self.claves:
            if i == clave:
                indice = self.claves.index(i)
                print( clave, indice)
                return indice
        return indice
    
    
    def analizar(self, instrucciones):
        resultados = []
        
        for i in instrucciones:
            accion = i.accion.lower()
            parametro = i.dato
            
            if accion == "imprimirln":
                imprimir = ">>> " + str(i.dato) 
                resultados.append(imprimir)
            elif accion == "imprimir":
                imprimir = ">>> " + str(i.dato) + "\n"
                resultados.append(imprimir)
            elif accion == "conteo":
                cont = ">>> " + str(self.conteo()) + "\n"
                resultados.append(cont)
            elif accion == "promedio":
                prom = ">>> " + str(self.promedio(parametro)) + "\n"
                resultados.append(prom)
            elif accion == "datos":
                dat = ">>> " + "\n" + str(self.datos()) + "\n"
                resultados.append(dat)
            elif accion == "contarsi":
                cont_si = ">>> " + str(self.contar_si(parametro[0], parametro[1]))+ "\n"
                resultados.append(cont_si)
            elif accion == "sumar":
                suma = ">>> " + str(self.suma(parametro)) + "\n"
                resultados.append(suma)
            elif accion == "max":
                maximo = ">>> " + str(self.maximo(parametro))+ "\n"
                resultados.append(maximo)
            elif accion == "min":
                minimo = ">>> " + str(self.minimo(parametro))+ "\n"
                resultados.append(minimo)
            elif accion == "exportarreporte":
                self.exportar_reporte(parametro)
                exportar = ">>> Se ha exportado el reporte." + "\n"
                resultados.append(exportar)
                
        return resultados
        
        
            

if __name__ == '__main__':
    
    
    prueba = informacion(["nombre", "edad", "peso"], [["Juan", 20, 70], ["Pedro", 30, 80], ["Maria", 40, 90]])

    
    contar_si = prueba.contar_si("edad", 2)
    print(contar_si)
    
    
   
    
    
    
    