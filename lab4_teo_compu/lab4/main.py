import os

from afn import Estado
from regex import a_postfix
from thompson import construir_afn


def leer_expresiones(archivo):
    expresiones = []

    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip().replace(" ", "")

            if linea:
                expresiones.append(linea)

    return expresiones


def main():
    os.makedirs("grafos", exist_ok=True)

    expresiones = leer_expresiones("expresiones.txt")

    for numero, expresion in enumerate(expresiones, start=1):
        print("=" * 50)
        print(f"Expresion {numero}: {expresion}")

        try:
            Estado.contador = 0

            postfix = a_postfix(expresion)

            print(f"Postfix: {postfix}")

            afn = construir_afn(postfix)

            ruta = os.path.join(
                "grafos",
                f"afn_{numero}"
            )

            afn.dibujar(ruta)

            print(
                f"Grafo guardado en: "
                f"grafos\\afn_{numero}.png"
            )

            cadena = input(
                "Ingrese la cadena que desea probar: "
            )

            if cadena in {"E"}:
                cadena = ""

            if afn.acepta(cadena):
                print("si")
            else:
                print("no")

        except ValueError as error:
            print(f"Error: {error}")

        print()

    print("=" * 50)
    print("Programa terminado.")


if __name__ == "__main__":
    main()