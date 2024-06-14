import numpy as np
#
import matplotlib.pyplot as plt

# Devuelve una lista de enteros de tamaño n en orden ascendente
def bestA(n):
    return list(range(n))	#Devuelve un objeto de tipo list con número ordenados ascendentemente

# Devuelve una lista de enteros de tamaño n en orden descendente
def worstA(n):
    return list(range(n, 0, -1))	#Devuelve una lista con números ordenados descendentemente

# Devuelve una lista de enteros (generados y ordenados aleatoriamente) de tamaño n
def randomA(n):
    return list(np.random.randint(1, 1001, size=n))	#Devuelve una lista de números aleatorios

# Ordena una lista y cuenta el número de operaciones relevantes (intercambios)
def insertionSort(lista):
    n = len(lista)
    contOperaciones = 0
    for j in range(1, n):  # Empezamos a evaluar desde el segundo dato de la lista
        aux = lista[j]  # Se asigna el valor del elemento de la lista que está siendo evaluado a la variable aux
        contOperaciones += 1  # Contamos las operaciones relevantes, en este caso es el cambio de índice
        i = j - 1  # Índice del elemento anterior al elemento de la lista que está siendo evaluado
        while i >= 0 and aux < lista[i]:
            lista[i + 1] = lista[i]
            contOperaciones += 1  # Contamos las operaciones relevantes, en este caso son las asignaciones
            i -= 1
        lista[i + 1] = aux
        contOperaciones += 1  # Contamos las operaciones relevantes, en este caso son las asignaciones
    return contOperaciones

# Tamaños de arreglos
tamaños = list(range(10, 110, 10))	#Devuelve una lista equivalente a [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#tamaños = list[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Inicialización de matrices para almacenar el número de operaciones
tiempoEjecucionesMejor = np.zeros((10, 10))
tiempoEjecucionesPeor = np.zeros((10, 10))
tiempoNumAleatorios = np.zeros((10, 10))

# Ejecutar los casos y medir operaciones
for i, n in enumerate(tamaños):
    for j in range(10):
        # Mejor caso
        A = bestA(n)
        tiempoEjecucionesMejor[i, j] = insertionSort(A) #Se añade la cantidad de operaciones al arreglo para tiempo de ejecuciones de mejor caso
        
        # Peor caso
        A = worstA(n)
        tiempoEjecucionesPeor[i, j] = insertionSort(A)	#Se añade la cantidad de operaciones al arreglo para tiempo de ejecuciones de peor caso
        
        # Números aleatorios
        A = randomA(n)
        tiempoNumAleatorios[i, j] = insertionSort(A)	#Se añade la cantidad de operaciones al arreglo para números aleatorios

# # Convertir resultados a DataFrame
# df_mejor = pd.DataFrame(tiempoEjecucionesMejor, columns=[f'Ejecución {i+1}' for i in range(10)], index=tamaños)
# df_mejor.index.name = 'Tamaño'
# df_mejor.columns.name = 'Mejor Caso'

# df_peor = pd.DataFrame(tiempoEjecucionesPeor, columns=[f'Ejecución {i+1}' for i in range(10)], index=tamaños)
# df_peor.index.name = 'Tamaño'
# df_peor.columns.name = 'Peor Caso'

# df_promedio = pd.DataFrame(tiempoNumAleatorios, columns=[f'Ejecución {i+1}' for i in range(10)], index=tamaños)
# df_promedio.index.name = 'Tamaño'
# df_promedio.columns.name = 'Caso Promedio'

# # Guardar DataFrames a un archivo de Excel
# with pd.ExcelWriter('resultados_insertion_sort.xlsx') as writer:
#     df_mejor.to_excel(writer, sheet_name='Mejor Caso')
#     df_peor.to_excel(writer, sheet_name='Peor Caso')
#     df_promedio.to_excel(writer, sheet_name='Caso Promedio')

# Graficar resultados
plt.figure(figsize=(12, 8))

# Mejor caso
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesMejor[:, j], marker='o', linestyle='-', label=f'Mejor caso - Ejecución {j+1}' if j == 0 else "")

# Peor caso
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesPeor[:, j], marker='x', linestyle='--', label=f'Peor caso - Ejecución {j+1}' if j == 0 else "")

# Caso promedio
for j in range(10):
    plt.plot(tamaños, tiempoNumAleatorios[:, j], marker='s', linestyle=':', label=f'Números aleatorios - Ejecución {j+1}' if j == 0 else "")

plt.xlabel('Cantidad de datos')
plt.ylabel('Cantidad de instrucciones ejecutadas')
plt.title('Número de operaciones del algoritmo de Insertion Sort')
plt.xticks(tamaños)
plt.legend()
plt.grid(True)
plt.show()
