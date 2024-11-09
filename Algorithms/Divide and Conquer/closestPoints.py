def calcularDistancia(punto1, punto2):
    # Retorna la distancia euclidiana entre punto1 y punto2
    return ((punto1.x - punto2.x)**2 + (punto1.y - punto2.y)**2)**0.5

def distanciaMinimaCasoBase(puntos):
    # Inicializa la distancia mínima como infinita
    minDist = float('inf')
    # Número de puntos en el conjunto
    # Recorre cada par de puntos y calcula la distancia entre ellos
            # Calcula la distancia entre los puntos i y j
            # Si la distancia es menor que la mínima actual, actualiza minDist
    # Retorna la distancia mínima encontrada
    return minDist

def distanciaMinimaEnZonaCentral(puntos, delta):
    # Inicializa la distancia mínima con el valor de delta
    minDist = delta
    # Número de puntos en la zona central
    # Recorre cada par de puntos en la zona central
            # Verifica si la diferencia en Y es menor que la distancia mínima actual
                # Calcula la distancia entre los puntos i y j
                # Si la distancia es menor que minDist, actualiza minDist
    # Retorna la distancia mínima encontrada en la zona central
    return minDist

# Algoritmo principal de divide y vencerás para encontrar la distancia mínima
def distanciaMinimaDivideYVenceras(puntos):
    # Si el número de puntos es menor o igual a 3, resuelve directamente usando el caso base
    if len(puntos) <= 3:
        return distanciaMinimaCasoBase(puntos)
    
    # Encuentra la mitad de la lista de puntos
    mitad = len(puntos) // 2
    # Divide los puntos en dos mitades: izquierda y derecha
    puntosIzquierda = puntos[:mitad]
    puntosDerecha = puntos[mitad:]

    distanciaIzquierda = distanciaMinimaDivideYVenceras(puntosIzquierda)
    distanciaDerecha = distanciaMinimaDivideYVenceras(puntosDerecha)

    # Encuentra el mínimo entre las distancias de ambas mitades
    delta = min(distanciaIzquierda, distanciaDerecha)

    # Encuentra los puntos en la región central que están dentro de la distancia delta
    puntosCentrales = [punto for punto in puntos if abs(punto.x - xMitad) < delta]

    # Calcula la distancia mínima en la región central
    distanciaCentral = distanciaMinimaEnZonaCentral(puntosCentrales, delta)

    # Retorna la distancia mínima global entre delta y distanciaCentral
    return min(delta, distanciaCentral)

# Función para preparar los puntos y ejecutar el algoritmo principal
def encontrarParMasCercano(puntos):
    # Ordena los puntos por su coordenada X antes de llamar al algoritmo de divide y vencerás
    puntos.sort(key=lambda punto: punto.x)
    # Llama al algoritmo de divide y vencerás y retorna la distancia mínima
    return distanciaMinimaDivideYVenceras(puntos)
