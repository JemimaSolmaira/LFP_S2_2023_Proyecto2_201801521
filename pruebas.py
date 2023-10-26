from tokens import tk

'''
data = [
    ["Nombre", "Edad", "Ciudad", "Puntuación", "Fecha"],
    ["Alice", 25, "Nueva York", 95.5, "2023-10-23"],
    ["Bob", 30, "Los Ángeles", 88.2, "2023-10-23"],
    ["Charlie", 22, "Chicago", 75.0, "2023-10-23"],
    ["David", 28, "Miami", 92.8, "2023-10-23"]
]

# Calcular la longitud máxima de cada columna
column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

# Imprimir la tabla con alineación
for row in data:
    formatted_row = "|".join("{:{}}".format(item, width) for item, width in zip(row, column_widths))
    print(formatted_row)

# La línea de separación entre la cabecera y los datos
separator = "+".join("-" * width for width in column_widths)
print(separator)


'''


def contiene_tres_comillas_consecutivas(lista):
    for i in range(3):
        if lista[i:i+3] == ['"', '"', '"']:
            return True
        elif lista[i:i+3] == ["'", "'", "'"]:
            return True
        elif lista[i:i+2] == ["'", '"']:
            return True
        elif lista[i:i+2] == ['"', "'"]:
            return True
    return False

# Ejemplo de uso
mi_lista = ['"', '"', '"',  ':', '/', '"', '"']
resultado = contiene_tres_comillas_consecutivas(mi_lista)

if resultado:
    print("La lista contiene tres comillas consecutivas.")
else:
    print("La lista no contiene tres comillas consecutivas.")

mi_lista2 = ["tk_string", "tk_string", "tk_string",  "tk_string", '/', '"', '"']

def varios_strings_consecutivos( lista):
        for i in range(len(lista)-1):
            if lista[i] == "tk_string" and lista[i+1] == "tk_string":
                return True
        return False 
resultado2 = varios_strings_consecutivos(mi_lista2)

if resultado2:
    print("La lista contiene varios strings consecutivos.")
else:
    print("La lista no contiene tres comillas consecutivas.")
    

def eliminar_elementos_vacios(lista):
    lista_sin_vacios = [elemento for elemento in lista if elemento.strip() != ""]
    return lista_sin_vacios

# Ejemplo de uso
mi_lista = ["", "Hola", "  ", "Mundo", "", "Python"]
mi_lista_sin_vacios = eliminar_elementos_vacios(mi_lista)

print(mi_lista_sin_vacios)



def eliminar_elementos_hasta_salto_de_linea(lista):
    while lista and lista[0] != "tk_salto_linea":
        lista.pop(0)  # Elimina el primer elemento de la lista

    if lista and lista[0] == "tk_salto_linea":
        lista.pop(0)  # Elimina la última instancia de "tk_salto_linea" si existe


# Ejemplo de uso
mi_lista = ["elemento1", "elemento2", "tk_salto_linea", "elemento3", "tk_salto_linea", "elemento4"]

print(mi_lista)
eliminar_elementos_hasta_salto_de_linea(mi_lista)

print(mi_lista)


def encontrar_corchetes(lista):
    for elemento in lista:
        if "[" in elemento or "]" in elemento:
            return True
    return False

# Ejemplo de uso
mi_lista = ["manzanas", "[", "uvas", "plátanos", "naranjas"]
corchetes = encontrar_corchetes(mi_lista)

if corchetes:
    print("Se encontraron corchetes.")
else:
    print("No se encontraron corchetes.")


def encontrar_llaves(lista):

    for elemento in lista:
        if "{" in elemento or "}" in elemento:
            return True
    return False

# Ejemplo de uso
mi_lista = ["manzanas","uvas", "plátanos", "sandías", "naranjas", "peras", "manzanas"]
llaves = encontrar_llaves(mi_lista)

if llaves:
    print("Se encontraron llaves.")
else:    
    print("No se encontraron llaves.")

tokens = []

tokens.append(tk(" ", "tk_espacio", 1, 5))
tokens.append(tk(" ", "tk_espacio", 1, 11))
tokens.append(tk(" ", "tk_espacio", 1, 12))
tokens.append(tk(" ", "tk_salto_linea", 1, 13))
tokens.append(tk("mundo", "tk_string", 1, 6))
tokens.append(tk("!", "tk_string", 1, 12))
tokens.append(tk(" ", "tk_espacio", 1, 13))

def eliminar_espacios():
    token = tokens[0]
    
    while tokens:
        if token.token not in ["tk_espacio", "tk_salto_linea"]:
            break  # Detener la eliminación cuando se encuentra una palabra diferente
        else:
            tokens.pop(0)
            token = tokens[0]

def eliminar_sinsalto():
    token = tokens[0]
    
    while tokens:
        if token.token not in ["tk_espacio"]:
            break  # Detener la eliminación cuando se encuentra una palabra diferente
        else:
            tokens.pop(0)
            token = tokens[0]

# Ejemplo de uso:
#mi_lista = ["tk_espacio", "tk_espacio", "tk_salto_linea", "otra_palabra", "tk_espacio", "final"]
#eliminar_elementos_iniciales(mi_lista)
#print(mi_lista)  # La lista resultante será ["otra_palabra", "tk_espacio", "final"]

eliminar_sinsalto()

for i in tokens:
    print(i.palabra, i.token, i.linea, i.col)
    
    
