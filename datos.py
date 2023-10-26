from tokens import tk
import copy

class scanner:
    def __init__(self):
        self.tokens = []
        self.palabras_reservadas = ["claves", "clave", "registros", "registro", "imprimir", "imprimirln", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]
        self.alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" ,"k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s" ,"t", "u", "v", "w", "x", "y", "z"]
        self.caracteres_alfa = ["[", "]", "{", "}", "(", ")", ",", ";", "=", " ", "\t", "\n", '"', "'", "#", ":", ".", "_", "-"]
        self.errores = []
        
    def lectura (self, dato):
        line = 1
        col= 1
        i = 0
        
        while i < len(dato):
            char = dato[i]
            if char.isspace():
                if char == "\n":
                    self.tokens.append(tk("\n", "tk_salto_linea", line, col))
                    line += 1
                    col = 1
                elif char == "\t":
                    col += 4
                else:
                    self.tokens.append(tk(char, "tk_espacio", line, col))
                    col += 1
                i += 1
            
            elif char in ["#"]:
                self.tokens.append(tk(char, "tk_sim_numeral", line, col))
                col += 1
                i += 1
            elif char in ["'", '"']:
                self.tokens.append(tk(char, "tk_comillas", line, col))
                col += 1
                i += 1

            elif char in ["="]:
                self.tokens.append(tk(char, "tk_igual", line, col))
                col += 1
                i += 1
            elif char == "[":
                self.tokens.append(tk(char, "tk_corchete_in", line, col))  
                col += 1
                i += 1
            elif char == "]":
                self.tokens.append(tk(char, "tk_corchete_fin", line, col))  
                col += 1
                i += 1
            elif char == "(":
                self.tokens.append(tk(char, "tk_parentesis_in", line, col))
                col += 1 
                i += 1   
            elif char ==")":
                self.tokens.append(tk(char, "tk_parentesis_fin", line, col))
                col += 1
                i += 1
            elif char == "{" :
                self.tokens.append(tk(char, "tk_llave_in", line, col))
                col += 1
                i += 1
            elif char == "}":
                self.tokens.append(tk(char, "tk_llave_fin", line, col))
                col += 1
                i += 1
            elif char == ",":
                self.tokens.append(tk(char, "tk_coma", line, col))
                col += 1
                i += 1
            elif char == ";":
                self.tokens.append(tk(char, "tk_punto_coma", line, col))
                col += 1
                i += 1
            
            elif char.isdigit():
                number, pos = self.numeros(dato[i:], i)
                col += pos - i
                i = pos
                token = tk(number, "tk_numero", line, col)
                self.tokens.append(token)
            
            
            else:
                string, pos = self.textos(dato[i:], i)
                col += len(string) + 1
                i = pos + 1
                token = tk(string,"tk_string", line, col)
                self.tokens.append(token)
                  
 
    

    def textos(self,dato, i):
        token = ""
        for char in dato:
            if char in ["[" , "]" , "{ " , "{ " , "(" , ")" , "," , ";" , "=" , " " , "\t" , "\n" , '"', "'"]:
                return [token, i-1]
            token += char
            i += 1
        print("Error: string no cerrado")


    # token para los numeros
    def numeros(self, dato, i):
        token = ""
        isDecimal = False
        for char in dato:
            if char.isdigit():
                token += char
                i += 1
            elif char == "." and not isDecimal:
                token += char
                i += 1
                isDecimal = True
            else:
                break
        if isDecimal:
            return [float(token), i]
        return [int(token), i]
    
    
    
    def mostra_tabla(self):
        for i in self.tokens:
            print(i.palabra, i.token, i.linea, i.col)
    
    def encontrar_errores(self):
        
        
        for i in self.tokens:
            if i.token == "tk_string":
                palabra = i.palabra
                if len(palabra) == 1:
                    if palabra in ["[", "]", "{", "}", "(", ")", ",", ";", "="]:
                        m = 0
                    else:
                        error = [i.palabra, "Error Lexico: caracter no valido", i.linea, i.col]
                        self.errores.append(error)
                        self.tokens.remove(i)
                else:
                    palabra = palabra.lower()
                    if palabra in self.palabras_reservadas:
                        m = 0
                    else: 
                        for j in palabra:    
                            if j in self.alfabeto or j.isdigit() or j in self.caracteres_alfa:
                                m= 0
                            else:
                                print("error lexico, caracter no valido")
                                palabra = palabra.replace(j, "")
                        
                        
                        if palabra == "":
                            error = [i.palabra, "Error Lexico: palabra no valida", i.linea, i.col]
                            self.tokens.remove(i)
                            #self.tokens.remove(i)
                
        
        
    
    
    def revString(self, strin):
        palabras = ["claves", "clave", "registros", "registro",  "imprimirln", "imprimir", "datos", "conteo", "promedio", "contarsi", "sumar" ,"max", "min", "exportarreporte" ]
        string = strin.lower()
        errores = []
        error = ""
        palabra = ""
        for i in palabras:

            j = 0
            k = 0
            while j < len(i) and k < len(string):
                if i[j] == string[k]:
                    palabra += string[k]
                    j += 1
                    k += 1
                    
                else:
                    error = string[k]
                    k += 1
                    
            
            if palabra == i:
                    break
            else:
                palabra = ""
                error = ""

        return error, palabra 
        
    
    def clasificar(self, dato):
        clasificacion = ""
        if dato == "clave":
            clasificacion = "tk_claves"
        elif dato == "claves":
            clasificacion = "tk_claves"
        elif  dato == "registro":
            clasificacion = "tk_registros"
        elif dato == "registros":
            clasificacion = "tk_registros"
        elif dato == "imprimir":
            clasificacion = "tk_imprimir"
        elif dato == "imprimirln":
            clasificacion = "tk_imprimirln"
        elif dato == "datos":
            clasificacion = "tk_datos"
        elif dato == "conteo":
            clasificacion = "tk_conteo"
        elif dato == "promedio":
            clasificacion = "tk_promedio"
        elif dato == "contarsi":
            clasificacion = "tk_contarsi"
        elif dato == "sumar":
            clasificacion = "tk_sumar"
        elif dato == "max":
            clasificacion = "tk_max"
        elif dato == "min":
            clasificacion = "tk_min"
        elif dato == "exportarreporte":
            clasificacion = "tk_exportarreporte"
               
        return clasificacion
    
    def hacer_copy(self):
        tokens = copy.copy(self.tokens)
        return tokens
        
    
if __name__ == '__main__':
    ta = scanner()
    
    
    ruta = "basico.txt"
    archivo = open(ruta, 'r')
    dato = archivo.read()
    ta.lectura(dato)
    ta.encontrar_errores()
    ta.mostra_tabla()
    
   
    for i in ta.tokens:
        print(i.palabra, i.token, i.linea, i.col)
    
    
    
    '''
    resultados = ta.revString("musa")
    print(resultados)
    
    clasificacion = ta.clasificar(resultados[1])
    print (len(clasificacion))
    
    '''
    
    