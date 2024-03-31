# Implementación de métodos computacionales

Teoría de la computación: mates discretas, programación paralela y funcional.

Computación evolutiva, machine learning, AutoML. Estancias de investigación de 7mo, prgramas de becarios, etc con el profe.

CETEC Sur 5, CT536

## Sesión #1

53%, 47%: 12 quizzes (12%), 3 exámenes (15%), 8 tareas (20%).

Conjuntos: colección de elementos representado como enumeración o descripción con predicados

- $A=\{1,2,3,\ldots\}$

- $A=\{a\in \mathbb{N}|a<4\}$

Notación:

<img title="" src="assets/2024-02-13-14-12-50-image.png" alt="" data-align="center" width="626">

La inclusión se usa siempre con llaves a la izquierda ya que compara conjunto - conjunto. La pertenencia usa siempre la forma elemento - conjunto.

## Sesión #2

Producto cartesiano entre dos conjuntos es la multiplicación cartesiana entre dos conjuntos. Es decir, cada elemento de uno con cada elemento del otro.

Conjunto potencia: conjunto que contiene todos los subconjuntos de cierto conjuntos. Su tamaño se denota por $|P(A)|=2^{|A|}$.

Relaciones y funciones: una relación es un subconjunto dentro del producto cartesiano entre dos conjuntos. Por ejemplo, la relación $\le$ es una relación sobre $\mathbb{N}\times\mathbb{N}$, es decir, la relación entre el primer conjunto con el segundo. Se puede escribir como: $\le\subseteq\mathbb{N}^2$, ya que una relación es un subconjunto. 

Una función depende de que a toda $x$ existe una única $f(x)$, es decir, para todo elemento en el dominio existe un único valor para él en el codominio. Para una relación esto no es necesario, y por eso una relación no es lo mismo que una función.

Diagrama de Hasse: para mostrar todos los elementos en una relación, es decir, todas las tuplas en order con una flecha.

<img title="" src="data:image/png;base64,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" alt="MODELO MATRICIAL PARA LA CONSTRUCCIÓN DEL DIAGRAMA DE HASSE DE UN CONJUNTO  PARCIALMENTE ORDENADO Pedro Raúl Acosta De la Cruz" width="262" data-align="center">

Reflexividad: una relación es reflexiva si (y solo si) contiene para cada elemento en el conjunto por lo menos una tupla interior que sea reflexiva (que se contiene únicamente a sí mismo pero dos veces). Todos las tuplas conteniendo su mismo elemento varias veces es reflexiva, como $(1,1)$, ó $(2,2,2)$, etc. Se puede expresar como:

 $\exists(a,a)\in R, \forall\ a\in A$.

Transitividad: que todos los elementos tengan caminos con absolutamente todos los demás elementos (investigar más). Es que cada vez que existan 3 nodos encadenadas con 2 tuplas, entonces exista una tercera tupla "cerrando el ciclo".

Simetría: si todas las tuplas vistas al revés se encuentran en la relación.

## Sesión #3

Un alfabeto $\Sigma$ es un conjunto finito de símbolos. Por ejemplo, el alfabeto en español: $\Sigma_{español}=\{a,b,c,\ldots,ñ,\ldots,x,y,z\}$

La potencia de un alfabeto se define recursivamente a partir de sus anteriores potencias. El caso base es un alfabeto de tamaño 1, pues su único símbolo es su potencia. 

Las potencias son todas las combinaciones posibles de cierto $\Sigma$ de $n$ elementos (que es un número entero positivo  $n\in\mathbb{Z^+}$).

<img title="" src="assets/5cefd4846630e2b44b0fc3b6cf0ddcb1d28d6b59.JPG" alt="" width="427" data-align="center">

En la figura arriba en el último renglón, los números negros son $x$, que vienen de $\Sigma$ (1d arr), y los dos rojos son $y$, que vienen de $\Sigma^2$ (2d arr).

$\empty \ne \epsilon$, el conjunto vación no es lo mismo a la palabra vacía. $x\epsilon=x$, es como el elemento neutro de la multiplicación. Por eso es que $\Sigma^0={\epsilon}$.

Cuantos elementos hay en $\Sigma^{100}$?

Hay $|\Sigma^n|=|\Sigma|^n$

$\Sigma^+$ es el conjunto de todas las palabras de tamaño 1, unión el conjunto de todas las palabras de tamaño 2, unión el conjunto... de tamaño 3, unión... tamaño 4, y hasta $n$. Recordar que $n$ es la cantidad de símbolos.

$\Sigma^{*}$ es lo mismo pero desde el cero, es decir, también contiene el conjunto de palabra nula $\{\epsilon\}$.

Dos palabras $w_1$ y $w_2$ son iguales si para todo carácter contenido en una palabra la primera palabra $w_1$ está en la misma posición que en la segunda palabra $w_2$.

Una palabra es una concatenación de otras palabras contenidas en $\Sigma^{*}$. 

<img src="assets/2024-02-20-14-18-44-image.png" title="" alt="" data-align="center">

$x^{n+1}=xx^n$

## Sesión #4

Cuaderno

Un autómata finito determinista (DFA) es una quintupla. La definición formal es $M=(Q,\Sigma,\delta,q,F)$. Algoritmos definidos formalmente.

- $Q$: estado de la máquina

- $\Sigma$: alfabeto

- $\delta$: dado un estado y un símbolo del alfabeto, es una función que toma ambos y te dice a donde ir

- $q\in Q$: estado inicial

- $F\subseteq Q$: donde es viable que la maquina reconozca una palabra en el lenguaje

Siempre debemos tener n x m transiciones cuando tenemos n estados y m símbolos debido a $\delta=Q\times \Sigma\rightarrow Q$.

## Sesión #5

Un problema de diseñar un DFA para cierta condición de número de símbolos o alguna otra se puede resolver usando diversas cantidades de estados. Estos estados los define la persona para resolver el problema. Óptimamente la cantidad de estados debe ser la mínima y existen diversas maneras de minimizar los estados de una implementación.

## Sesión #6

A contrario de un DFA (que es deterministico), un NFA se refiere a cuando estando en un mismo estado podemos transitar hacia dos estados diferentes al mismo tiempo y por ello no es deterministico.

El no determinismo nos ayuda a evitar complicaciones en sistemas deterministas. Esto funciona porque se ejecutan múltiples caminos al mismo tiempo al definir dos rumbos distintos para una misma entrada, lo cuál divide en ramas a una transición.

Por ejemplo, leer todas las entradas para de un sistema.

Un NFA no se puede programar con un sistema común como Python.

En la concatenación de sistemas se deben de eliminar los estados de aceptación de los sistemas anteriores

**CHECAR PRESENTACIÓN PORQUE ESTO NO ES TODO**

## Sesión #7

Teorema para poder intercambiar de NFA a DFA

![[Pasted image 20240305133542.png]]

Los lenguajes regulares son reconocidos por lenguajes deterministas, que a su vez a otros no deterministas.

Se definen primero los estados dentro del diagrama. Estos estados 

En algún momento llegamos a nuestra tabla de $\delta$ para el nuevo DFA. 

Ver este video para entender:

https://www.youtube.com/watch?v=Y92dtMnarAU

## Sesión #8

Una expresión regular $R$ es la descripción del lenguaje.

Por ejemplo:

$L=L(M)=\{w|w\ \text{termina en}\ 00\}=\Sigma^{*}00$

Algunas identidades de las expresiones regulares:

$R\ \cup \emptyset=R$
$R\cdot\varepsilon=\varepsilon\cdot R=R$
$R\cup\varepsilon \ne R$
$R\odot\emptyset=R\emptyset=\emptyset$

Jerarquía de operaciones:

1. Estrella
2. Concatenación
3. Unión

Construcción de diagramas de transiciones a partir de expresiones regulares:

![[Pasted image 20240308143458.png]]

