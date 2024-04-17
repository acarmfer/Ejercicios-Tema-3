import random
import time

# Algoritmo de ordenamiento por casilleros (Bucket Sort)
def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_bucket = (max_val - min_val) / len(arr)
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        index = int((num - min_val) / range_bucket)
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr

# Algoritmo de ordenamiento Shell
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Algoritmo de ordenamiento Radix
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# Generar lista aleatoria de elementos
def generate_random_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_sorting_algorithm(sorting_algorithm, lst):
    start_time = time.time()
    sorting_algorithm(lst)
    end_time = time.time()
    return end_time - start_time

# Generar listas para probar los algoritmos de ordenamiento
sizes = [100000, 1000000, 10000000]
for size in sizes:
    random_list = generate_random_list(size)
    
    time_bucket_sort = measure_sorting_algorithm(bucket_sort, random_list.copy())
    time_shell_sort = measure_sorting_algorithm(shell_sort, random_list.copy())
    time_radix_sort = measure_sorting_algorithm(radix_sort, random_list.copy())
    
    print(f"Tamaño de la lista: {size}")
    print(f"Tiempo de ejecución de Bucket Sort: {time_bucket_sort} segundos")
    print(f"Tiempo de ejecución de Shell Sort: {time_shell_sort} segundos")
    print(f"Tiempo de ejecución de Radix Sort: {time_radix_sort} segundos")
    print()

# Generar lista aleatoria de elementos para probar algoritmos de búsqueda
def generate_random_search_list(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Algoritmo de búsqueda lineal
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

# Algoritmo de búsqueda binaria
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Medir el tiempo de ejecución de un algoritmo de búsqueda
def measure_search_algorithm(search_algorithm, lst, target):
    start_time = time.time()
    search_algorithm(lst, target)
    end_time = time.time()
    return end_time - start_time

# Generar listas para probar los algoritmos de búsqueda
search_sizes = [100000, 1000000, 10000000]
for size in search_sizes:
    random_list = generate_random_search_list(size)
    target = random.randint(0, 1000000)
    
    time_linear_search = measure_search_algorithm(linear_search, random_list.copy(), target)
    time_binary_search = measure_search_algorithm(binary_search, sorted(random_list.copy()), target)
    
    print(f"Tamaño de la lista: {size}")
    print(f"Tiempo de ejecución de Búsqueda Lineal: {time_linear_search} segundos")
    print(f"Tiempo de ejecución de Búsqueda Binaria: {time_binary_search} segundos")
    print()
