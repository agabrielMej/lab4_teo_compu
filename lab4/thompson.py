from collections import defaultdict

from afn import AFN, Estado, agregar_transicion


def combinar_transiciones(*listas):
    resultado = defaultdict(list)

    for transiciones in listas:
        for clave, destinos in transiciones.items():
            resultado[clave].extend(destinos)

    return resultado


def construir_afn(postfix):
    pila = []

    for token in postfix:

        if token not in {"|", ".", "*", "+", "?"}:
            inicio = Estado()
            fin = Estado()

            transiciones = defaultdict(list)
            agregar_transicion(
                transiciones,
                inicio,
                token,
                fin
            )

            pila.append(
                AFN(inicio, fin, transiciones)
            )

        elif token == ".":
            if len(pila) < 2:
                raise ValueError("Expresion postfix invalida")

            segundo = pila.pop()
            primero = pila.pop()

            transiciones = combinar_transiciones(
                primero.transiciones,
                segundo.transiciones
            )

            agregar_transicion(
                transiciones,
                primero.aceptacion,
                "E",
                segundo.inicio
            )

            pila.append(
                AFN(
                    primero.inicio,
                    segundo.aceptacion,
                    transiciones
                )
            )

        elif token == "|":
            if len(pila) < 2:
                raise ValueError("Expresion postfix invalida")

            segundo = pila.pop()
            primero = pila.pop()

            inicio = Estado()
            fin = Estado()

            transiciones = combinar_transiciones(
                primero.transiciones,
                segundo.transiciones
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                primero.inicio
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                segundo.inicio
            )

            agregar_transicion(
                transiciones,
                primero.aceptacion,
                "E",
                fin
            )

            agregar_transicion(
                transiciones,
                segundo.aceptacion,
                "E",
                fin
            )

            pila.append(
                AFN(inicio, fin, transiciones)
            )

        elif token == "*":
            if not pila:
                raise ValueError("Expresion postfix invalida")

            afn = pila.pop()

            inicio = Estado()
            fin = Estado()

            transiciones = combinar_transiciones(
                afn.transiciones
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                afn.inicio
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                fin
            )

            agregar_transicion(
                transiciones,
                afn.aceptacion,
                "E",
                afn.inicio
            )

            agregar_transicion(
                transiciones,
                afn.aceptacion,
                "E",
                fin
            )

            pila.append(
                AFN(inicio, fin, transiciones)
            )

        elif token == "+":
            if not pila:
                raise ValueError("Expresion postfix invalida")

            afn = pila.pop()

            inicio = Estado()
            fin = Estado()

            transiciones = combinar_transiciones(
                afn.transiciones
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                afn.inicio
            )

            agregar_transicion(
                transiciones,
                afn.aceptacion,
                "E",
                afn.inicio
            )

            agregar_transicion(
                transiciones,
                afn.aceptacion,
                "E",
                fin
            )

            pila.append(
                AFN(inicio, fin, transiciones)
            )

        elif token == "?":
            if not pila:
                raise ValueError("Expresion postfix invalida")

            afn = pila.pop()

            inicio = Estado()
            fin = Estado()

            transiciones = combinar_transiciones(
                afn.transiciones
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                afn.inicio
            )

            agregar_transicion(
                transiciones,
                inicio,
                "E",
                fin
            )

            agregar_transicion(
                transiciones,
                afn.aceptacion,
                "E",
                fin
            )

            pila.append(
                AFN(inicio, fin, transiciones)
            )

    if len(pila) != 1:
        raise ValueError("No se pudo construir el AFN")

    return pila.pop()