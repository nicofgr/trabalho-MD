#IMPORT:
from numpy import random
from matplotlib import pyplot as plt
import time

#FUNCOES SORT
#bubbleSort:
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

#quickSort:
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

#radixSort
def countingSort(arr, exp1):
  
    n = len(arr)
  
    # The output array elements that will have sorted arr
    output = [0] * (n)
  
    # initialize count array as 0
    count = [0] * (10)
  
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
  
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
  
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
  
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
  
def radixSort(arr):
  
    # Find the maximum number to know number of digits
    max1 = max(arr)
  
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(arr, exp)
        exp *= 10


#Variaveis

resultados = [[],[]] #Tamanho x Valores

resMedia = [[],[]] #Tamanho x Valores

tamanhos = 5 # 1000 ate (tamanhos+1) * 1000
repeticoes = 5 
for i in range(tamanhos):
    numElementos = 100 * (1 + i)

    for j in range(repeticoes):

        arr = random.randint(100, size=(numElementos))

        #Mede o tempo de execucao
        tInicial = time.process_time()
        # Function Call
        bubbleSort(arr)
        #quick_sort(arr, 0, len(arr) - 1)
        #radixSort(arr)
        

        tFinal = time.process_time()
        tTotal = tFinal - tInicial

        resultados[0].append(numElementos)
        resultados[1].append(tTotal)

        print('radixSort')
        print('Numero de elementos:', numElementos )
        print('Tempo de execucao: ', tTotal, 'segundos')

#Media
for i in range(tamanhos):
    resMedia[0].append(100 * (1 + i))
    resMedia[1].append(0)

    for j in range(repeticoes):
        resMedia[1][i] = (resMedia[1][i] + resultados[1][(repeticoes*i)+j])

    resMedia[1][i] /= repeticoes
        
print('MEDIA')
print(resMedia[0])
print(resMedia[1])

#Grafico
plt.scatter(resultados[0], resultados[1], label = 'Dados brutos')
plt.plot(resMedia[0], resMedia[1], 'r--', label = 'Media')
plt.title('radixSort')
plt.xlabel('Quantidade de elementos')
plt.ylabel('Tempo de execucao (segundos)')
plt.legend()

plt.show()

