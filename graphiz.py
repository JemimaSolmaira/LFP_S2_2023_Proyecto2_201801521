import os

class Grafica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contador = 0



    def encabezado(self):
        Encabezado = "digraph " + '"' + "Arbol_Binario" + '"' + " { \n\n "
        Encabezado += "fontname=" + '"' + "black" + '"' + "\n\n"
        Encabezado += "node [fontname=" + '"' + "black" + '"' + "]" + "\n\n"
        Encabezado += "edge [fontname=" + '"' + "black" + '"' + "]" + "\n\n"
        Encabezado += "graph [newrank = true , nodesep = 0.8, overlap = true, splines = false]" + "\n\n"
        Encabezado += "node [fixedsize = false, fontsize = 24, height = 2, shape = " + '"' + "circle" + '"' + ", style = " + '"' + "filled,setlinewidth(5)" + '"' + ", width = 2.2, shape = " + '"' + "circle" + '"' + ",color = " + '"' + "black" + '"' + " , fillcolor = " + '"' + "cornflowerblue" + '"' + " ]" + "\n\n"
        Encabezado += "edge [ arrowsize = 0.5, weight = 2, style = " + '"' + "filled,setlinewidth(5)" + '"' + "row = func, arrowhead = 0.1,color = " + '"' + "black" + '"' + ", row = func ]" + "\n\n"
        
        
        return Encabezado        
    
    def comentario(self, inicio):
        comentario = ""

        self.contador += 1
        comentario += "subgraph Comentario {" + "\n"
        
        if inicio != None:
            comentario += inicio + " -> " + "inicio" + str(self.contador) + "\n"
        
        comentario += "inicio" + str(self.contador) + " [label = " + '"' + "Inicio" + '"' + "]" + "\n"
        self.contador +=1
        comentario += "comentario" + str(self.contador) + " [label = " + '"' + "Comentario" + '"' + "]" + "\n"
        comentario += "inicio" + str(self.contador - 1) + "->" + "comentario" + str(self.contador) + "\n"
        self.contador +=1
        comentario += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        comentario += "comentario" + str(self.contador - 1) + "->" + "C" + str(self.contador) + "\n"
        self.contador +=1
        enviar = "comentario_sig" + str(self.contador)
        comentario += "comentario" + str(self.contador - 2) + "->" + enviar + "\n"
        comentario += enviar + " [label = " + '"' + "Comentario" + '"' + "]" + "\n"
        comentario += "}" + "\n"
        
        return comentario, enviar
  
  
    def claves(self, inicio):
        claves = ""
        self.contador += 1
        claves += "subgraph Claves {" + "\n"
        if inicio != None:
            claves += inicio + " -> " + "inicio" + str(self.contador) + "\n"
        
        
        claves += "inicio" + str(self.contador) + " [label = " + '"' + "Inicio" + '"' + "]" + "\n"
        self.contador +=1
        enviar = "claves" + str(self.contador)
        claves += "inicio" + str(self.contador-1) + "->" + "claves" + str(self.contador) + "\n"
        claves += "claves" + str(self.contador) + " [label = " + '"' + "Claves" + '"' + "]" + "\n"
        self.contador +=1
        claves += "C" + str(self.contador) + " [label = " + '"' + "tk_claves" + '"' + "]" + "\n"
        self.contador +=1
        claves += "C" + str(self.contador) + " [label = " + '"' + "tk_igual" + '"' + "]" + "\n"
        self.contador +=1
        claves += "C" + str(self.contador) + " [label = " + '"' + "tk_corchete_in" + '"' + "]" + "\n"
        
        claves += enviar + "->" + "C" + str(self.contador - 2) + "\n"
        claves += enviar + "->" + "C" + str(self.contador - 1) + "\n"
        claves += enviar + "->" + "C" + str(self.contador) + "\n"
        claves += "}" + "\n"
    
        return claves, enviar
    
    def claves_inicio(self, inicio):
        claves_inicio = ""
        self.contador += 1
        claves_inicio += "subgraph Claves_Inicio {" + "\n"  
        claves_inicio += inicio + " -> " + "grupo_claves"+ str(self.contador) + "\n"  
        
        enviar = "grupo_claves" + str(self.contador)
        claves_inicio += "grupo_claves" + str(self.contador) + " [label = " + '"' + "Grupo_claves" + '"' + "]" + "\n"
        self.contador +=1
        claves_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        claves_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        claves_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        
        claves_inicio += enviar + "->" + "C" + str(self.contador - 2) + "\n"
        claves_inicio += enviar + "->" + "C" + str(self.contador - 1) + "\n"
        claves_inicio += enviar + "->" + "C" + str(self.contador) + "\n"
        claves_inicio += "}" + "\n"
        
        return claves_inicio, enviar
    
    def claves_dinamicas(self, inicio):
        claves_dinamicas = ""
        self.contador += 1
        claves_dinamicas += "subgraph Claves_dinamicas {" + "\n"  
        claves_dinamicas += inicio + " -> " + "clave_sig"+ str(self.contador) + "\n"  
        
        clave_sig = "clave_sig" + str(self.contador)
        claves_dinamicas += "clave_sig" + str(self.contador) + " [label = " + '"' + "clave_sig" + '"' + "]" + "\n"
        self.contador +=1
        claves_dinamicas += "C" + str(self.contador) + " [label = " + '"' + "tk_coma" + '"' + "]" + "\n"
        self.contador +=1
        claves_dinamicas += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        claves_dinamicas += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        claves_dinamicas += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        
        claves_dinamicas += clave_sig + "->" + "C" + str(self.contador - 3) + "\n"
        claves_dinamicas += clave_sig + "->" + "C" + str(self.contador - 2) + "\n"
        claves_dinamicas += clave_sig + "->" + "C" + str(self.contador - 1) + "\n"
        claves_dinamicas += clave_sig + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "grupo_claves" + str(self.contador)
        claves_dinamicas += clave_sig + "->" + enviar + "\n"
        claves_dinamicas += enviar + " [label = " + '"' + "Grupo_claves" + '"' + "]" + "\n"
        claves_dinamicas += "}" + "\n"
        
        return claves_dinamicas, enviar
    
    def claves_fin(self, inicio):
        claves_fin = ""
        self.contador += 1
        claves_fin += "subgraph Claves_fin {" + "\n"
        claves_fin += inicio + " -> " + "clave_sig"+ str(self.contador) + "\n"
        claves_fin += "clave_sig" + str(self.contador) + " [label = " + '"' + "clave_sig" + '"' + "]" + "\n"
        self.contador +=1
        claves_fin += "C" + str(self.contador) + " [label = " + '"' + "tk_corchete_fin" + '"' + "]" + "\n"
        claves_fin += "clave_sig" + str(self.contador - 1) + "->" + "C" + str(self.contador) + "\n"
        self.contador +=1
        enviar = "inicio_registros" + str(self.contador)
        claves_fin += "clave_sig" + str(self.contador - 2) + "->" + enviar + "\n"
        claves_fin += enviar + " [label = " + '"' + "Inicio_registros" + '"' + "]" + "\n"
        claves_fin += "}" + "\n"
        
        return claves_fin, enviar
        

    def registros(self, inicio):
        registros = ""
        self.contador += 1
        registros += "subgraph Registros {" + "\n"
        registros += inicio + " -> " + "inicio"+ str(self.contador) + "\n"
        registros += "inicio" + str(self.contador) + " [label = " + '"' + "Inicio" + '"' + "]" + "\n"
        self.contador +=1
        enviar = "registros" + str(self.contador)
        registros += "inicio" + str(self.contador-1) + "->" + enviar + "\n"
        registros += enviar + " [label = " + '"' + "Registros" + '"' + "]" + "\n"
        self.contador +=1
        registros += "C" + str(self.contador) + " [label = " + '"' + "tk_registros" + '"' + "]" + "\n"
        self.contador +=1
        registros += "C" + str(self.contador) + " [label = " + '"' + "tk_igual" + '"' + "]" + "\n"
        self.contador +=1
        registros += "C" + str(self.contador) + " [label = " + '"' + "tk_corchete_in" + '"' + "]" + "\n"
        
        registros += enviar + "->" + "C" + str(self.contador - 2) + "\n"
        registros += enviar + "->" + "C" + str(self.contador - 1) + "\n"
        registros += enviar + "->" + "C" + str(self.contador) + "\n"
        registros += "}" + "\n"
    
        return registros, enviar
    
    
    def registro_inicio(self, inicio):
        registro_inicio = ""
        self.contador += 1
        registro_inicio += "subgraph registro_inicio {" + "\n"  
        registro_inicio += inicio + " -> " + "grupo_registros"+ str(self.contador) + "\n"  
        
        enviar = "grupo_registros" + str(self.contador)
        registro_inicio += enviar + " [label = " + '"' + "Grupo_claves" + '"' + "]" + "\n"
        self.contador +=1
        registro_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_llave_in" + '"' + "]" + "\n"
        self.contador +=1
        registro_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        registro_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        registro_inicio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        
        registro_inicio += enviar + "->" + "C" + str(self.contador - 3) + "\n"
        registro_inicio += enviar + "->" + "C" + str(self.contador - 2) + "\n"
        registro_inicio += enviar + "->" + "C" + str(self.contador - 1) + "\n"
        registro_inicio += enviar + "->" + "C" + str(self.contador) + "\n"
        registro_inicio += "}" + "\n"
        
        return registro_inicio, enviar
    
    
    def registros_dinamicos(self, inicio):
        registros_dinamicos = ""
        self.contador += 1
        registros_dinamicos += "subgraph Claves_dinamicas {" + "\n"  
        registros_dinamicos += inicio + " -> " + "reg_sig"+ str(self.contador) + "\n"  
        
        reg_sig = "reg_sig" + str(self.contador)
        registros_dinamicos += reg_sig + " [label = " + '"' + "reg_sig" + '"' + "]" + "\n"
        self.contador +=1
        registros_dinamicos += "C" + str(self.contador) + " [label = " + '"' + "tk_coma" + '"' + "]" + "\n"
        self.contador +=1
        registros_dinamicos += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        registros_dinamicos += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        registros_dinamicos += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        
        registros_dinamicos += reg_sig + "->" + "C" + str(self.contador - 3) + "\n"
        registros_dinamicos += reg_sig + "->" + "C" + str(self.contador - 2) + "\n"
        registros_dinamicos += reg_sig + "->" + "C" + str(self.contador - 1) + "\n"
        registros_dinamicos += reg_sig + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "grupo_registros" + str(self.contador)
        registros_dinamicos += reg_sig + "->" + enviar + "\n"
        registros_dinamicos += enviar + " [label = " + '"' + "Grupo_claves" + '"' + "]" + "\n"
        registros_dinamicos += "}" + "\n"
        
        return registros_dinamicos, enviar
    
    def registros_fin(self, inicio):
        registros_fin = ""
        self.contador += 1
        registros_fin += "subgraph Registros_fin {" + "\n"
        registros_fin += inicio + " -> " + "grupo_claves_fin"+ str(self.contador) + "\n"
        registros_fin += "grupo_claves_fin" + str(self.contador) + " [label = " + '"' + "Grupo_claves" + '"' + "]" + "\n"
        
        self.contador +=1
        enviar = "reg_fin" + str(self.contador)
        registros_fin += enviar + " [label = " + '"' + "reg_sig" + '"' + "]" + "\n"
        registros_fin += "grupo_claves_fin" + str(self.contador - 1) + "->" + enviar + "\n"
        
        self.contador +=1
        registros_fin += "C" + str(self.contador) + " [label = " + '"' + "tk_llave_fin" + '"' + "]" + "\n"
        self.contador +=1
        registros_fin += "C" + str(self.contador) + " [label = " + '"' + "tk_corchete_fin" + '"' + "]" + "\n"
        
        registros_fin += enviar + "->" + "C" + str(self.contador - 1) + "\n"
        registros_fin += enviar + "->" + "C" + str(self.contador) + "\n"
        registros_fin += "}" + "\n"
        
        return registros_fin, enviar
    

    def instrucciones(self, inicio):
        instrucciones = ""
        self.contador += 1
        instrucciones += "subgraph Instrucciones {" + "\n"
        instrucciones += inicio + " -> " + "inicio"+ str(self.contador) + "\n"
        instrucciones += "inicio" + str(self.contador) + " [label = " + '"' + "Inicio" + '"' + "]" + "\n"
        self.contador +=1
        enviar = "instrucciones" + str(self.contador)
        instrucciones += "inicio" + str(self.contador-1) + "->" + enviar + "\n"
        instrucciones += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        instrucciones += "}" + "\n"
        
        return instrucciones, enviar
        
    
    def imprimir(self, inicio):
        imprimir = ""
        self.contador += 1
        imprimir += "subgraph imprimir {" + "\n"
        im = "imprimir" + str(self.contador)
        imprimir += inicio + " -> " + im + "\n"
        imprimir += im + " [label = " + '"' + "Imprimir" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_imprimir" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        imprimir += im + "->" + "C" + str(self.contador - 6) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 5) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 4) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 3) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 2) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 1) + "\n"
        imprimir += im + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        imprimir += im + "->" + enviar + "\n"
        imprimir += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        imprimir += "}" + "\n"
        
        return imprimir, enviar
        
        
    def imprimirln(self, inicio):
        imprimir = ""
        self.contador += 1
        imprimir += "subgraph imprimirln {" + "\n"
        im = "imprimirln" + str(self.contador)
        imprimir += inicio + " -> " + im + "\n"
        imprimir += im + " [label = " + '"' + "Imprimirln" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_imprimirln" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        imprimir += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        imprimir += im + "->" + "C" + str(self.contador - 6) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 5) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 4) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 3) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 2) + "\n"
        imprimir += im + "->" + "C" + str(self.contador - 1) + "\n"
        imprimir += im + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        imprimir += im + "->" + enviar + "\n"
        imprimir += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        imprimir += "}" + "\n"
        
        return imprimir, enviar    
        
         
    def datos(self, inicio):
        datos = ""
        self.contador += 1
        datos += "subgraph Datos {" + "\n"
        da = "datos" + str(self.contador)
        datos += inicio + " -> " + da + "\n"
        datos += da + " [label = " + '"' + "Datos" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_datos" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        datos += da + "->" + "C" + str(self.contador - 3) + "\n"
        datos += da + "->" + "C" + str(self.contador - 2) + "\n"
        datos += da + "->" + "C" + str(self.contador - 1) + "\n"
        datos += da + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        datos += da + "->" + enviar + "\n"
        datos += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        datos += "}" + "\n"
        
        return datos, enviar
    
    
    def conteo(self, inicio):
        datos = ""
        self.contador += 1
        datos += "subgraph Conteo {" + "\n"
        da = "conteo" + str(self.contador)
        datos += inicio + " -> " + da + "\n"
        datos += da + " [label = " + '"' + "Conteo" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_datos" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        datos += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        datos += da + "->" + "C" + str(self.contador - 3) + "\n"
        datos += da + "->" + "C" + str(self.contador - 2) + "\n"
        datos += da + "->" + "C" + str(self.contador - 1) + "\n"
        datos += da + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        datos += da + "->" + enviar + "\n"
        datos += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        datos += "}" + "\n"
        
        return datos, enviar
        
        
    
    def promedio(self, inicio):
        promedio = ""
        self.contador += 1
        promedio += "subgraph Promedio {" + "\n"
        pro = "promedio" + str(self.contador)
        promedio += inicio + " -> " + pro + "\n"
        promedio += pro + " [label = " + '"' + "Promedio" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_promedio" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n" 
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        promedio += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        promedio += pro + "->" + "C" + str(self.contador - 6) + "\n"
        promedio += pro + "->" + "C" + str(self.contador - 5) + "\n"
        promedio += pro + "->" + "C" + str(self.contador - 4) + "\n"
        promedio += pro + "->" + "C" + str(self.contador - 3) + "\n"
        promedio += pro + "->" + "C" + str(self.contador - 2) + "\n"
        promedio += pro + "->" + "C" + str(self.contador - 1) + "\n"
        promedio += pro + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        promedio += pro + "->" + enviar + "\n"
        promedio += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        promedio += "}" + "\n"
        
        return promedio, enviar
    
    
    def contarsi(self, inicio):
        contarsi = ""
        self.contador += 1
        contarsi += "subgraph Contarsi {" + "\n"
        con = "contarsi" + str(self.contador)
        contarsi += inicio + " -> " + con + "\n"
        contarsi += con + " [label = " + '"' + "Contarsi" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_contarsi" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_coma" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_numero" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        contarsi += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        contarsi += con + "->" + "C" + str(self.contador - 8) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 7) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 6) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 5) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 4) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 3) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 2) + "\n"
        contarsi += con + "->" + "C" + str(self.contador - 1) + "\n"
        contarsi += con + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        contarsi += con + "->" + enviar + "\n"
        contarsi += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        contarsi += "}" + "\n"
        
        return contarsi, enviar
            
   
    
    def maximo(self, inicio):
        maximo = ""
        self.contador += 1
        maximo += "subgraph Maximo {" + "\n"
        ma = "maximo" + str(self.contador)
        maximo += inicio + " -> " + ma + "\n"
        maximo += ma + " [label = " + '"' + "Maximo" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_maximo" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        maximo += ma + "->" + "C" + str(self.contador - 6) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 5) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 4) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 3) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 2) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 1) + "\n"
        maximo += ma + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        maximo += ma + "->" + enviar + "\n"
        maximo += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        maximo += "}" + "\n"
        
        return maximo, enviar
        
        
    def minimo(self, inicio):
        maximo = ""
        self.contador += 1
        maximo += "subgraph Minimo {" + "\n"
        ma = "maximo" + str(self.contador)
        maximo += inicio + " -> " + ma + "\n"
        maximo += ma + " [label = " + '"' + "Minimo" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_minimo" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        maximo += ma + "->" + "C" + str(self.contador - 6) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 5) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 4) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 3) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 2) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 1) + "\n"
        maximo += ma + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        maximo += ma + "->" + enviar + "\n"
        maximo += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        maximo += "}" + "\n"
        
        return maximo, enviar  
   
    def suma(self, inicio):
        maximo = ""
        self.contador += 1
        maximo += "subgraph Suma {" + "\n"
        ma = "maximo" + str(self.contador)
        maximo += inicio + " -> " + ma + "\n"
        maximo += ma + " [label = " + '"' + "Suma" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_suma" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        maximo += ma + "->" + "C" + str(self.contador - 6) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 5) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 4) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 3) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 2) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 1) + "\n"
        maximo += ma + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        maximo += ma + "->" + enviar + "\n"
        maximo += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        maximo += "}" + "\n"
        
        return maximo, enviar 
    
    def exportar(self, inicio):
        maximo = ""
        self.contador += 1
        maximo += "subgraph Exportar {" + "\n"
        ma = "maximo" + str(self.contador)
        maximo += inicio + " -> " + ma + "\n"
        maximo += ma + " [label = " + '"' + "Exportar Reporte" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_exportarreporte" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_in" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_string" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_comillas" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_parentesis_fin" + '"' + "]" + "\n"
        self.contador +=1
        maximo += "C" + str(self.contador) + " [label = " + '"' + "tk_punto_coma" + '"' + "]" + "\n"
        
        maximo += ma + "->" + "C" + str(self.contador - 6) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 5) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 4) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 3) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 2) + "\n"
        maximo += ma + "->" + "C" + str(self.contador - 1) + "\n"
        maximo += ma + "->" + "C" + str(self.contador) + "\n"
        
        self.contador += 1
        enviar = "instrucciones" + str(self.contador)
        maximo += ma + "->" + enviar + "\n"
        maximo += enviar + " [label = " + '"' + "Instrucciones" + '"' + "]" + "\n"
        maximo += "}" + "\n"
        
        return maximo, enviar 
    
    
    def fin_arbol(self, inicio):
        fin = ""
        self.contador += 1
        fin += "subgraph Fin_arbol {" + "\n"
        fi = "fin_arbol" + str(self.contador)
        fin += inicio + " -> " + fi + "\n"
        fin += fi + " [label = " + '"' + "Fin_arbol" + '"' + "]" + "\n"
        fin += "}" + "\n"
        
        return fin
        

    
    def stringGeneral(self, array, claves, registros):
        parametros = []
        parametros = array
        
        string_general = self.encabezado()
        inicio = None
        
        for i in parametros:
 
            if i == "comentario":
                valores = self.comentario(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "claves":
                valores = self.claves(inicio)
                string_general += valores[0]
                inicio = valores[1]
                
                valores = self.claves_inicio(inicio)
                string_general += valores[0]
                inicio = valores[1]
                j = 0
                while j < claves:
                    valores = self.claves_dinamicas(inicio)
                    string_general += valores[0]
                    inicio = valores[1]
                    j += 1
                valores = self.claves_fin(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "registros":
                valores = self.registros(inicio)
                string_general += valores[0]
                inicio = valores[1]
                
                valores = self.registro_inicio(inicio)
                string_general += valores[0]
                inicio = valores[1]
                j = 0
                while j < registros:
                    valores = self.registros_dinamicos(inicio)
                    string_general += valores[0]
                    inicio = valores[1]
                    j += 1
                valores = self.registros_fin(inicio)
                string_general += valores[0]
                inicio = valores[1]
                
            elif i == "imprimir":
                valores = self.imprimir(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "imprimirln":
                valores = self.imprimirln(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "datos":
                valores = self.datos(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "conteo":
                valores = self.conteo(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "promedio":
                valores = self.promedio(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "contarsi":
                valores = self.contarsi(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "maximo":
                valores = self.maximo(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "minimo":
                valores = self.minimo(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "suma":
                valores = self.suma(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "exportar":
                valores = self.exportar(inicio)
                string_general += valores[0]
                inicio = valores[1]
            elif i == "fin_arbol":
                valores = self.fin_arbol(inicio)
                string_general += valores
                inicio = None
        
        string_general += "}" 
        return string_general

        
        
        
    
    def crearArchivo(self, string):
        nombrearchivo = self.nombre + ".dot"
        archivo = open(nombrearchivo, "w")
        archivo.write(string)
        archivo.close()
    
    def ConvertirArchivo(self):
        archivo = self.nombre + ".dot"
        imagen = self.nombre + ".svg"
        comando = "dot -Tsvg " + archivo + " > " + imagen
        os.system(comando)
        
        
        
if (__name__ == "__main__"):

    
    grupos = []
    grupos.append("comentario")
    grupos.append("comentario")
    grupos.append("claves")
    grupos.append("registros")
    grupos.append("imprimir")
    grupos.append("contarsi")
    grupos.append("maximo")
    grupos.append("minimo")
    grupos.append("suma")
    grupos.append("exportar")
    grupos.append("conteo")
    grupos.append("promedio")
    grupos.append("contarsi")
    grupos.append("fin_arbol")
     
    graph = Grafica("Arbol_derivacion")
    
    
    
    contenido = graph.stringGeneral(grupos, 3, 3)
    graph.crearArchivo(contenido)
    graph.ConvertirArchivo()
    