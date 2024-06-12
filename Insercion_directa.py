#Este programa genera un arreglo de tamaño n ya sea en orden ascendente, descendente o aleatorio (El usuario elije)
#Después ordena ese mismo arreglo usando insertion sort y cuenta el número de operaciones (intercabios) que se realizan para obtener el arreglo ordenado
#Todo esto sucede 10 veces

import random

#Devuelve una lista de enteros de tamaño n en orden ascendente
def bestA(n):
	lista = []
	for i in range(n):
		lista.append(i)
	
	return lista

#Devuelve una lista de enteros de tamaño n en orden descendente
def worstA(n):
	lista = []
	for i in range(n):
		lista.insert(0, i) #Insertamos un valor en el índice deseado, en este caso en el índice 0
	
	return lista

#Decuelve una lista de enteros (generados y ordenados aleatoriamente) de tamaño n
def randomA(n):
	lista = []
	for i in range(0, n):
		numAleatorio = random.randint(1,1000)	#Genera un número aleatorio entre 1 y 1000
		lista.append(numAleatorio)
	return lista

#Ordena una lista
def insertionSort(lista):
	n = len(lista)
	contOperaciones = 0
	for j in range(1, n):	#Empezamos a evaluar desde el segundo dato de la lista
		aux = lista[j]		#Se asigna el valor del elemento de la lista que está siendo evaluado a la variable aux
		contOperaciones += 1	#Contamos las operaciones relevantes, en este caso es el cambio de índice
		i = j-1				#Índice del elemento anterior al elemento de la lista que está siendo evaluado
		while aux < lista[i] and i>=0:
			lista[i+1] = lista[i]
			contOperaciones += 1	#Contamos las operaciones relevantes, en este caso son las asignaciones
			i -= 1
		lista[i+1] = aux
		contOperaciones += 1 #Contamos las operaciones relevantes, en este caso son las asignaciones
	return contOperaciones

#Muestra el contenido de una lista
def showList(lista):
	for number in A:
		print(number, end = " ")

opcion = input("Escribe 1 para ejecutar el programa con el mejor de los casos (ordenar arreglo ya ordenado)\nEscribe 2 para ejecutar con el peor de los casos (arreglo ordenado descendentemente)\nEscribe 3 para ejecutar con caso promedio (arreglo con datos en orden aleatorio)\n")

tam_n = [10,20,30,40,50,60,70, 80,90,100]
n = int(10)	#Cant de enteros que habrá en los arreglos
totalOperaciones = 0

while 1:
	match opcion:
		case '1':
			for i in range(0,10):
				A = bestA(n)
				print("\n\nArreglo antes de ser ordenado")
				showList(A)
					
				totalOperaciones = totalOperaciones + insertionSort(A)

				print("\nArreglo después de ser ordenado")
				showList(A)

				print("\n\nSe han realizado ", totalOperaciones, "operaciones\n")
			break
		case '2':
			for i in range(0,10):
				A = worstA(n)
				print("\nArreglo antes de ser ordenado")
				showList(A)
					
				totalOperaciones = totalOperaciones + insertionSort(A)

				print("\n\nArreglo después de ser ordenado")
				showList(A)

				print("\n\nSe han realizado ", totalOperaciones, "operaciones\n")
			break
		case '3':
			for i in range(0,10):
				A = randomA(n)
				print("\n\nArreglo antes de ser ordenado")
				showList(A)
					
				totalOperaciones = totalOperaciones + insertionSort(A)

				print("\nArreglo después de ser ordenado")
				showList(A)

				print("\n\nSe han realizado ", totalOperaciones, "operaciones\n")
			break
		case _:
			print("Opción no válida")
			opcion = input("Escribe 1 para ejecutar el programa con el mejor de los casos (ordenar arreglo ya ordenado)\nEscribe 2 para ejecutar con el peor de los casos (arreglo ordenado descendentemente)\nEscribe 2 para ejecutar con caso promedio (arreglo con datos en orden aleatorio)\n")


