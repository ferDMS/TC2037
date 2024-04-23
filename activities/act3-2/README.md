# Documentación de Lexer Aritmético

## Diagrama de Transiciones

![](diagram.png)

## Requisitos Previos

Para ejecutar este programa, se requiere lo siguiente:

Python 3.x: Debe estar instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python.
Pandas: Una biblioteca de Python utilizada para crear y manejar la tabla de transiciones del DFA de manera eficiente. Si aún no está instalada, puedes hacerlo ejecutando `pip install pandas` en tu terminal o línea de comandos.

## Instalación y Configuración

Asegúrate de que Python y Pandas estén correctamente instalados en tu sistema.
Coloca el archivo del programa main.py (o el nombre que le hayas dado) en un directorio de tu elección.

## Preparación del Archivo de Entrada

Crea un archivo de texto (por ejemplo, expresiones.txt) que contenga las expresiones aritméticas y comentarios que deseas analizar. Cada expresión o comentario debe estar en su propia línea.

## Ejecución del Programa

Navega al directorio donde guardaste el archivo del programa.
Abre un IDE donde puedas abrir el Jupyter Notebook, tal como Google Colab.

## Salida Esperada

El programa procesará cada línea del archivo de entrada, identificando los tokens y clasificándolos según su tipo (por ejemplo, variable, operador, entero, real, comentario).

Se mostrarán errores de sintaxis para las líneas que no cumplan con las reglas gramaticales esperadas por el DFA.
Finalmente, el programa generará una tabla de transiciones (DataFrame de Pandas) que muestra cómo el autómata cambia de estado con diferentes entradas. Esta tabla se visualiza en el notebook pero también puede ser exportada a un archivo CSV para ser analizada de manera más detallada.

## Lenguaje y Herramientas Utilizadas

Lenguaje de Programación: Python 3.x

Bibliotecas Externas: Pandas