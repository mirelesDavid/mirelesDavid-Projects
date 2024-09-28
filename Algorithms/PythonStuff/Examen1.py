def maxMin(nums, low, high):
    if low == high:
        return [nums[low], nums[low]]
    
    mid = (low + high) // 2
    min1, max1 = maxMin(nums, low, mid)
    min2, max2 = maxMin(nums, mid + 1, high)
    
    bestMax = max(max1, max2)
    bestMin = min(min1, min2)
    
    
    return (bestMin, bestMax)



nums = [3,6,8,43,1]
print(maxMin(nums, 0, len(nums) - 1))


# Clase para representar una actividad con su tiempo de inicio y finalización
class Actividad:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

def seleccion_actividades(actividades):
    # Ordenar actividades por tiempo de finalización en orden descendente (última actividad en comenzar)
    actividades_ordenadas = sorted(actividades, key=lambda x: x.fin, reverse=True)

    # La primera actividad seleccionada será la que termina más tarde (última en comenzar)
    seleccionadas = [actividades_ordenadas[0]]

    # Procesar el resto de las actividades
    for i in range(1, len(actividades_ordenadas)):
        # Si la actividad actual no se solapa con la última actividad seleccionada
        if actividades_ordenadas[i].fin <= seleccionadas[-1].inicio:
            seleccionadas.append(actividades_ordenadas[i])

    # Devolver las actividades seleccionadas
    return seleccionadas

# Lista de actividades con tiempos de inicio y finalización
actividades = [
    Actividad(1, 4),
    Actividad(3, 5),
    Actividad(0, 6),
    Actividad(5, 7),
    Actividad(3, 9),
    Actividad(5, 9),
    Actividad(6, 10),
    Actividad(8, 11),
    Actividad(8, 12),
    Actividad(2, 14),
    Actividad(12, 16)
]

actividades_seleccionadas = seleccion_actividades(actividades)

print("Actividades seleccionadas:")
for actividad in actividades_seleccionadas:
    print(f"Inicio: {actividad.inicio}, Fin: {actividad.fin}")
