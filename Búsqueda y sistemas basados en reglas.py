import heapq

# Definir el grafo del sistema de transporte masivo
class Grafo:
    def __init__(self):
        self.nodos = {}
    
    def agregar_nodo(self, nombre):
        """Agrega un nodo (punto de interés) al grafo."""
        self.nodos[nombre] = {}
    
    def agregar_arista(self, desde, hacia, peso, bidireccional=True):
        """Agrega una arista entre dos nodos con un peso específico.
        Si es bidireccional, se agrega la conexión en ambos sentidos."""
        self.nodos[desde][hacia] = peso
        if bidireccional:
            self.nodos[hacia][desde] = peso

# Algoritmo de Dijkstra para encontrar la ruta más corta
def dijkstra(grafo, inicio, fin):
    """Encuentra la ruta más corta desde el nodo 'inicio' hasta el nodo 'fin' usando el algoritmo de Dijkstra."""
    
    # Cola de prioridad para explorar los nodos en función de la distancia acumulada
    cola_prioridad = [(0, inicio)]
    # Diccionario para almacenar las distancias mínimas desde el nodo de inicio
    distancias = {nodo: float('inf') for nodo in grafo.nodos}
    distancias[inicio] = 0
    # Diccionario para reconstruir la ruta
    camino = {nodo: None for nodo in grafo.nodos}
    
    while cola_prioridad:
        (distancia_actual, nodo_actual) = heapq.heappop(cola_prioridad)
        
        # Si hemos llegado al destino, no es necesario seguir explorando
        if nodo_actual == fin:
            break
        
        # Explorar los vecinos del nodo actual
        for vecino, peso in grafo.nodos[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    # Reconstruir la ruta desde el destino hasta el origen
    ruta = []
    nodo = fin
    while nodo is not None:
        ruta.append(nodo)
        nodo = camino[nodo]
    ruta.reverse()
    
    return ruta, distancias[fin]

# Crear el grafo del sistema de transporte
grafo = Grafo()
# Agregar nodos (estaciones o puntos de interés)
nodos = ["A", "B", "C", "D", "E", "F"]
for nodo in nodos:
    grafo.agregar_nodo(nodo)

# Agregar aristas (conexiones entre nodos con distancias en kilómetros)
aristas = [
    ("A", "B", 4),
    ("B", "C", 7),
    ("A", "C", 5),
    ("C", "D", 5),
    ("B", "D", 2),
    ("D", "E", 1),
    ("C", "F", 3),  
    ("E", "F", 2)
]
for desde, hacia, peso in aristas:
    grafo.agregar_arista(desde, hacia, peso)

# Función para encontrar y mostrar la mejor ruta
def mostrar_mejor_ruta(grafo, inicio, fin):
    """Muestra la mejor ruta desde el nodo 'inicio' hasta el nodo 'fin'."""
    if inicio not in grafo.nodos or fin not in grafo.nodos:
        print(f"Uno o ambos nodos no existen en el grafo: {inicio}, {fin}")
        return
    
    ruta, distancia = dijkstra(grafo, inicio, fin)
    
    if distancia == float('inf'):
        print(f"No hay ruta disponible de {inicio} a {fin}.")
    else:
        print(f"La mejor ruta de {inicio} a {fin} es: {' -> '.join(ruta)} con una distancia de {distancia} km.")

# Encontrar y mostrar las mejores rutas entre algunos nodos
mostrar_mejor_ruta(grafo, "A", "D")
mostrar_mejor_ruta(grafo, "A", "E")
mostrar_mejor_ruta(grafo, "A", "F")
mostrar_mejor_ruta(grafo, "B", "F")