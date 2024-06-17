import numpy as np
import matplotlib.pyplot as plt
import random

# # Función para generar el mejor caso
# def mejor_caso(n):
#     c = [i * 2 for i in range(n)]
#     f = [i * 2 + 1 for i in range(n)]
#     return c, f

# # Función para generar el peor caso
# def peor_caso(n):
#     c = [0 for _ in range(n)]
#     f = [i + 1 for i in range(n)]
#     return c, f

# Función para generar c y f con precondiciones para un caso más común
def generar_arreglos_aleatorios(n):
    c = sorted(random.randint(0, n) for _ in range(n))
    f = [ci + random.randint(1, 5) for ci in c]
    return c, sorted(f)

# Función selec que devuelve un conjunto y cuenta los pasos (algoritmo voraz)
def selec_voraz(c, f, n):
    global conteoPasos
    conteoPasos = 0
    A = {1}  # Conjunto A inicializado con la primera actividad
    j = 0    # j es el índice de la última actividad seleccionada

    for i in range(1, n):
        conteoPasos += 1
        if c[i] >= f[j]:
            A.add(i + 1)
            j = i
            conteoPasos += 1

    return A

# Función para seleccionar actividades usando programación dinámica y contar pasos
def seleccion_actividades_dp(c, f):
    n = len(c)
    actividades = [(c[i], f[i], i+1) for i in range(n)]
    actividades.sort(key=lambda x: x[1])  # Ordenar por tiempo de finalización

    DP = [0] * (n + 1)
    DP[1] = 1

    def actividad_anterior_compat(actividad_actual):
        for k in range(actividad_actual - 1, -1, -1):
            if actividades[k][1] <= actividades[actividad_actual][0]:
                return k + 1
        return 0

    global conteoPasosDP
    conteoPasosDP = 0

    for j in range(2, n + 1):
        conteoPasosDP += 1
        incluir_actividad = 1 + DP[actividad_anterior_compat(j - 1)]
        DP[j] = max(DP[j - 1], incluir_actividad)
        conteoPasosDP += 1

    conjunto_actividades = set()
    j = n
    while j > 0:
        if DP[j] != DP[j - 1]:
            conjunto_actividades.add(actividades[j - 1][2])
            j = actividad_anterior_compat(j - 1)
        else:
            j -= 1

    return conjunto_actividades

# Definir tamaños de los arreglos
tamaños = list(range(10, 110, 10))

# Inicializar arreglos para almacenar los tiempos de ejecución
tiempoEjecucionesVoraz = np.zeros((10, 10))
tiempoEjecucionesDP = np.zeros((10, 10))

# Evaluar para los diferentes tamaños
for idx, n in enumerate(tamaños):
    for run in range(10):  # Realizar 10 ejecuciones para cada tamaño
        # Algoritmo voraz
        c, f = generar_arreglos_aleatorios(n)
        selec_voraz(c, f, n)
        tiempoEjecucionesVoraz[idx, run] = conteoPasos

        # Programación dinámica
        c, f = generar_arreglos_aleatorios(n)
        seleccion_actividades_dp(c, f)
        tiempoEjecucionesDP[idx, run] = conteoPasosDP

# Graficar resultados
plt.figure(figsize=(12, 8))

# Algoritmo voraz
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesVoraz[:, j], marker='o', linestyle='-', label=f'Voraz - Ejecución {j+1}' if j == 0 else "")

# Programación dinámica
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesDP[:, j], marker='s', linestyle=':', label=f'DP - Ejecución {j+1}' if j == 0 else "")

plt.xlabel('Cantidad de datos')
plt.ylabel('Cantidad de pasos ejecutados')
plt.title('Comparación de pasos ejecutados entre algoritmo voraz y programación dinámica')
plt.xticks(tamaños, rotation=90)
plt.legend()
plt.grid(True)
plt.show()
