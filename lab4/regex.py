def es_simbolo(c):
    return c not in {"|", "*", "+", "?", "(", ")", "."}


def agregar_concatenacion(regex):
    resultado = ""

    for i, actual in enumerate(regex):
        resultado += actual

        if i + 1 >= len(regex):
            continue

        siguiente = regex[i + 1]

        izquierda = es_simbolo(actual) or actual in {")", "*", "+", "?"}
        derecha = es_simbolo(siguiente) or siguiente == "("

        if izquierda and derecha:
            resultado += "."

    return resultado


def a_postfix(regex):
    regex = agregar_concatenacion(regex)

    prioridad = {
        "|": 1,
        ".": 2
    }

    salida = []
    pila = []

    for c in regex:
        if es_simbolo(c):
            salida.append(c)

        elif c == "(":
            pila.append(c)

        elif c == ")":
            while pila and pila[-1] != "(":
                salida.append(pila.pop())

            if not pila:
                raise ValueError("Parentesis incorrectos")

            pila.pop()

        elif c in {"*", "+", "?"}:
            salida.append(c)

        elif c in {"|", "."}:
            while (
                pila
                and pila[-1] != "("
                and prioridad.get(pila[-1], 0) >= prioridad[c]
            ):
                salida.append(pila.pop())

            pila.append(c)

        else:
            raise ValueError(f"Simbolo no reconocido: {c}")

    while pila:
        if pila[-1] == "(":
            raise ValueError("Parentesis incorrectos")

        salida.append(pila.pop())

    return "".join(salida)