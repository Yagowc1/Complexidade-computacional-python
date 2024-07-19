def bubble_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Bubble Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [11, 12, 22, 25, 34, 64, 90]