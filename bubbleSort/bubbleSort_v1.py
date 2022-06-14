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

numElementos = 2000
arr = random.randint(100, size=(numElementos))
 
#Mede o tempo de execução
tInicial = time.process_time()
bubbleSort(arr)
tFinal = time.process_time()

tTotal = tFinal - tInicial

print('bubbleSort')
print('Numero de elementos:', numElementos )
print('Tempo de execucao: ', tTotal, 'segundos')

#Gráfico

plt.scatter(numElementos, tTotal)
plt.title('bubbleSort')
plt.xlabel('Quantidade de elementos')
plt.ylabel('Tempo de execucao (segundos)')

plt.show()


