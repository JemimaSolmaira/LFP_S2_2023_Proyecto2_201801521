from datos import scanner
from claves import claves
from claves import registros
from claves import grupo_registro, grupo_palabras, imprimir, imprimirln
from claves import datos, conteo, promedio, contarsi, sumar, maximo, minimo, exportar_reporte
from datos_consola import datos_consola

class parserL:
    def __init__(self, tokens, errores):
        self.tokens = []
        self.tokens = tokens
        self.palabras_clave = []
        self.palabras_registros = []
        self.datos_registros = []
        self.palabras_reservadas = ["claves", "clave", "registros", "registro", "imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]	
        self.tokens_reservados = ["tk_claves", "tk_registro", "tk_registros", "tk_imprimir", "tk_imprimirln", "tk_datos", "tk_conteo", "tk_promedio", "tk_contarsi", "tk_sumar" ,"tk_max", "tk_min", "tk_exportarreporte" ]
        self.errores = []
        self.errores = errores
        self.arbol_derivacion = []
        

    def inicio(self):
        self.poner_comentario()
        
       
    def poner_comentario(self):
        pass
    


    def comentario(self):
        token = self.tokens.pop(0)
        comillas = ""
        cant_comillas = 0
        texto_numeral = False
        texto_comillas = False
        texto = ""
        if token.token == "tk_salto_linea":
            token  = self.tokens.pop(0)
        
        if token.token == "tk_sim_numeral":
            texto_numeral = True
        
        elif token.token == "tk_comillas":
     
            comillas += token.palabra
            cant_comillas += 1
            while cant_comillas != 3:
                    
                token = self.tokens.pop(0)
                    
                if token.token == "tk_comillas":
                    comillas += token.palabra
                        
                    cant_comillas += 1
                        
                else:
                    error = ['"', "Error Sintactico: Se esperaba una comilla", token.linea, token.col]
                    self.errores.append(error)
                    print("Error: Se esperaba una comilla")
                    #error de  comilla, error sintactico
            print(cant_comillas)
            
    
            
            if cant_comillas == 3:
                texto_comillas = True
                        
            
        if texto_numeral:
            #token = self.tokens.pop()
            while token.token != "tk_salto_linea":
                texto += token.palabra
                token = self.tokens[0]
                if token.token != "tk_salto_linea":
                    self.tokens.pop(0)
                    

        
        if texto_comillas:
            token = self.tokens.pop()
            while token.token != "tk_comillas":
                texto += token.palabra
                token = self.tokens[0]
                if token.token != "tk_comillas":
                    self.tokens.pop(0)
            
        
        
        if cant_comillas == 3: 
            cant_comillas = 0 
            token = self.tokens.pop(0)  
            if token.token == "tk_comillas":
                comillas = token.palabra
                cant_comillas += 1
                while cant_comillas != 3:
                    token = self.tokens.pop(0)
                    if token.token == "tk_comillas":
                        comillas += token.palabra
                        cant_comillas += 1
                    else:
                        error = ['"', "Error Sintactico: Se esperaba una comilla", token.linea, token.col]
                        self.errores.append(error)
                        print("Error: Se esperaba una comilla")
                        #error de  comilla, error sintactico
                        
            
        return texto                 
        
                        

    
    def comentario2(self):

        token = self.tokens[0]
        frase = ""
       
                    
        if token.token == "tk_sim_numeral":
            while token.token != "tk_salto_linea":
                frase += token.palabra
                token = self.tokens.pop(0)
            
            return frase
        

        comillas = []
        
        i=0
        while token.token != "tk_salto_linea":
            token = self.tokens[i]
            comillas.append(token.palabra)
            i+=1

        print(comillas)
        
        contiene = self.contiene_tres_comillas_consecutivas(comillas)
        print(contiene)
        token = self.tokens[0]
        if contiene == False:
            contiene = self.contiene_dos_comillas_consecutivas(comillas)
            
        print(contiene)
        

        if contiene:
            token = self.tokens.pop(0)
            while token.token == "tk_comillas":
                token = self.tokens.pop(0)
                
            
            while token.token != "tk_comillas":
                print(token.token)
                token = self.tokens[0]
                if token.token == "tk_espacio" or token.token == "tk_salto_linea" or token.token == "tk_string":
                    frase += token.palabra
                    self.tokens.pop(0)
                    token = self.tokens[0]
            
            while token.token == "tk_comillas":
                token = self.tokens.pop(0)        
                
        return frase                
     

    def eliminar_elementos_hasta_salto_de_linea(self, lista):
        while lista and lista[0] != "tk_salto_linea":
            lista.pop(0)  # Elimina el primer elemento de la lista

        if lista and lista[0] == "tk_salto_linea":
            lista.pop(0)  # Elimina la última instancia de "tk_salto_linea" si existe

            
        
        
    def contiene_tres_comillas_consecutivas(self, lista):
        lista1 = self.eliminar_elementos_vacios(lista)
        for i in range(3):
            if lista1[i:i+3] == ['"', '"', '"']:
                return True
            elif lista1[i:i+3] == ["'", "'", "'"]:
                return True

        return False
     
    def contiene_dos_comillas_consecutivas(self, lista):
        lista1 = self.eliminar_elementos_vacios(lista)    
        for i in range(2):
            if lista1[i:i+2] == ['"', '"']:
                    return True
            elif lista1[i:i+2] == ["'", "'",]:
                return True
        return False
    
    def varios_strings_consecutivos(self, lista):
        lista1 = self.eliminar_elementos_vacios(lista)  
        for i in range(len(lista1)-1):
            if lista1[i] == "tk_string" and lista[i+1] == "tk_string":
                return True
        return False   
        
    def eliminar_elementos_vacios(self, lista):
        lista_sin_vacios = [elemento for elemento in lista if elemento.strip() != ""]
        return lista_sin_vacios


        
        
    def espacios(self):
        if self.detener != True:
            token = self.tokens[0]

            while token.token == "tk_espacio" or token.token == "tk_salto_linea":
                self.tokens.pop(0) 
                if self.detener == True:
                    break
                else:
                    token = self.tokens[0] 
                    
    def espacios_sinsalto(self):
        if self.detener != True:
            token = self.tokens[0]
            
            while token.token == "tk_espacio":
                self.tokens.pop(0) 
                if self.detener == True:
                    break
                else:
                    token = self.tokens[0]            
             
    
    def claves2(self):
        self.palabras_clave = []
        validar_clave = claves()
        
        completado = False
        tk_valido = "tk_claves"
        validar = ""
        tokens_leidos = [] 
         
        while completado == False:
            
            self.espacios()
            token = self.tokens[0]
            self.espacios()
            
            tokens_leidos.append(token.token)
            print (token.token)

            if token.token == "tk_string":
                validar = self.datos_string(token.palabra)
                if validar in self.tokens_reservados:  
                    print(validar) 
                else:    
                    if "tk_corchete_in" in tokens_leidos or "tk_claves" in tokens_leidos or "tk_igual" in tokens_leidos:
                        tk_valido = "tk_grupo_claves"
                    
            elif token.token == "tk_comillas":
                tk_valido = "tk_grupo_claves"
                
            else:
                validar = token.token
            

            if  tk_valido == "tk_grupo_claves":
                print("inicio de claves")
                self.grupo_claves()
                tk_valido = validar_clave.inicio_clave(tk_valido, self.palabras_clave)
                
                
            else:
                tk_valido = validar_clave.inicio_clave(validar, token.palabra)
                self.tokens.pop(0)
                self.espacios()
        
            completado = validar_clave.completado()
            print(completado)
        validar_clave.mostrar_datos()    
                
    
            
                 
    def grupo_claves(self):
        clave_repitencia = False
        while True:
           
            if clave_repitencia:
                self.fin_claves()
                break
            else:
                clave_repitencia = self.clave_coma()
            
        
        for i in self.palabras_clave:
            print(i)      

                
                           
            
    def fin_claves(self):
        self.espacios()
        token = self.tokens[0]
        print(token.token)
        self.espacios()  
        if token.token == "tk_corchete_fin":
            print ("fin de claves")
        else:
            error = ["[", "Error Sintactico: Se esperaba un corchete de cierre", token.linea, token.col]
            self.errores.append(error)
            print("Error: Se esperaba un corchete de cierre")
            #agregar a la tabla de errores

    def clave_coma(self):
        validacion = False
        self.espacios()
        token = self.tokens[0]
        print("primer token =" + token.token)

        if token.token == "tk_comillas":
            self.tokens.pop(0)
            self.espacios()
            token = self.tokens[0]
            #print("2 token =" + token.token)
        else:
            error = ['"', "Error Sintactico: Se esperaba una comilla", token.linea, token.col]
            self.errores.append(error)
            print("Error: Se esperaba una comilla" )
            #agregar a la tabla de errores
        
        
        if token.token == "tk_string":
            self.palabras_clave.append(token.palabra)
            self.tokens.pop(0)
            self.espacios_sinsalto()
            token = self.tokens[0]
            #print("3 token =" + token.token)
            #print(token.palabra)
            

        if token.token == "tk_comillas":
            self.tokens.pop(0)
            self.espacios_sinsalto()
            token = self.tokens[0]
            
            #print(token.token)
        
        else:
            print("Error: Se esperaba una comilla")
            #agregar a la tabla de errores 
            error = ['"', "Error Sintactico: Se esperaba una comilla", token.linea, token.col]
            self.errores.append(error)   
        self.espacios_sinsalto()
        
          
        if token.token == "tk_coma":
            print("clave leida")
            self.tokens.pop(0)
            self.espacios_sinsalto()
            
            if self.tokens[0].token == "tk_corchete_fin":
                
                print("Error: Se esperaba una clave")
                error = ['claves ', "Error Sintactico: Se esperaba una clave", token.linea, token.col]
                self.errores.append(error)
                self.tokens.pop(0)
                return True
            
            
        else:
            if self.tokens[0].token == "tk_comillas" or self.tokens[0].token == "tk_string" or self.tokens[0].token == "tk_coma":
                print("Error: Se esperaba una coma")
                error = [', ', "Error Sintactico: Se esperaba una coma", token.linea, token.col]
                self.errores.append(error)
                    
            else:
                return True
                
            #elif self.tokens[0].token == "tk_corchete_fin" or self.tokens[0].token == "tk_salto_linea": 
                #validacion = True
        

        self.espacios()
        print("1" + token.token)    
        if self.tokens[0].token == "tk_coma":
            print("se esperaba una clave")
            error = ['claves ', "Error Sintactico: Se esperaba una clave", token.linea, token.col]
            self.errores.append(error)
            self.tokens.pop(0)
            #agregar a la tabla de errores
        print("2" +token.token)
        
        return False
        
    
    
    def datos_string(self, dato):
        scann = scanner()
        inf = scann.revString(dato)
        
        if len(inf) == 0:
            print("Error: Se esperaba una palabra reservada")
            #agregar a la tabla de errores
            return ""
        
        if inf[0] != "":
            print("Error lexico", inf[0])
            #agregar a la tabla de errores
            
        if inf[1] != "":
            token = scann.clasificar(inf[1])
            return token
        
    
    
    def registros(self):
        self.palabras_registros = []
        validar_registro = registros()
        
        completado = False
        tk_valido = "tk_registros"
        validar = ""
        tokens_leidos = [] 
         
        while completado == False:
            
            self.espacios()
            token = self.tokens[0]
            self.espacios()
            
            tokens_leidos.append(token.token)

            if token.token == "tk_string":
                validar = self.datos_string(token.palabra)
                if validar in self.tokens_reservados:  
                    print(validar) 
                    
            elif token.token == "tk_llave_in" or token.token == "tk_comillas":
                tk_valido = "tk_grupo_registros"
                
            else:
                validar = token.token
            

            if  tk_valido == "tk_grupo_registros":
                print("inicio de registros")
                conjunto = self.conjunto_registros()
                tk_valido =  validar_registro.inicio_registro(tk_valido, conjunto, token)               
                
            else:
                tk_valido = validar_registro.inicio_registro(validar, token.palabra, token)
                self.tokens.pop(0)
                #self.espacios()
        
            completado = validar_registro.completado()
            print(completado)
        
        validar_registro.encontrar_error()
        self.llenar_errores(validar_registro.errores)
    
    def llenar_errores(self, errores):
        for i in errores:
            self.errores.append(i)    
    
    def conjunto_registros(self):
        conjunto = []
        completado = False
        
        while completado == False:
            token = self.tokens[0]
            if token.token == "tk_corchete_fin" or token.token in self.tokens_reservados:
                break
            agregar = self.grupo_registros()
            if agregar[0] != None:
                conjunto.append(agregar[0])
            completado = agregar[1]
        
        print("conjunto de registros")
        print(conjunto)
        return conjunto
    
    
    def grupo_registros(self):
        
        grupo = grupo_registro()
        completado = False
        grupo_completado = False
        grupo_palabras = []
        
        tk_valido = "tk_llave_in"
        validar = ""
        i=0
        token = self.tokens[0]
        print("el token ingresado" + str(token.token))
        
        
        
        while completado == False:
            
            
            self.espacios_sinsalto()
            token = self.tokens[0]
            
            self.espacios_sinsalto()
            
            if token.token in ["tk_corchete_fin"] or token.token in self.palabras_reservadas:
                grupo_completado = True
                break
            
            if token.token == "tk_string" or token.token == "tk_comillas" or token.token == "tk_numero":
                tk_valido = "tk_grupo_palabras"
                
            else:
                validar = token.token
                
            if tk_valido == "tk_grupo_palabras":
                print("inicio de grupo de palabras")
                grupo_palabras = self.grupo_palabras()
                completado = grupo.inicio_grupo_registro(tk_valido, grupo_palabras, token)
                tk_valido = "tk_llave_fin"
            else:
                completado = grupo.inicio_grupo_registro(validar, token.palabra, token)
                self.tokens.pop(0)
            
            i+=1
            print(completado)
        
        print("buscar error")
        print (grupo.informacion)
        grupo.encontrar_error()
        self.llenar_errores(grupo.errores)
            
        print("grupo de palabras")
        if grupo.vacio() == False:
            print(grupo.datos)
            self.datos_registros.append(grupo_palabras)
        else:
            return None, grupo_completado
        
        return grupo.datos, grupo_completado   
                
             
    def grupo_palabras(self):
        conjunto = []
        completado = False
        
        while completado == False:

            palabra = self.palabras()
            if palabra[0] != None:
                conjunto.append(palabra[0])
            completado = palabra[1]
        
        return conjunto
            

    def palabras(self):
        palabras = grupo_palabras()
        
        completado = False
        grupo_completado = False
        palabras.contador = 0
        tk_valido = ""
        self.espacios_sinsalto()
        token = self.tokens[0]
        es_numero = False
        if token.token == "tk_numero":
            es_numero = True
            tk_valido = "tk_numero"
        elif token.token == "tk_comillas" or token.token == "tk_string":
            es_numero = False
            tk_valido = "tk_comillas"
        elif token.token == "tk_coma":
            #colocar instrucciones de errores
            print("Error: Se esperaba un numero o una palabra")
            error = ['Numero o palabra ', "Error Sintactico: Se esperaba un numero o una palabra", token.linea, token.col]
            self.errores.append(error)
            self.tokens.pop(0)
            return [None, True]
        elif token.token == "tk_corchete_fin" or token.token == "tk_llave_in" or token.token == "tk_llave_fin" or token.token == "tk_salto_linea":
            return [None, True]
        
        while completado == False:
            
            self.espacios_sinsalto()
            token = self.tokens[0]
            self.espacios_sinsalto()
            valores = palabras.inicio(token.token, token.palabra, es_numero, token)
            completado = valores[0]
            grupo_completado = valores[1]
            
            if completado == False:
                self.tokens.pop(0)
            else:
                if token.token == "tk_coma":
                    self.tokens.pop(0)
        
        if es_numero:
            dato = palabras.datos_numero[0]
            print(dato)
        else:
            dato = palabras.datos_coma[1]
            print(dato)  
        
        #errores
        analizar = self.tokens[0].token
        palabras.encontrar_error(es_numero, analizar)
        self.llenar_errores(palabras.errores)
            
        return dato, grupo_completado
            
            
    
    def imprimir(self):
        im = imprimir()
        self.espacios()
        token = self.tokens[0]
        completado = False

        if token.token == "tk_salto_linea":
           
            token = self.tokens.pop(0)
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)   
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                
        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
               
    def imprimirln(self):
        im = imprimirln()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string"  :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra,token)
                    self.tokens.pop(0)
            else:
                
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]

            
    def datos(self):
        im = datos()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo

            completado = im.insertar_dato(token.token, token.palabra, token)
            self.tokens.pop(0)    
            self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def conteo(self):
        im = conteo()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo

            completado = im.insertar_dato(token.token, token.palabra, token)
            self.tokens.pop(0)    
            self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def promedio(self):
        im = promedio()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string" or token.token == "tk_numero" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)  
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                
        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def contarsi(self):
        im = contarsi()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            
            if token.token != "tk_numero":
                tipo = self.datos_string(token.palabra)
                if tipo != None:
                    token.token = tipo
                
            
            if token.token == "tk_comillas" or token.token == "tk_string":
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token) 
                    self.tokens.pop(0)

            else:

                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                
        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3] , im.datos[6]
    
    def sumar(self):
        im = sumar()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:

            if token.token != "tk_numero":
                tipo = self.datos_string(token.palabra)    
                if tipo != None:
                    token.token = tipo
            print(token.token)
            
            if token.token == "tk_comillas" or token.token == "tk_string" or token.token == "tk_numero" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)   
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto() 

            token = self.tokens[0]
                
        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def max(self):
        im = maximo()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string" or token.token == "tk_numero" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)   
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def min(self):
        im = minimo()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            tipo = self.datos_string(token.palabra)
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string" or token.token == "tk_numero" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)  
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                #self.espacios_sinsalto()

            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    def exportarReporte(self):
        im = exportar_reporte()
        self.espacios()
        token = self.tokens[0]
        completado = False
        
        
        while completado == False:
            
            
            tipo = self.datos_string(token.palabra)
            
            
            if tipo != None:
                token.token = tipo
            
            if token.token == "tk_comillas" or token.token == "tk_string" or token.token == "tk_numero" :
                if token.token == "tk_string":
                    palabra = self.formar_palabra()
                    completado = im.insertar_dato("tk_string", palabra, token)
                elif token.token == "tk_comillas":
                    completado = im.insertar_dato(token.token, token.palabra, token)   
                    self.tokens.pop(0)
            else:
                completado = im.insertar_dato(token.token, token.palabra, token)
                self.tokens.pop(0)    
                self.espacios_sinsalto()
            
            if self.detener():
                completado = True
            else:
                token = self.tokens[0]
                

        im.ejecutar_errores()
        self.llenar_errores(im.errores)
        
        return im.datos[0], im.datos[3]
    
    
    def detener(self):
        if len(self.tokens) == 0:
            return True
    
    def formar_palabra(self):
        palabra = ""
        token = self.tokens[0]
        while token.token != "tk_comillas" and token.token != "tk_salto_linea" and token.token != "tk_parentesis_fin" and token.token != "tk_punto_coma":
            palabra += str(token.palabra)
            self.tokens.pop(0)
            token = self.tokens[0]
        return palabra 
    
   
    def eliminar_espacios(self):
        token = self.tokens[0]
        
        while self.tokens:
            if token.token not in ["tk_espacio", "tk_salto_linea"]:
                break  # Detener la eliminación cuando se encuentra una palabra diferente
            else:
                self.tokens.pop(0)
                token = self.tokens[0]

    def eliminar_sinsalto(self):
        token = self.tokens[0]
        
        while self.tokens:
            if token.token not in ["tk_espacio"]:
                break  # Detener la eliminación cuando se encuentra una palabra diferente
            else:
                self.tokens.pop(0)
                token = self.tokens[0]
        
    
    def analizar_valor(self):
        
        self.eliminar_espacios()
        token = self.tokens[0]
        comillas_cant = 0
        valor = self.datos_string(token.palabra)
        
        if valor in self.tokens_reservados:
             
            return valor
        
        
        if token.token == "tk_sim_numeral":
            valor = "comentario"
            return valor
        
        fila = []
        
        i=0
        while token.token != "tk_salto_linea":
            token = self.tokens[i]
            fila.append(token.palabra)
            i+=1

        print(fila)
        
        contiene = self.contiene_tres_comillas_consecutivas(fila)
        print(contiene)
        if contiene:
            valor = "comentario"
            return valor
        else:
            contiene = self.contiene_dos_comillas_consecutivas(fila)
            if contiene:
                valor = "comentario"
                return valor
            else:
                contiene = self.encontrar_llaves(fila)
                if contiene:
                    valor = "tk_llaves"
                    return valor
                else:
                    contiene = self.encontrar_corchetes(fila)
                    if contiene:
                        valor = "tk_corchetes"
                        return valor
                    else:
                        while token.token != "tk_salto_linea":
                            self.tokens.pop(0)
                            token = self.tokens[0]
                            valor = None

        '''
        if token.token == "tk_comillas":
            a = self.tokens[0]
            if a.token == "tk_comillas":
                comillas_cant += 1
            b = self.tokens[1]
            if b.token == "tk_comillas":
                comillas_cant += 1
            c = self.tokens[2]
            if c.token == "tk_comillas":
                comillas_cant += 1
            
        if comillas_cant <= 2:
            valor = "comentario" 
        
        
        '''
                 
        return valor
    
    
    def encontrar_corchetes(self,  lista):
        for elemento in lista:
            if "[" in elemento or "]" in elemento:
                return True
        return False
    
    def encontrar_llaves(self, lista):
        for elemento in lista:
            if "{" in elemento or "}" in elemento:
                return True
        return False
    
    def exportar_datos(self):
        valor = ""
        imprimir_consola = []
        valor = self.analizar_valor()
        print(valor)
        

        while len(self.tokens) != 0:
            valor = self.analizar_valor()
            print(valor)
            
            if valor == "comentario":
                enviar = self.comentario2()
                imprimir_consola.append(datos_consola("comentario", enviar))
                self.arbol_derivacion.append("comentario")
            elif valor == "tk_claves":
                self.claves2()
                self.arbol_derivacion.append("claves")
            elif valor == "tk_registros":
                self.registros()
                self.arbol_derivacion.append("registros")
            elif valor == "tk_imprimir":
                enviar = self.imprimir()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("imprimir")
            elif valor == "tk_imprimirln":
                enviar = self.imprimirln()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("imprimirln")
            elif valor == "tk_datos":
                enviar = self.datos()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("datos")
            elif valor == "tk_conteo":
                enviar = self.conteo()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("conteo")
            elif valor == "tk_promedio":
                enviar = self.promedio()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("promedio")
            elif valor == "tk_contarsi":
                enviar = self.contarsi()
                valores = [ enviar[1], enviar[2]]
                imprimir_consola.append(datos_consola(enviar[0], valores))
                self.arbol_derivacion.append("contarsi")
            elif valor == "tk_sumar":
                enviar = self.sumar()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))   
                self.arbol_derivacion.append("sumar")
            elif valor == "tk_max":
                enviar = self.max()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("max")
            elif valor == "tk_min":
                enviar = self.min()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("min")
            elif valor == "tk_exportarreporte":
                enviar = self.exportarReporte()
                imprimir_consola.append(datos_consola(enviar[0], enviar[1]))
                self.arbol_derivacion.append("exportarreporte")
            else:
                print("Error: linea no reconocida")
                token = self.tokens[0]
                while token.token != "tk_salto_linea":
                            self.tokens.pop(0)
                            token = self.tokens[0]
                            valor = None
                 

        return imprimir_consola

    def mostrar(self):
        for i in self.tokens:
            print(i.palabra, i.token, i.linea, i.col)
    
    
    
if __name__ == '__main__':
    ta = scanner()
    
    
    ruta = "basico.txt"
    archivo = open(ruta, 'r')
    dato = archivo.read()
    ta.lectura(dato)
    ta.encontrar_errores()
    
    par = parserL(ta.tokens, ta.errores)
    par.mostrar()
    
    '''
    comentario = par.comentario()
    print(comentario)

    comentario = par.comentario()
    print(comentario)

    comentario = par.comentario()
    print(comentario)

    par.claves2()

    par.registros()
    par.imprimir()
    par.imprimir()
    par.imprimirln()
    par.imprimirln()
    par.datos()
    par.conteo()
    par.promedio()
    par.contarsi()
    par.sumar()
    par.max()
    par.min()
    par.exportarReporte()
    '''
    


    imprimir_consola = par.exportar_datos()
    
    for i in imprimir_consola:
        print("accion" + i.accion, "dato" + str(i.dato))
        
    print(par.palabras_clave)

    print(par.datos_registros)
    


    print (par.errores)


