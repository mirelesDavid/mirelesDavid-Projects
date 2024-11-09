import random
import sys

def generar_puntos_aleatorios(n, rango):
    puntos = []
    for _ in range(n):
        x = random.uniform(rango[0], rango[1])
        y = random.uniform(rango[0], rango[1])
        puntos.append((x, y))
    return puntos

def guardar_puntos_en_txt(puntos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for punto in puntos:
            archivo.write(f"{punto[0]},{punto[1]}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error! python generator.py numero_puntos")
        exit(-1)
    numero_de_puntos = int(sys.argv[1])  
    rango = (0, 10)  
    nombre_archivo = "points.txt"

    puntos = generar_puntos_aleatorios(numero_de_puntos, rango)
    guardar_puntos_en_txt(puntos, nombre_archivo)
    print(f"{numero_de_puntos} puntos aleatorios generados y guardados en {nombre_archivo}.")

