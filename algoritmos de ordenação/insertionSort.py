def insertion_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Insertion Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Exemplo de uso
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [5, 6, 11, 12, 13]