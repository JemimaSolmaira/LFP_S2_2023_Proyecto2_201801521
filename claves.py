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
        self.lexemas = ["registros", "=", "[", "grupo", "]"]
        self.patron = ["tk_registros", "tk_igual", "tk_corchete_in", "tk_grupo_registros", "tk_corchete_fin", "fin"]
        self.datos = [None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]
        self.informacion = [None, None, None, None, None]
        self.errores = []
        
    def inicio_registro(self, token, dato, inf):
        if token in self.patron:
            self.llenar_datos(token, dato, inf)
        else:
            palabra = dato.lower()
            if palabra in self.palabras_reservados and self.contador > 2:   
                #if palabra in ["registros", "registro", "="] and self.contador > 2:
                self.contador = 5                       
            else:
                error = [palabra, "error lexico: token desconocido", inf.linea, inf.col]
                self.errores.append(error)
        
        return self.patron[self.contador]
    
    def llenar_datos(self, token, dato, inf):
        token_esperado = self.patron[self.contador]
        
        if token == token_esperado:
        
            if token == "tk_registros":
                self.agregar_dato(dato, inf)   
            elif token == "tk_igual":
                self.agregar_dato(dato, inf)
            elif token == "tk_corchete_in":
                self.agregar_dato(dato, inf)
            elif token == "tk_grupo_registros":
                self.agregar_dato(dato, inf)
            elif token == "tk_corchete_fin":
                self.agregar_dato(dato, inf)
                self.contador = 4
            
            self.contador += 1    
        
        else:
            self.agregar_sin_orden(token, dato, inf)
            

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
        
    def agregar_dato(self, dato, inf):
        lista = self.datos[self.contador]
        if lista == None:
            self.datos[self.contador] = dato
            self.informacion[self.contador] = inf
            #self.contador += 1
        else:
            error = [dato, "error sintactico: dato no esperado", inf.linea, inf.col]
            self.errores.append(error)
            
    
    def agregar_sin_orden(self, token, dato, inf):
        i =  self.buscar_token(token)
        #existencia = self.datos[i]
        
        if i != None:
            if i > self.contador: 
                if dato in self.datos:
                    error = [dato, "error lexico: token desconocido", inf.linea, inf.col]
                    self.errores.append(error)
                elif token == "tk_grupo_registros":
                    self.datos[i] = dato
                    self.contador = i +1   
                else:
                    self.datos[i] = dato
                    self.contador = i + 1
            else:
                if dato in self.datos:
                    error = [dato, "error lexico: token desconocido", inf.linea, inf.col]
                    self.errores.append(error)
                elif token == "tk_grupo_registros":
                    self.datos[i] = dato 
                    self.contador = i + 1
                else:
                    self.datos[i] = dato
                    #self.contador = 1 
                    error = [dato, "error lexico: token desconocido", inf.linea, inf.col]
                    self.errores.append(error)

        else:
            print("error sintactico, token no esperado")
            
    def encontrar_error(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                token = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                error = [token, "error lexico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)  
        
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == 4:
                return self.informacion[3]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
            
    
        
        
        
class grupo_registro:
    def __init__(self):
        self.lexemas = ["{", "grupo", "}"]
        self.patron = ["tk_llave_in", "tk_grupo_palabras", "tk_llave_fin", "fin"]
        self.datos = [None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None]
        self.errores = []
    
    def inicio_grupo_registro(self, token, dato, inf):
        fin = False
        if token in self.patron:
            fin = self.llenar_datos(token, dato, inf)
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
    
    def llenar_datos(self, token, dato, inf):
        token_esperado = self.patron[self.contador]

        fin = False

        if token == "tk_llave_in":
            if self.datos[0] == None:
                self.datos[0] = dato
                self.informacion[0] = inf
            else:
                fin = True 
            if token == token_esperado:
                self.contador += 1 
                
        elif token == "tk_grupo_palabras":
            self.datos[1] = dato
            self.informacion[1] = inf
            if token == token_esperado:
                self.contador += 1 
                
        elif token == "tk_llave_fin":
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
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

        
        if self.vacio() == False:
            if self.datos[1]== None:
                if self.datos[0] != None and self.datos[2]!= None:
                    error = ["Registros", "error sintactico: Registro vacio", self.informacion[0].linea, self.informacion[0].col]
                    self.errores.append(error)
                else:
                    token = self.lexemas[self.caracter()]
                    inf = self.encontrar_indice(self.caracter())
                    error = [token, "error sintactico: palabra o letra no esperada", inf.linea, inf.col]
                    self.errores.append(error)
            else:
                for i in self.datos:
                    indice = self.datos.index(i)
                    if i == None:
                        token = self.lexemas[indice]
                        inf = self.encontrar_indice(indice)
                        print(inf)
                        error = [token, "error lexico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                        self.errores.append(error)
                        print("error sintactico" + "se esperaba: " + token)
            
    def caracter(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i != None:
                return indice
        return indice
    
    def vacio(self):
        vacio = True
        for i in self.datos:
            if i != None:
                vacio = False
        return vacio
    
    def obtener_registro(self):
        return self.datos
  
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == 2:
                return self.informacion[1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]

    
    
        
class grupo_palabras:
    def __init__(self):    
        self.lexemas = ['"', "String", '"', "," ]
        self.lexema_numero = ["numero", ","]
        self.patron_coma = ["tk_comillas", "tk_string", "tk_comillas", "tk_coma", "fin"]
        self.patron_numero = ["tk_numero","tk_coma" ,"fin"]
        self.datos_coma = [None, None, None, None]
        self.datos_numero = [None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "Registros", "Registro", "=","[" , "]" ,"imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte"]
        self.indicadores = ["{", "}", "\n"]
        self.indicadores_string = ["'", '"', "tk_string"]
        self.inf_str = [None, None, None, None]
        self.inf_num = [None, None]
        self.errores = []
        

    def inicio(self, token, palabra, es_numero, inf):
        if es_numero == True:
            valores = self.evaluar_numero(token, palabra, inf)   
        else:
            valores = self.evaluar(token, palabra, inf)
            
        return valores
            
    
    def evaluar_numero(self, token, palabra, inf):
        token_esperado = self.patron_numero[self.contador]
        fin = False
        grupo_completo = False
        
        if token == "tk_numero":
            if self.datos_numero[0] == None:
                self.datos_numero[0] = palabra
                self.inf_num[0] = inf
            else:
                fin = True

            if token == token_esperado:
                self.contador += 1

        
        if token == "tk_coma":
            self.datos_numero[1] = palabra
            self.inf_num[1] = inf
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

 
        
        return fin, grupo_completo   
    
     
    def evaluar(self, token, palabra, inf):
        token_esperado = self.patron_coma[self.contador]
        fin = False
        grupo_finalizado = False

        
        if token == "tk_comillas":
  
            if self.datos_coma[0] == None:
                self.datos_coma[0] = palabra
                self.inf_str[0] = inf
            else:
                if self.datos_coma[2] == None:
                    self.datos_coma[2] = palabra
                    self.inf_str[2] = inf

                else:
                    print("error sintactico, comillas extras")
                    error = [palabra, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, comillas no esperadas")
                error = [palabra, "error sintactico: comillas no esperadas", inf.linea, inf.col]
                self.errores.append(error)
    
        elif token == "tk_string":
            
            if self.datos_coma[1]== None:
                self.datos_coma[1] = palabra
                self.inf_str[1] = inf
            else:
                fin = True
                
            if token == token_esperado:
                self.contador += 1
            else:
                print("error sintactico, string no esperado")
                
        elif token == "tk_coma":
            if self.datos_coma[3] == None:
                self.datos_coma[3] = palabra
                self.inf_str[3] = inf
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
    

    def agregar_sin_orden(self, token, dato, inf):
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
                    error = [dato, "error sintactico: dato repetido", inf.linea, inf.col]
                    self.errores.append(error)
                else:
                    self.datos_coma[i] = dato
                    #self.contador = 1 
                    print("error sintactico, token no esperado")
                    error = [dato, "error sintactico: token no esperado", inf.linea, inf.col]
                    self.errores.append(error)  

        else:
            print("error sintactico, token no esperado")
            error = [dato, "error sintactico: token no esperado", inf.linea, inf.col]
            self.errores.append(error)
    

    def buscar_token(self,token):
        if token in self.patron_coma:
            indice = self.patron_coma.index(token)
            return indice
        
    def encontrar_error(self, es_numero, sig_token):
        if es_numero == True:
            self.encontrar_error_numero(sig_token)
        else:
            self.encontrar_error_string(sig_token)
        
    def encontrar_error_string(self, sig_token):
        if sig_token in ["tk_llave_in", "tk_llave_fin", "tk_salto_linea", "tk_corchete_fin", "tk_corchete_in"]:
            self.datos_coma.pop()
             
        for i in self.datos_coma:
            indice = self.datos_coma.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice_str(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
                
    def encontrar_error_numero(self, sig_token):
        if sig_token in ["tk_llave_in", "tk_llave_fin", "tk_salto_linea", "tk_corchete_fin", "tk_corchete_in"]:
            self.datos_numero.pop()
        
        for i in self.datos_numero:
            indice = self.datos_numero.index(i)
            if i == None:
                lexema = self.lexema_numero[indice]
                inf = self.encontrar_indice_num(indice)
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                print("error sintactico" + "se esperaba: " )
                
                
    def encontrar_indice_num(self, indice):
        inf = self.inf_num[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.inf_num) - 1:
                return self.inf_num[indice - 1]
            elif indice == 0:
                return self.inf_num[1]
            else:
                return self.inf_num[indice - 1]
            
    def encontrar_indice_str(self, indice):
        inf = self.inf_str[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.inf_str) - 1:
                return self.inf_str[indice - 1]
            elif indice == 0:
                return self.inf_str[1]
            else:
                return self.inf_str[indice - 1]
                
        
class imprimir:
    def __init__(self):
        self.lexemas = ["imprimir", "(", '"', "String", '"', ")", ";"]
        self.patron = ["tk_imprimir", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_imprimir":
            if self.datos[0] == None:
                self.datos[0] = dato
                self.informacion[0] = inf 
                self.orden.append(token) 
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: imprimir repetido", inf.linea, inf.col]
                self.errores.append(error)
                self.contador += 1
                
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)    
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                error = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                print("error sintactico, punto y coma repetido")
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
                
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()


class imprimirln:
    def __init__(self):
        self.lexemas = ["imprimirln", "(", '"', "String", '"', ")", ";"]
        self.patron = ["tk_imprimirln", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []


    def insertar_dato(self,token , dato, inf):
        fin = False
            
        if token == "tk_imprimirln":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: imprimirln repetido", inf.linea, inf.col]
                self.errores.append(error)
                print("error sintactico, imprimir repetido")
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                print("error sintactico, parentesis repetido")
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            

        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                error = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
                
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
                
    
class datos:
    def __init__(self):
        self.lexemas = ["datos", "(",  ")", ";"]
        self.patron = ["tk_datos", "tk_parentesis_in",  "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_datos":
            if self.datos[0] == None:
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: dato repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
                
        elif token == "tk_parentesis_fin":
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
                
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class conteo:
    def __init__(self):
        self.lexemas = ["conteo", "(",  ")", ";"]
        self.patron = ["tk_conteo", "tk_parentesis_in",  "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_conteo":
            if self.datos[0] == None:
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: dato repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
                
        elif token == "tk_parentesis_fin":
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
                  
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class promedio:
    def __init__(self):
        self.lexemas = ["promedio", "(", '"', "String", '"', ")", ";"]
        self.patron = ["tk_promedio", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_promedio":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: promedio repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            
            
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
                     
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class contarsi:
    def __init__(self):
        self.lexemas = ["contarsi", "(", '"', "String", '"', ",", '"', "Numero", '"', ")", ";"]
        self.patron = ["tk_contarsi", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas", "tk_coma", "tk_numero" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_contarsi":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: contarsi repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
                    
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
        elif token == "tk_coma":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, coma repetido")
                error = [dato, "error sintactico: coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_numero":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, numero repetido")
                error = [dato, "error sintactico: numero repetido", inf.linea, inf.col]
                self.errores.append(error)
        

        elif token == "tk_parentesis_fin":
            if self.datos[7] == None:
                self.datos[7] = dato
                self.informacion[7] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[8] == None:
                self.datos[8] = dato
                self.informacion[8] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
                       
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class sumar:
    def __init__(self):
        self.lexemas = ["sumar", "(", '"', "String", '"', ",", '"', "String", '"', ")", ";"]
        self.patron = ["tk_sumar", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_sumar":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: sumar repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)

                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class maximo:
    def __init__(self):
        self.lexemas = ["max", "(", '"', "String", '"', ")", ";"]
        self.patron = ["tk_max", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_max":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: max repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
                
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
    
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
class minimo:
    def __init__(self):
        self.lexemas = ["min", "(", '"', "String", '"', ")", ";"]
        self.patron = ["tk_min", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []


    def insertar_dato(self,token , dato, inf):
        fin = False
        
        if token == "tk_min":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: min repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    
    
class exportar_reporte:
    def __init__(self):
        self.lexemas = ["exportarreporte", "(", '"', "String", '"', ",", '"', "String", '"', ")", ";"]
        self.patron = ["tk_exportarreporte", "tk_parentesis_in", "tk_comillas" ,  "tk_string",  "tk_comillas" , "tk_parentesis_fin", "tk_punto_coma" , "fin"]
        self.datos = [None, None, None, None, None, None, None]
        self.contador = 0
        self.palabras_reservados = ["claves", "clave", "registros", "registro", "=","[" , "]" ,"imprimir", ",", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte", "{", "}", "\n"]
        self.informacion = [None, None, None, None, None, None, None]
        self.errores = []
        self.orden = []

    def insertar_dato(self,token , dato, inf):
        fin = False

        if token == "tk_exportarreporte":
            if self.datos[0] == None:
            
                self.datos[0] = dato
                self.informacion[0] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, imprimir repetido")
                error = [dato, "error sintactico: exportarreporte repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_parentesis_in":
            if self.datos[1] == None:
                self.datos[1] = dato
                self.informacion[1] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_comillas":
            
            if self.datos[2] == None:
                self.datos[2] = dato
                self.informacion[2] = inf
                self.orden.append(token)
            else:
                if self.datos[4] == None:
                    self.datos[4] = dato
                    self.informacion[4] = inf
                    self.orden.append(token)
                else:
                    print("error sintactico, comillas extras")
                    error = [dato, "error sintactico: comillas extras", inf.linea, inf.col]
                    self.errores.append(error)
            
                
        elif token == "tk_string" :
            if self.datos[3] == None:
                self.datos[3] = dato
                self.informacion[3] = inf
                self.orden.append(token)
            else:
                print("error sintactico, string repetido")
                errores = [dato, "error sintactico: string repetido", inf.linea, inf.col]
                self.errores.append(errores)
                
                
        elif token == "tk_parentesis_fin":
            if self.datos[5] == None:
                self.datos[5] = dato
                self.informacion[5] = inf
                self.orden.append(token)
            else:
                print("error sintactico, parentesis repetido")
                error = [dato, "error sintactico: parentesis repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_punto_coma":
            if self.datos[6] == None:
                self.datos[6] = dato
                self.informacion[6] = inf
                self.orden.append(token)
                
            else:
                print("error sintactico, punto y coma repetido")
                error = [dato, "error sintactico: punto y coma repetido", inf.linea, inf.col]
                self.errores.append(error)
                
        elif token == "tk_salto_linea":
            fin = True
            
        return fin
        
        
    def encontrar_errores(self):
        for i in self.datos:
            indice = self.datos.index(i)
            if i == None:
                lexema = self.lexemas[indice]
                inf = self.encontrar_indice(indice)
                print("error sintactico" + "se esperaba: " )
                error = [lexema, "error sintactico: se esperaba caracter o palabra reservada", inf.linea, inf.col]
                self.errores.append(error)
                
    def encontrar_indice(self, indice):
        inf = self.informacion[indice]
        if inf != None:
            return inf
        else:
            if indice == len(self.informacion) - 1:
                return self.informacion[indice - 1]
            elif indice == 0:
                return self.informacion[1]
            else:
                return self.informacion[indice - 1]
    
    def revisar_orden(self):
        i = 0
        j = 0
        while i <= len(self.datos) - 1:
            if self.datos[i] != None:
                if self.patron[i] != self.orden[j]:
                    print("error sintactico, orden incorrecto")
                    error = [self.datos[i], "error sintactico: orden incorrecto", self.informacion[i].linea, self.informacion[i].col]
                    self.errores.append(error)
                i += 1
                j += 1
            else:
                i += 1
       
    def ejecutar_errores(self):
        self.encontrar_errores()
        self.revisar_orden()
    