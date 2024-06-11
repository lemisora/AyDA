import time
import numpy as np
import matplotlib.pyplot as plt

# Algoritmo de inserción
def insertion_sort(A):
    """
    Implementa el algoritmo de ordenamiento por inserción.
    :param A: Lista de números enteros a ordenar.
    """
    for j in range(1, len(A)):
        aux = A[j]
        i = j - 1
        while i >= 0 and A[i] > aux:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = aux

# Función para generar los arreglos
def generar_arreglo(n, caso='promedio'):
    """
    Genera un arreglo de enteros basado en el caso especificado.
    :param n: Tamaño del arreglo.
    :param caso: Tipo de caso ('mejor', 'peor', 'promedio').
    :return: Lista de enteros generada.
    """
    if caso == 'mejor':
        return list(range(n))
    elif caso == 'peor':
        return list(range(n, 0, -1))
    elif caso == 'promedio':
        return list(np.random.randint(1, n + 1, size=n))

# Medición de tiempos
def medir_tiempos(casos, tamaños):
    """
    Mide el tiempo de ejecución del algoritmo de inserción para diferentes tamaños de arreglos y casos.
    :param casos: Lista de casos ('mejor', 'peor', 'promedio').
    :param tamaños: Lista de tamaños de arreglos a probar.
    :return: Diccionario con los tiempos de ejecución para cada caso.
    """
    tiempos = {'mejor': [], 'peor': [], 'promedio': []}
    
    for tamaño in tamaños:
        for caso in casos:
            arreglo = generar_arreglo(tamaño, caso)
            inicio = time.time()
            insertion_sort(arreglo)
            fin = time.time()
            tiempos[caso].append(fin - inicio)
    
    return tiempos

# Configuración de casos y tamaños
casos = ['mejor', 'peor', 'promedio']
tamaños = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Medir tiempos
tiempos = medir_tiempos(casos, tamaños)

# Graficar los resultados
plt.figure(figsize=(10, 6))
for caso in casos:
    plt.plot(tamaños, tiempos[caso], marker='o', label=f'Caso {caso}')

plt.xlabel('Cantidad de datos')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución del algoritmo de inserción')
plt.xticks(tamaños)  # Asegura que se muestren todas las iteraciones en el eje x
plt.legend()
plt.grid(True)
plt.show()
