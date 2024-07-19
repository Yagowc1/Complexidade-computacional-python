def selection_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Selection Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Exemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [11, 12, 22, 25, 64]