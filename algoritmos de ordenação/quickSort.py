def quick_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Quick Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivo = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivo]
        iguais = [x for x in arr if x == pivo]
        maiores = [x for x in arr if x > pivo]
        return quick_sort(menores) + iguais + quick_sort(maiores)

# Exemplo de uso
arr = [10, 7, 8, 9, 1, 5]
print(f"Array ordenado: {quick_sort(arr)}")  # Output: [1, 5, 7, 8, 9, 10]