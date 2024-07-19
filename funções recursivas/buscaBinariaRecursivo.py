def busca_binaria(arr, esquerda, direita, x):
    """
    Realiza uma busca binária recursiva em um array ordenado.
    
    :param arr: Lista de elementos ordenados.
    :param esquerda: Índice inicial.
    :param direita: Índice final.
    :param x: Elemento a ser buscado.
    :return: Índice do elemento, se encontrado. Caso contrário, -1.
    """
    if direita >= esquerda:
        meio = (esquerda + direita) // 2
        if arr[meio] == x:
            return meio
        elif arr[meio] > x:
            return busca_binaria(arr, esquerda, meio - 1, x)
        else:
            return busca_binaria(arr, meio + 1, direita, x)
    else:
        return -1

# Exemplo de uso
arr = [2, 3, 4, 10, 40]
x = 10
resultado = busca_binaria(arr, 0, len(arr) - 1, x)
print(f"Elemento encontrado no índice: {resultado}")  # Output: 3