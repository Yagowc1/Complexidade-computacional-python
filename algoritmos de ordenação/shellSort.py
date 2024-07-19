def shell_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Shell Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
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

# Exemplo de uso
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [2, 3, 12, 34, 54]