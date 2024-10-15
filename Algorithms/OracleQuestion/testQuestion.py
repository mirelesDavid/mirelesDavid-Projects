from itertools import combinations

def minArea(x, y, k):
    points = list(zip(x, y)) 
    n = len(points)
    
    # Si k es mayor o igual que el número de puntos, no necesitamos incluir ningún punto
    if k >= n:
        return 0
    
    # Si no se pueden excluir puntos, devolvemos el área del cuadrado que encierra todos los puntos
    if k == 0:
        min_x, max_x = min(x), max(x)
        min_y, max_y = min(y), max(y)
        return (max(max_x - min_x, max_y - min_y) + 2) ** 2
    
    min_area = float('inf')
    
    # Probar todas las combinaciones de n - k puntos
    for comb in combinations(points, n - k):
        xs = [p[0] for p in comb]
        ys = [p[1] for p in comb]
        
        # Calcular los límites del cuadrado para estos puntos
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        
        # Calcular el lado del cuadrado y su área
        side_length = max(max_x - min_x, max_y - min_y) + 2
        area = side_length ** 2
        
        # Mantener el área mínima encontrada
        min_area = min(min_area, area)
    
    return min_area

# Ejemplo de prueba
x = [2, 0]
y = [4, 0]
k = 0
print(minArea(x, y, k))

