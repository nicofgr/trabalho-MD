from numpy import random
from matplotlib import pyplot as plt
import time
 
 
# Function to find the partition position
def partition(array, low, high):
 
  # Choose the rightmost element as pivot
  pivot = array[high]
 
  # Pointer for greater element
  i = low - 1
 
  # Traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # If element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1
 
      # Swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])
 
  # Swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])
 
  # Return the position from where partition is done
  return i + 1
 
# Function to perform quicksort
def quick_sort(array, low, high):
  if low < high:
 
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)
 
    # Recursive call on the left of pivot
    quick_sort(array, low, pi - 1)
 
    # Recursive call on the right of pivot
    quick_sort(array, pi + 1, high)
 
   
         
#Variaveis

resultados = [[],[]] #Tamanho x Valores

resMedia = [[],[]] #Tamanho x Valores

tamanhos = 20 # 1000 ate (tamanhos+1) * 1000
repeticoes = 5 
for i in range(tamanhos):
    numElementos = 1000 * (1 + i)

    for j in range(repeticoes):

        arr = random.randint(100, size=(numElementos))

        #Mede o tempo de execucao
        tInicial = time.process_time()
        quick_sort(arr, 0, len(arr) - 1)
        tFinal = time.process_time()
        tTotal = tFinal - tInicial

        resultados[0].append(numElementos)
        resultados[1].append(tTotal)

        print('quickSort')
        print('Numero de elementos:', numElementos )
        print('Tempo de execucao: ', tTotal, 'segundos')

#Media
for i in range(tamanhos):
    resMedia[0].append(1000 * (1 + i))
    resMedia[1].append(0)

    for j in range(repeticoes):
        resMedia[1][i] = (resMedia[1][i] + resultados[1][(repeticoes*i)+j])

    resMedia[1][i] /= repeticoes
        
print('TESTE')
print(resMedia[0])
print(resMedia[1])

#Grafico
plt.scatter(resultados[0], resultados[1], label = 'Dados brutos')
plt.plot(resMedia[0], resMedia[1], 'r--', label = 'Media')
plt.title('quickSort')
plt.xlabel('Quantidade de elementos')
plt.ylabel('Tempo de execucao (segundos)')
plt.legend()

plt.show()
