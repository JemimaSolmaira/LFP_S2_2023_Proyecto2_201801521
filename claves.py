from datos import scanner

class claves:
    def __init__(self):
        
        self.patron = ["tk_claves", "tk_igual", "tk_corchete_in", "tk_grupo_claves", "tk_corchete_fin", "fin"]
        self.datos = [None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]
        
    def inicio_clave(self, token, dato):
        print (token, dato)
        if token in self.patron:
            self.llenar_datos(token, dato)
        else:
            palabra = dato.lower()
            if palabra in self.palabras_reservados and self.contador > 2:   
                #if palabra in ["registros", "registro", "="] and self.contador > 2:
                self.contador = 5                       
            else:
                print("error lexico: token desconocido")
        
        print(self.contador)
        return self.patron[self.contador]
    
    def llenar_datos(self, token, dato):
        token_esperado = self.patron[self.contador]
        print(token_esperado , token)
        
        if token == token_esperado:
        
            if token == "tk_claves":
                self.agregar_dato(dato)   
            elif token == "tk_igual":
                self.agregar_dato(dato)
            elif token == "tk_corchete_in":
                self.agregar_dato(dato)
            elif token == "tk_grupo_claves":
                self.agregar_dato(dato)
            elif token == "tk_corchete_fin":
                self.agregar_dato(dato)
                self.contador = 4
            
            self.contador += 1    
        
        else:
            self.agregar_sin_orden(token, dato)
            

    def completado(self):
        if self.contador == 5:
            return True
        return False
    
    def mostrar_datos(self):
        print(self.datos)

        
    def buscar_token(self,token):
        if token in self.patron:
            indice = self.patron.index(token)
            return indice 
        
    def agregar_dato(self, dato):
        lista = self.datos[self.contador]
        if lista == None:
            self.datos[self.contador] = dato
            #self.contador += 1
        else:
            print ("error sintactico, dato repetido")
    
    def agregar_sin_orden(self, token, dato):
        i =  self.buscar_token(token)
        #existencia = self.datos[i]
        
        if i != None:
            if i > self.contador: 
                if dato in self.datos:
                    print("error sintactico, dato repetido") 
                elif token == "tk_grupo_claves":
                    self.datos[i] = dato
                    self.contador = i +1   
                else:
                    self.datos[i] = dato
                    self.contador = i + 1
            else:
                if dato in self.datos:
                    print("error sintactico, dato repetido")
                elif token == "tk_grupo_claves":
                    self.datos[i] = dato 
                    self.contador = i + 1
                else:
                    self.datos[i] = dato
                    #self.contador = 1 
                    print("error sintactico, token no esperado")  

        else:
            print("error sintactico, token no esperado")
            
    def encontrar_error(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
            

class registros:
    def __init__(self):
        self.patron = ["tk_registros", "tk_igual", "tk_corchete_in", "tk_grupo_registros", "tk_corchete_fin", "fin"]
        self.datos = [None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]
        self.informacion = []
        
    def inicio_registro(self, token, dato):
        print (token, dato)
        if token in self.patron:
            self.llenar_datos(token, dato)
        else:
            palabra = dato.lower()
            if palabra in self.palabras_reservados and self.contador > 2:   
                #if palabra in ["registros", "registro", "="] and self.contador > 2:
                self.contador = 5                       
            else:
                print("error lexico: token desconocido")
        
        print(self.contador)
        return self.patron[self.contador]
    
    def llenar_datos(self, token, dato):
        token_esperado = self.patron[self.contador]
        print(token_esperado , token)
        
        if token == token_esperado:
        
            if token == "tk_registros":
                self.agregar_dato(dato)   
            elif token == "tk_igual":
                self.agregar_dato(dato)
            elif token == "tk_corchete_in":
                self.agregar_dato(dato)
            elif token == "tk_grupo_registros":
                self.agregar_dato(dato)
            elif token == "tk_corchete_fin":
                self.agregar_dato(dato)
                self.contador = 4
            
            self.contador += 1    
        
        else:
            self.agregar_sin_orden(token, dato)
            

    def completado(self):
        if self.contador == 5:
            return True
        return False
    
    def mostrar_datos(self):
        print(self.datos)

        
    def buscar_token(self,token):
        if token in self.patron:
            indice = self.patron.index(token)
            return indice 
        
    def agregar_dato(self, dato):
        lista = self.datos[self.contador]
        if lista == None:
            self.datos[self.contador] = dato
            #self.contador += 1
        else:
            print ("error sintactico, dato repetido")
    
    def agregar_sin_orden(self, token, dato):
        i =  self.buscar_token(token)
        #existencia = self.datos[i]
        
        if i != None:
            if i > self.contador: 
                if dato in self.datos:
                    print("error sintactico, dato repetido") 
                elif token == "tk_grupo_registros":
                    self.datos[i] = dato
                    self.contador = i +1   
                else:
                    self.datos[i] = dato
                    self.contador = i + 1
            else:
                if dato in self.datos:
                    print("error sintactico, dato repetido")
                elif token == "tk_grupo_registros":
                    self.datos[i] = dato 
                    self.contador = i + 1
                else:
                    self.datos[i] = dato
                    #self.contador = 1 
                    print("error sintactico, token no esperado")  

        else:
            print("error sintactico, token no esperado")
            
    def encontrar_error(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)    
        

        
        
class grupo_registro:
    def __init__(self):
        self.patron = ["tk_llave_in", "tk_grupo_palabras", "tk_llave_fin", "fin"]
        self.datos = [None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
    
    def inicio_grupo_registro(self, token, dato):
        print (token, dato)
        fin = False
        if token in self.patron:
            fin = self.llenar_datos(token, dato)
        elif token == "tk_salto_linea":
            fin = True
        else:
            palabra = dato.lower()
            if palabra in self.palabras_reservados and self.contador > 2:   
                #if palabra in ["registros", "registro", "="] and self.contador > 2:
                fin = True                       
            else:
                print("error lexico: token desconocido")
        
        print(self.contador)
        return fin
    
    def llenar_datos(self, token, dato):
        token_esperado = self.patron[self.contador]
        print(token_esperado , token)
        fin = False

        if token == "tk_llave_in":
            if self.datos[0] == None:
                self.datos[0] = dato
            else:
                fin = True 
            if token == token_esperado:
                self.contador += 1 
                
        elif token == "tk_grupo_palabras":
            self.datos[1] = dato
            if token == token_esperado:
                self.contador += 1 
                
        elif token == "tk_llave_fin":
            self.datos[2] = dato
            fin = True   
            if token == token_esperado:
                self.contador += 1 

        return fin   


        
    def buscar_token(self,token):
        if token in self.patron:
            indice = self.patron.index(token)
            return indice 
        
    def agregar_dato(self, dato):
        lista = self.datos[self.contador]
        if lista == None:
            self.datos[self.contador] = dato
            self.contador += 1
        else:
            print ("error sintactico, dato repetido")
    
            
    def encontrar_error(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
    def vacio(self):
        vacio = True
        for i in self.datos:
            if i != None:
                vacio = False
        return vacio
    
    def obtener_registro(self):
        return self.datos
    
    
        
class grupo_palabras:
    def __init__(self):    
        self.patron_coma = ["tk_comillas", "tk_string", "tk_comillas", "tk_coma", "fin"]
        self.patron_numero = ["tk_numero","tk_coma" ,"fin"]
        self.datos_coma = [None, None, None, None]
        self.datos_numero = [None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "Registros", "Registro", "=","[" , "]" ,"imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte"]
        self.indicadores = ["{", "}", "\n"]
        self.indicadores_string = ["'", '"', "tk_string"]

    
    
    def inicio(self, token, palabra, es_numero):
        if es_numero == True:
            valores = self.evaluar_numero(token, palabra)    
        else:
            valores = self.evaluar(token, palabra)
            
        return valores
            
    
    def evaluar_numero(self, token, palabra):
        token_esperado = self.patron_numero[self.contador]
        fin = False
        grupo_completo = False
        print(token, palabra)
        
        if token == "tk_numero":
            if self.datos_numero[0] == None:
                self.datos_numero[0] = palabra
            else:
                fin = True

            if token == token_esperado:
                self.contador += 1

        
        if token == "tk_coma":
            self.datos_numero[1] = palabra
            fin = True
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, coma no esperada")
        
        else:
            if palabra in self.indicadores:
                grupo_completo = True
                fin = True
            elif palabra in self.indicadores_string:
                fin = True
            elif palabra in self.palabras_reservados and self.contador > 2:
                grupo_completo = True
                fin = True 


         
        print (fin, grupo_completo)    
        
        return fin, grupo_completo   
    
     
    def evaluar(self, token, palabra):
        token_esperado = self.patron_coma[self.contador]
        fin = False
        grupo_finalizado = False
        print(token, palabra)
        
        if token == "tk_comillas":
  
            if self.datos_coma[0] == None:
                self.datos_coma[0] = palabra
            else:
                if self.datos_coma[2] == None:
                    self.datos_coma[2] = palabra

                else:
                    print("error sintactico, comillas extras")
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
    
        elif token == "tk_string":
            
            if self.datos_coma[1]== None:
                self.datos_coma[1] = palabra
            else:
                fin = True
                
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, string no esperado")
                
        elif token == "tk_coma":
            if self.datos_coma[3] == None:
                self.datos_coma[3] = palabra
                fin = True
 
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, coma no esperada")
            
        else:
            if palabra in self.indicadores:
                grupo_finalizado = True
                fin = True
            elif token == "tk_numero":
                fin = True
            elif palabra in self.palabras_reservados and self.contador > 2:
                grupo_finalizado = True
                fin = True 


        #self.encontrar_error(fin)
        
        return fin, grupo_finalizado
    
    def comillas(self, token, palabra):
        if self.datos_coma[0] != None: 
            self.datos_coma[0] = palabra
            print("error sintactico, orden incorrecto")
        elif self.datos_coma[2] == None: 
            self.datos_coma[2] = palabra  
            print("error sintactico, orden incorrecto")  
        else:
            print("error sintactico, comillas no esperadas")    
    
    
    
    def agregar_sin_orden(self, token, dato):
        i =  self.buscar_token(token)
        
        if i != None:
            if i > self.contador: 
                if dato in self.datos_coma:
                    print("error sintactico, dato repetido")  
                else:
                    self.datos_coma[i] = dato
                    self.contador = i + 1
            else:
                if dato in self.datos_coma:
                    print("error sintactico, dato repetido")
                else:
                    self.datos_coma[i] = dato
                    #self.contador = 1 
                    print("error sintactico, token no esperado")  

        else:
            print("error sintactico, token no esperado")
    

    def buscar_token(self,token):
        if token in self.patron_coma:
            indice = self.patron_coma.index(token)
            return indice
        
    def encontrar_error(self, es_numero, grupo_completo):
        if es_numero == True:
            self.encontrar_error_numero(grupo_completo)
        else:
            self.encontrar_error_string(grupo_completo)
        
    def encontrar_error_string(self, grupo_completo):
        if grupo_completo == True:
            self.datos_coma.pop()
        print(self.datos_coma)
        
        for i in self.datos_coma:
            indice = self.datos_coma.index(i)
            if i == None:
                token = self.patron_coma[indice]
                print("error sintactico" + "se esperaba: " + token)
                
    def encontrar_error_numero(self, grupo_completo):
        if grupo_completo == True:
            self.datos_coma.pop()
        print(self.datos_numero)
        
        for i in self.datos_numero:
            indice = self.datos_numero.index(i)
            if i == None:
                token = self.patron_numero[indice]
                print("error sintactico" + "se esperaba: " + token)
                
            


        
class imprimir:
    def __init__(self):
        self.patron = ["tk_imprimir", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_imprimir":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class imprimirln:
    def __init__(self):
        self.patron = ["tk_imprimirln", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
            
        if token == "tk_imprimirln":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class datos:
    def __init__(self):
        self.patron = ["tk_datos", "tk_parentesis_in",  "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_datos":
            if self.datos[0] == None:
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
                
        elif token == "tk_parentesis_fin":
            if self.datos[2] == None:
                self.datos[2] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class conteo:
    def __init__(self):
        self.patron = ["tk_conteo", "tk_parentesis_in",  "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_conteo":
            if self.datos[0] == None:
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
                
        elif token == "tk_parentesis_fin":
            if self.datos[2] == None:
                self.datos[2] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class promedio:
    def __init__(self):
        self.patron = ["tk_promedio", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_promedio":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class contarsi:
    def __init__(self):
        self.patron = ["tk_contarsi", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas", "tk_coma", "tk_numero" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_contarsi":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_coma":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, coma no esperado")
            else:
                print("error sintactico, coma repetido")
                
        elif token == "tk_numero":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, numero no esperado")
            else:
                print("error sintactico, numero repetido")
        

        elif token == "tk_parentesis_fin":
            if self.datos[7] == None:
                self.datos[7] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[8] == None:
                self.datos[8] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class sumar:
    def __init__(self):
        self.patron = ["tk_sumar", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_sumar":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class maximo:
    def __init__(self):
        self.patron = ["tk_max", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_max":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class minimo:
    def __init__(self):
        self.patron = ["tk_min", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_min":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)
    
class exportar_reporte:
    def __init__(self):
        self.patron = ["tk_exportarreporte", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]

    def insertar_dato(self,token , dato):
        fin = False
        token_esperado = self.patron[self.contador]
        
        if token == "tk_exportarreporte":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, imprimir no esperado")
            else:
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                else:
                    print("error sintactico, comillas extras")
            
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, string no esperado")
            else:
                print("error sintactico, string repetido")
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, parentesis no esperado")
            else:
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                if token == token_esperado:
                    self.contador += 1
                else:
                    print("error sintactico, punto y coma no esperado")
            else:
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.patron[indice]
                print("error sintactico" + "se esperaba: " + token)