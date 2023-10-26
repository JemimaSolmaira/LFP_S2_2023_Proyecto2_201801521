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
## Manual Tecnico

El archivo interfaz.py contiene todo el desarrollo de la interfaz grafica , el cual es realizada en con la libreria tkinder consta de 2 menus desplegables con las funciones para manejar el archivo.

![Tkinder](https://i.ibb.co/60Y10YW/Interfaz1.jpg)

en el menu desplegable de Archivo tenemos las funciones que se usan para las opciones de cargar un archivo, asi como analizar el archivo.

El archivo debe ser un texto de formato .bizData, el archivo de texto debe venir con los datos que necesitaremos para realizar el analisis de inventario, el archivo puede contener comentarios, los cuales deberan venir inicialmente con el simbolo numeral, o con tres comillas de inicio y cierre, las claves deben ser simbolizadas con la palabra reservada "Claves" seguido del simbolo igual, y dentro de corchetes toda la informacion sobre las claves, para los registros se debera iniciar con la palabra reservada "Registros" seguido del simbolo igual, dentro de los corchetes se debe agregar cada registro dentro de llaves:

![MenuDesplegable](https://i.ibb.co/N6VPdLW/dats.jpg)

dentro del documento asi mismo pueden venir comandos especificos que realicen diferentes acciones, tales como realizar un promedio, o una suma de algun parametro en especifico

![Funciones Principales](https://i.ibb.co/vD8pj7Y/datos.jpg)

La principal funcion del programa es el analizador pues su funcion es leer el archivo de texto letra por letra aplicando un analizador lexico y sintactico:

Primeramente se realiza un analisis lexico, obteniendo todos los tokens dentro del documento de texto

* Gramatica Scanner

La gramatica permitida es la que se presenta en el siguiente cuadro: 

![Gramatica](https://i.ibb.co/rkZg5XT/lexico.jpg)

Para realizar este proceso se utiliza la clase Scanner, en donde encontramos todas las funciones que nos permiten dividir los tokens dependiendo de sus patrones de texto, cual token que no se incluya dentro de nuestra gramatica sera considerado un error e incluido en la tabla de errores


El analisis se realiza letra por letra , las palabras se comparan con los patrones permitidos, en caso de encontrar alguna letra que no sea permitida se eliminara del formato inicial.

al finalizar este proceso, se iniciara con el analisis sintactico, el cual esta incluida en la clase ParserL, se analizara el orden de los tokens y si esta en el orden correcto, para ello se utiliza una gramatica tipo 2, una gramatica libre de contexto

* Gramatica Parser

![gramaticatipo2](https://i.ibb.co/m56TYP6/sintactico1.jpg)

![gramaticatipo2.0](https://i.ibb.co/gz8QGTS/sintactico2.jpg)

En caso de existir algun orden que no se encuentre en la gramatica , sera reportado como error sintactico a la tabla de erorres

La lectura del texto permite generar un arbol de derivacion el cual nos muestra el recorrido que ha realizado el analisis sintactico por la gramatica tipo 2 planteada anteriormente,

![Arbol](https://i.ibb.co/hZB9Qf3/arbol2.jpg) 


