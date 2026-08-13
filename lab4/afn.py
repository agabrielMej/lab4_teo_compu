from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx


class Estado:
    contador = 0

    def __init__(self):
        self.id = Estado.contador
        Estado.contador += 1


class AFN:
    def __init__(self, inicio, aceptacion, transiciones):
        self.inicio = inicio
        self.aceptacion = aceptacion
        self.transiciones = transiciones

    def cerradura_epsilon(self, estados):
        pila = list(estados)
        cerradura = set(estados)

        while pila:
            estado = pila.pop()

            for siguiente in self.transiciones.get(
                (estado.id, "E"), [] #cambie la letra ε por E ya que se me compluca el buscarl el simbolo
            ):
                if siguiente not in cerradura:
                    cerradura.add(siguiente)
                    pila.append(siguiente)

        return cerradura

    def mover(self, estados, simbolo):
        resultado = set()

        for estado in estados:
            for siguiente in self.transiciones.get(
                (estado.id, simbolo), []
            ):
                resultado.add(siguiente)

        return resultado

    def acepta(self, cadena):
        actuales = self.cerradura_epsilon(
            {self.inicio}
        )

        for simbolo in cadena:
            actuales = self.mover(
                actuales,
                simbolo
            )

            actuales = self.cerradura_epsilon(
                actuales
            )

        return self.aceptacion in actuales

    def obtener_estados(self):
        estados = {
            self.inicio.id: self.inicio,
            self.aceptacion.id: self.aceptacion
        }

        for (origen, _), destinos in self.transiciones.items():
            if origen not in estados:
                estados[origen] = None

            for destino in destinos:
                estados[destino.id] = destino

        return estados

    def dibujar(self, nombre):
        grafo = nx.DiGraph()

        estados = self.obtener_estados()

        for estado_id in estados:
            grafo.add_node(estado_id)

        etiquetas = {}

        for (origen, simbolo), destinos in self.transiciones.items():
            for destino in destinos:
                clave = (origen, destino.id)

                if clave not in etiquetas:
                    etiquetas[clave] = []

                etiquetas[clave].append(simbolo)
                grafo.add_edge(origen, destino.id)

        distancias = {
            self.inicio.id: 0
        }

        cola = [self.inicio.id]

        while cola:
            actual = cola.pop(0)

            for vecino in grafo.successors(actual):
                if vecino not in distancias:
                    distancias[vecino] = (
                        distancias[actual] + 1
                    )
                    cola.append(vecino)

        max_distancia = max(
            distancias.values(),
            default=0
        )

        for estado in grafo.nodes():
            if estado not in distancias:
                max_distancia += 1
                distancias[estado] = max_distancia

        columnas = {}

        for estado, distancia in distancias.items():
            if distancia not in columnas:
                columnas[distancia] = []

            columnas[distancia].append(estado)

        pos = {}

        separacion_x = 3.0
        separacion_y = 2.0

        for columna in sorted(columnas):
            lista = columnas[columna]
            cantidad = len(lista)

            centro = (cantidad - 1) / 2

            for i, estado in enumerate(lista):
                x = columna * separacion_x
                y = (centro - i) * separacion_y

                pos[estado] = (x, y)

        cantidad_columnas = len(columnas)

        ancho = max(
            12,
            cantidad_columnas * 2.5
        )

        alto = max(
            6,
            max(
                len(lista)
                for lista in columnas.values()
            ) * 2
        )

        plt.figure(
            figsize=(ancho, alto)
        )

        estados_normales = [
            estado
            for estado in grafo.nodes()
            if estado != self.aceptacion.id
        ]

        nx.draw_networkx_nodes(
            grafo,
            pos,
            nodelist=estados_normales,
            node_size=1400,
            edgecolors="black",
            linewidths=1.5
        )


        nx.draw_networkx_nodes(
            grafo,
            pos,
            nodelist=[self.aceptacion.id],
            node_size=1750,
            edgecolors="black",
            linewidths=1.5
        )

        nx.draw_networkx_nodes(
            grafo,
            pos,
            nodelist=[self.aceptacion.id],
            node_size=1400,
            edgecolors="black",
            linewidths=1.5
        )


        nombres = {
            estado: f"q{estado}"
            for estado in grafo.nodes()
        }

        nx.draw_networkx_labels(
            grafo,
            pos,
            labels=nombres,
            font_size=10
        )


        nx.draw_networkx_edges(
            grafo,
            pos,
            arrows=True,
            arrowsize=20,
            node_size=1400,
            width=1.2,
            connectionstyle="arc3,rad=0.08"
        )

        etiquetas_dibujo = {}

        for clave, simbolos in etiquetas.items():
            etiquetas_dibujo[clave] = ",".join(
                simbolos
            )

        nx.draw_networkx_edge_labels(
            grafo,
            pos,
            edge_labels=etiquetas_dibujo,
            font_size=9,
            rotate=False
        )

        x_inicio, y_inicio = pos[
            self.inicio.id
        ]

        plt.annotate(
            "",
            xy=(
                x_inicio - 0.15,
                y_inicio
            ),
            xytext=(
                x_inicio - 1.5,
                y_inicio
            ),
            arrowprops=dict(
                arrowstyle="->",
                linewidth=1.5
            )
        )

        plt.text(
            x_inicio - 1.7,
            y_inicio,
            "inicio",
            horizontalalignment="right",
            verticalalignment="center"
        )

        x_fin, y_fin = pos[
            self.aceptacion.id
        ]

        plt.text(
            x_fin,
            y_fin - 1,
            "aceptacion",
            horizontalalignment="center"
        )

        plt.title("AFN - Thompson")

        plt.axis("off")

        plt.tight_layout()

        plt.savefig(
            nombre + ".png",
            dpi=200,
            bbox_inches="tight"
        )

        plt.close()


def agregar_transicion(
    transiciones,
    origen,
    simbolo,
    destino
):
    transiciones[
        (origen.id, simbolo)
    ].append(destino)


def nuevas_transiciones():
    return defaultdict(list)