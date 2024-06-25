# INFORME DE COBERTURA HTML

File	        statements	missing	excluded	coverage
test_Tarea.py	26	            2	    0	        92%
Total	        26	            2	    0	        92%

# ---Este es el informe de cobertura dada por la libreria coverage pero en formato html---
# lo primero que dice en la pagina es "Coverage report: 92%" significa que el porcentaje de codigo cubierto fue del 92%
# hay 3 opciones a elegir, files, functions, classes, files representa los archivos cubiertos por el reporte, functions son todas las funciones que se encuentran en dichos archivos, junto con ello las funciones se clasifican por file, function, statements, missing, excluded y coverage,  y por ultimo classes, son las clases que se encuentran en dichos archivos, junto con ello las funciones se clasifican por file, classes, statements, missing, excluded y coverage.
# abajo del todo nos da informacion como el nombre de la libreria, la version, la fecha y la hora de creacion.
# como funciones extra, a la derecha nos da la oportunidad de buscar por medio de los filtros, una casilla para elegir si quiero o no mostrar los archivos cubiertos y por ultimo el icono del teclado nos muestra atajos del teclado para manejar la pagina con mayor facilidad.
# Al seleccionar un archivo, vemos el codigo completo y por medio de colores nos indica que codigo se ejecuto y cual no, en mi caso, se ejecuto todo menos la linea 9, ya que no tengo una division por cero en mis pruebas, y la linea 35 que bueno, normalmente nunca se ejecuta porque solamente se encarga de que el archivo al que se le hacen las pruebas sea el correcto.
# Se puede concluir que gracias a este informe de cobertura por html hasta una persona con conocimientos basicos o hasta nulos sobre la programación, podria entender medianamente lo que esta sucediendo.