from numpy import random
from matplotlib import pyplot as plt
import time


#Bubblesort VV
def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 

# Driver code to test above

#Variaveis
resElementos = []
resTempo = []

resMedia = [[],[]]

tamanhos = 2
repeticoes = 2
 
for i in range(tamanhos):
    numElementos = 1000 * (1 + i)

    for j in range(repeticoes):

        arr = random.randint(100, size=(numElementos))

        #Mede o tempo de execucao
        tInicial = time.process_time()
        bubbleSort(arr)
        tFinal = time.process_time()
        tTotal = tFinal - tInicial

        resElementos.append(numElementos)
        resTempo.append(tTotal)

        print('bubbleSort')
        print('Numero de elementos:', numElementos )
        print('Tempo de execucao: ', tTotal, 'segundos')

#Media
for i in range(tamanhos):
    resMedia[0].append(1000 * (1 + i))
    resMedia[1].append(0)

    for j in range(repeticoes):
        resMedia[1][i] = (resMedia[1][i] + resTempo[j])

    #resMedia[1][i] /= repeticoes
        
print('TESTE')
print(resMedia[0])
print(resMedia[1])

#Grafico
plt.plot(resMedia[0], resMedia[1], 'r--', label = "Media")
plt.scatter(resElementos, resTempo, label = 'Dados brutos', )
plt.title('bubbleSort')
plt.xlabel('Quantidade de elementos')
plt.ylabel('Tempo de execucao (segundos)')

plt.show()


