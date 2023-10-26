import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from parserL import parserL as par
from datos import scanner as sc

from obtener_informacion import informacion
from archivos_salida import salida
from graphiz import Grafica


# Función para cargar un archivo
texto = ""
palabras_clave = []
grupo_registros = []
arbol = []
errores = []
imprimir_consola = []
tokens = []


def cargar_archivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        with open(archivo, 'r') as file:
            global texto 
            texto = file.read()
            texto_area_editable.delete(1.0, tk.END)  # Borrar el contenido actual del área de texto editable
            texto_area_editable.insert(tk.END, texto)
    
    analizar_texto()

def analizar_texto():
    global texto
    global tokens
    scan = sc()
    scan.lectura(texto)
    scan.encontrar_errores()
    tokens = scan.hacer_copy()
    parser = par(scan.tokens, scan.errores)
    consola = parser.exportar_datos()
    global palabras_clave
    global grupo_registros
    global arbol
    global errores
    global imprimir_consola
    palabras_clave = parser.palabras_clave
    grupo_registros = parser.datos_registros
    arbol = parser.arbol_derivacion
    errores = parser.errores
    imprimir_consola = consola
    
    print(len(tokens))


def analizar_archivo():

    global texto
    if texto == "":
        resultado = "No hay archivo cargado."
        texto_area_no_editable.delete(1.0, tk.END)
        texto_area_no_editable.insert(tk.END, resultado)
    else:
        inf = informacion(palabras_clave, grupo_registros)
        resultados = inf.analizar(imprimir_consola)
        
        for i in resultados:
            resultado = str(i)
            texto_area_no_editable.insert(tk.END, resultado)



def reporte_tokens():
    global tokens
    tok = tokens
    s = salida("tokens")

    s.tokens("tokens", tok)
    
    messagebox.showinfo("Reporte", "Reporte de tokens generado con exito")

def reporte_errores():
    global errores
    s = salida("errores")
    s.errores("errores", errores)
    messagebox.showinfo("Reporte", "Reporte de errores generado con exito")
    
def arbol_derivacion():
    
    global arbol, grupo_registros, palabras_clave
    clave = len(palabras_clave)
    reg = len(grupo_registros)
    
    g = Grafica("arbol")
    texto = g.stringGeneral(arbol, clave, reg)
    g.crearArchivo(texto)
    g.ConvertirArchivo()
    
    messagebox.showinfo("Reporte", "Reporte de arbol de derivacion generado con exito")

# ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de Análisis")

# Menú principal
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Menú Archivo
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Cargar archivo", command=cargar_archivo)
menu_archivo.add_command(label="Analizar archivo", command=analizar_archivo)

# Menú Reportes
menu_reportes = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Reportes", menu=menu_reportes)
menu_reportes.add_command(label="Reporte de Tokens", command=reporte_tokens)
menu_reportes.add_command(label="Reporte de Errores", command=reporte_errores)
menu_reportes.add_command(label="Árbol de Derivación", command=arbol_derivacion)

# Área de texto editable
texto_area_editable = tk.Text(ventana, wrap=tk.WORD,  width=70, height=40)
texto_area_editable.pack(side=tk.LEFT)

# Área de texto no editable
texto_area_no_editable = tk.Text(ventana, wrap=tk.WORD,  width=90, height=40)
texto_area_no_editable.pack(side=tk.RIGHT)
#texto_area_no_editable.configure(state="disabled")  # Hacer que el área de texto no sea editable

# Iniciar la aplicación
ventana.mainloop()
