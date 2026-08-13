# Laboratorio 4 - Teoría de la Computación

## Problema 1 - AFN con algoritmo de Thompson

Este programa construye un Autómata Finito No Determinista (AFN) a partir de una expresión regular utilizando el algoritmo de Thompson.

El programa lee las expresiones regulares desde un archivo de texto, construye el AFN correspondiente, genera una imagen del autómata y permite ingresar una cadena para comprobar si pertenece o no al lenguaje de la expresión regular.

## Expresiones regulares

El archivo `expresiones.txt` contiene las siguientes expresiones:

```text
(a*|b*)+
((E|a)|b*)*
(a|b)*abb(a|b)*
0?(1?)?0*
```

En el programa se utiliza `E` para representar epsilon (ε).

## Estructura del proyecto

```text
lab4/
│
├── grafos/
│   ├── afn_1.png
│   ├── afn_2.png
│   ├── afn_3.png
│   └── afn_4.png
│
├── afn.py
├── expresiones.txt
├── main.py
├── regex.py
├── thompson.py
└── README.md
```

## Archivos

- `main.py`: ejecuta el programa y lee las expresiones regulares.
- `regex.py`: procesa las expresiones regulares y las convierte a notación postfix.
- `thompson.py`: construye los AFN utilizando el algoritmo de Thompson.
- `afn.py`: contiene la representación del AFN, su simulación y la generación de los grafos.
- `expresiones.txt`: contiene las expresiones regulares utilizadas.
- `grafos/`: contiene las imágenes generadas de los AFN.

## Requisitos

El programa utiliza Python 3 y las siguientes librerías:

```text
matplotlib
networkx
```

Se pueden instalar con:

```bash
pip install matplotlib networkx
```

## Ejecución

Desde la carpeta del proyecto ejecutar:

```bash
python main.py
```

El programa mostrará la expresión regular procesada, su representación postfix y solicitará una cadena.

Ejemplo:

```text
Expresion 1: (a*|b*)+
Postfix: a*b*|+
Grafo guardado en: grafos\afn_1.png
Ingrese la cadena que desea probar: aaabbb
si
```

Si la cadena pertenece al lenguaje de la expresión regular se muestra `si`. En caso contrario se muestra `no`.

Para ingresar la cadena vacía se utiliza:

```text
E
```

## Grafos

Los AFN generados se guardan automáticamente en la carpeta `grafos` en formato PNG.

Cada grafo muestra:

- Estado inicial.
- Estados del AFN.
- Estado de aceptación.
- Transiciones.
- Transiciones epsilon representadas con `E`.

## Video

Video de demostración:

Pendiente de agregar enlace de YouTube.