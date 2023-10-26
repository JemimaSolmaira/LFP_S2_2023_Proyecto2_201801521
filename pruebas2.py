def formatear_lista_datos(lista):
    # Encabezados de columnas
    encabezados = ["Columna 1", "Columna 2", "Columna 3", "Columna 4", "Columna 5"]
    
    # Encabezados formateados
    encabezados_formateados = [encabezado.ljust(15) for encabezado in encabezados]
    
    # Crear la línea de separación
    separador = '-' * (15 * 5)
    
    # Inicializar el resultado con los encabezados y el separador
    resultado = ' '.join(encabezados_formateados) + '\n' + separador + '\n'
    
    # Formatear los datos y agregarlos al resultado
    for fila in lista:
        fila_formateada = [str(dato).ljust(15) for dato in fila]
        resultado += ' '.join(fila_formateada) + '\n'
    
    return resultado

# Ejemplo de uso:
datos = [
    [1, 'A', 10.5, 'Texto largo', True],
    [2, 'B', 20.3, 'Otro texto', False],
]

resultado_formateado = formatear_lista_datos(datos)
print(resultado_formateado)
