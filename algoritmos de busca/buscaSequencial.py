def busca_sequencial(arr, x):
    """
    Realiza uma busca sequencial em um array.
    
    :param arr: Lista de elementos.
    :param x: Elemento a ser buscado.
    :return: Índice do elemento, se encontrado. Caso contrário, -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Exemplo de uso
arr = [2, 3, 4, 10, 40]
x = 10
resultado = busca_sequencial(arr, x)
print(f"Elemento encontrado no índice: {resultado}")  # Output: 3