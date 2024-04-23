import csv
import random

# Crear y escribir datos en un archivo CSV
with open('datos_ejemplo.csv', 'w', newline='') as csvfile:
    fieldnames = ['CO2', 'GasesToxicos', 'Resultado']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Escribir encabezados
    writer.writeheader()

    # Generar datos aleatorios
    for _ in range(100):
        co2 = random.randint(0, 1024)
        gases_toxicos = random.randint(0, 14)
        
        # Determinar el resultado según los criterios
        resultado = 1 if co2 > 500 or gases_toxicos > 9 else 0

        # Escribir fila en el archivo CSV
        writer.writerow({'CO2': co2, 'GasesToxicos': gases_toxicos, 'Resultado': resultado})

print("Archivo CSV generado con éxito: datos_ejemplo.csv")
