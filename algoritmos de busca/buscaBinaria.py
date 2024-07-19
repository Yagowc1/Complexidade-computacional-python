def busca_binaria(arr, x):
    """
    Realiza uma busca binária em um array ordenado.
    
    :param arr: Lista de elementos ordenados.
    :param x: Elemento a ser buscado.
    :return: Índice do elemento, se encontrado. Caso contrário, -1.
    """
    esquerda = 0
    direita = len(arr) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == x:
            return meio
        elif arr[meio] < x:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

# Exemplo de uso
arr = [2, 3, 4, 10, 40]
x = 10
resultado = busca_binaria(arr, x)
print(f"Elemento encontrado no índice: {resultado}")