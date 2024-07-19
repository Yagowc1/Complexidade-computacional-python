def fatorial(n):
    """
    Calcula o fatorial de um número de forma recursiva.
    
    :param n: Número inteiro não negativo.
    :return: Fatorial de n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
print(f"Fatorial de 5: {fatorial(5)}")  # Output: 120