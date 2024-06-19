import numpy as np
import matplotlib.pyplot as plt
import random

# Función para generar el peor caso (involucra una mayor cantidad de pasos)
def peor_caso(n):
    c = [i * 2 for i in range(n)]
    f = [i * 2 + 1 for i in range(n)]
    return c, f

# Función para generar el mejor caso (involucra una menor cantidad de pasos)
def mejor_caso(n):
    c = [0 for _ in range(n)]
    f = [i + 1 for i in range(n)]
    return c, f

# Función para generar c y f con precondiciones para un caso más común
def generar_arreglos_aleatorios(n):
    c = sorted(random.randint(0, n) for _ in range(n))
    f = [ci + random.randint(1, 5) for ci in c]
    return c, sorted(f)

# Algoritmo voraz que devuelve un conjunto con las actividades seleccionadas
def selec_voraz(c, f):
    n = len(c)  # Se determina el valor de n basándonos en la longitud del conjunto c que es igual al de f
    global conteoPasos
    conteoPasos = 0 
    A = set()  # Conjunto A creado inicializado con la primera actividad
    j = 0    # j es el índice de la última actividad seleccionada
    A.add(1) #A inicializado con la primera actividad
    for i in range(1, n):
        if c[i] >= f[j]:
            A.add(i + 1) #Se añade el índice, se le suma 1, para que al imprimirlo el usuario lo entienda
            j = i   #Se cambia el valor de j por el que tiene actualmente i
            conteoPasos += 1
    return A

# Función para seleccionar actividades usando programación dinámica
def seleccion_actividades_dp(c, f):
    n = len(c)  # Se determina el valor de n con la longitud de c, que es la misma de f
    # Se crea una lista de tuplas 'actividades' que contienen (c[i], f[i], i+1) para cada i en el rango de n
    global conteoPasosDP
    conteoPasosDP = 0
    actividades = [(c[i], f[i], i+1) for i in range(n)] 
    # Ordenar las actividades por su tiempo de finalización (f[i])
    actividades.sort(key=lambda x: x[1])  

    # Crear una lista DP para almacenar los resultados de subproblemas, inicializada en 0 con tamaño n+1
    DP = [0] * (n + 1)
    DP[1] = 1  # El primer subproblema tiene una solución de valor 1, ya que podemos seleccionar la primera actividad

    # Definir una función auxiliar para encontrar la actividad compatible más reciente
    def actividad_anterior_compat(actividad_actual):
        # Iterar en reversa desde la actividad actual hacia la primera actividad
        global conteoPasosDP
        for k in range(actividad_actual - 1, -1, -1):
            # conteoPasosDP += 1
            # Si la actividad k termina antes de que comience la actividad actual, es compatible
            if actividades[k][1] <= actividades[actividad_actual][0]:
                # conteoPasosDP += 1
                return k + 1  # Retornar el índice de la actividad compatible (ajustado para DP)
        return 0  # Si no se encuentra una actividad compatible, retornar 0

    # Iterar sobre cada actividad desde la segunda hasta la última
    for j in range(2, n + 1):
        # Calcular el valor si se incluye la actividad j-1
        incluir_actividad = 1 + DP[actividad_anterior_compat(j - 1)]
        # Almacenar el valor máximo entre incluir la actividad j-1 o no incluirla
        DP[j] = max(DP[j - 1], incluir_actividad)
        conteoPasosDP += 3  # Incrementar el contador de pasos

    conjunto_actividades = set()  # Inicializar el conjunto para almacenar las actividades seleccionadas
    j = n  # Comenzar desde la última actividad
    while j > 0:
        # Si la solución actual es diferente a la solución sin la actividad j
        if DP[j] != DP[j - 1]:
            # Añadir la actividad j-1 al conjunto de actividades seleccionadas
            conjunto_actividades.add(actividades[j - 1][2])
            # Actualizar j para ir a la siguiente actividad compatible
            j = actividad_anterior_compat(j - 1)
        else:
            # Si la actividad j no se incluye, simplemente decrementar j
            j -= 1
            conteoPasosDP += 1

    return conjunto_actividades  # Retornar el conjunto de actividades seleccionadas


# Definir tamaños de los arreglos
tamaños = list(range(10, 110, 10))

# Inicializar arreglos para almacenar los tiempos de ejecución
tiempoEjecucionesVoraz = np.zeros((10, 10))
tiempoEjecucionesDP = np.zeros((10, 10))

# Evaluar para los diferentes tamaños
for idx, n in enumerate(tamaños):
    for run in range(10):  # Realizar 10 ejecuciones para cada tamaño
        # Algoritmo voraz
        c, f = peor_caso(n)
        # c = [0, 1, 2]
        # f = [5, 2, 3]
        # c = [1, 3, 4, 8]
        # f = [2, 4, 5, 10]
        actividades_voraz = selec_voraz(c, f)
        tiempoEjecucionesVoraz[idx, run] = conteoPasos

        # Programación dinámica
        actividades_dp = seleccion_actividades_dp(c, f)
        tiempoEjecucionesDP[idx, run] = conteoPasosDP
        
    print(f"\nActividades algoritmo voraz: {actividades_voraz}")
    print(f"\nActividades algoritmo de pd: {actividades_dp}")

    
print(f"\nLa cantidad de pasos ejecutados por el algoritmo voraz son:\n {tiempoEjecucionesVoraz}")
print(f"\nLa cantidad de pasos ejecutados por el algoritmo dp son:\n {tiempoEjecucionesDP}")

# Graficar resultados
plt.figure(figsize=(12, 8))

# Algoritmo voraz
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesVoraz[:, j], marker='o', linestyle='-', label=f'Voraz' if j == 0 else "")

# Programación dinámica
for j in range(10):
    plt.plot(tamaños, tiempoEjecucionesDP[:, j], marker='s', linestyle=':', label=f'DP' if j == 0 else "")

plt.xlabel('Cantidad de datos')
plt.ylabel('Cantidad de pasos ejecutados')
plt.title('Comparación de pasos ejecutados entre algoritmo voraz y programación dinámica')
plt.xticks(tamaños, rotation=90)
plt.legend()
plt.grid(True)
plt.show()
