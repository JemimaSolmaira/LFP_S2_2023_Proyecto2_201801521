# Laboratorio de lenguajes Formales y de programacion
## Proyecto1
### Segundo Semestre 2023
```js
Universidad San Carlos de Guatemala
Programador: Jemima Solmaira Chavajay Quieju
Carne: 201801521
Correo: jemimasolmaira2425@gmail.com
```
---
## Descripción del Proyecto
El siguiente proyecto consta del  desarrollo de un programa utilizando Python, su funcion principal es contabilizar registros de inventario, sin embargo los datos que ingresen al programa son analizados previamente, el programa incluye una herramienta diseñada para analizar y dividir un flujo de caracteres de entrada en unidades léxicas significativas, conocidas como tokens según las reglas gramaticales y las expresiones regulares definidas y de esa manera obtener los errores Lexicos y Sintacticos.


## Objetivos
* Objetivo General
    * Contabilizar registros de inventario que son ingresados por medio de un archivo de extension .bizdata 
* Objetivos Específicos
    * Implementar un analizador lexico para la lectura de datos de un archivo .bizdata
    * Implementar un AFD para el proceso de deteccion de tokens correctos e incorrectos
    * Implementar un analizador sintactico para la lectura de datos de un archivo .bizData
    * Implementar un arbol de derivacion para el proceso de deteccion de sintaxis incorrecto
    * Hacer uso de comandos para implementar instrucciones, para la obtencion de informacion

---
## Manual de Usuario

Al iniciar el programa se muestra la interfaz grafica, en donde tenemos dos listas desplegables donde podremos elegir la funcion que necesitamos realizar

![Interfaz](https://i.ibb.co/60Y10YW/Interfaz1.jpg)  

Para cargar un archivo seleccionamos la opcion Archivo para subir un archivo de texto en formato .bizdata

El texto izquierdo mostrara el contenido del texto ingresado

![TextoIngresado](https://i.ibb.co/z56W98t/interfaz2.jpg) 

En la opcion archivo, podemos elegir tambien la opcion de analizar el archivo, esta opcion analizara el texto letra por letra para distinguir los datos ingresados, y los comandos que el usuario necesita, ademas de encontrar errores en  caso de que exista, al finalizar mostrara los comandos solicitados en el area de texto derecho

![Analizar](https://i.ibb.co/cxb8hs0/interfaz3.jpg) 

El comando ExportarReporte que puede venir incluido dentro del texto puede realizar un reporte en formato html de todos los productos ingresados


![ProductosHTML](https://i.ibb.co/WfBmhzD/productos-tabla.jpg)

Para poder obtener el resto de reportes sobre el archivo de texto ingresado podemos elegir la opcion Reportes:

La primera opcion es realizar un reporte de todos los tokens obtenidos al momento de realizar el analisis del texto, en formato HTML:

![TokensHTML](https://i.ibb.co/yy266kz/tokens.jpg)  

La segunda opcion es realizar un reporte de erroes obtenidos al momento de analizar el archivo de texto

![Errores](https://i.ibb.co/zSqb76j/Errores-tabla.jpg)

Y la ultima opcion es obtener todo el analisis del texto en forma de arbol de derivacion el cual nos muestra el trayecto realizado para realizar el analisis sintactico del texto


![Arbol1](https://i.ibb.co/T4tPm4V/Arbol1.jpg) 


![Arbol2](https://i.ibb.co/hZB9Qf3/arbol2.jpg)

