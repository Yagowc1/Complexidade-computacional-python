# Funções recursivas

## Função 1: Busca Binária Recursiva

```python
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
```

### Estrutura da Função

1. **Definição da Função**:
   ```python
   def busca_binaria(arr, esquerda, direita, x):
   ```
   - Define a função `busca_binaria` com os parâmetros `arr` (lista ordenada), `esquerda` (índice inicial), `direita` (índice final) e `x` (elemento a ser buscado).

2. **Docstring**:
   ```python
   """
   Realiza uma busca binária recursiva em um array ordenado.
    
   :param arr: Lista de elementos ordenados.
   :param esquerda: Índice inicial.
   :param direita: Índice final.
   :param x: Elemento a ser buscado.
   :return: Índice do elemento, se encontrado. Caso contrário, -1.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Condição Base**:
   ```python
   if direita >= esquerda:
   ```
   - Verifica se a pesquisa ainda é válida, ou seja, se a porção da lista a ser buscada é válida.

4. **Calcular o Índice do Meio**:
   ```python
   meio = (esquerda + direita) // 2
   ```
   - Calcula o índice do meio da porção atual da lista.

5. **Comparar o Elemento do Meio**:
   ```python
   if arr[meio] == x:
       return meio
   elif arr[meio] > x:
       return busca_binaria(arr, esquerda, meio - 1, x)
   else:
       return busca_binaria(arr, meio + 1, direita, x)
   ```
   - Compara o elemento do meio com `x`:
     - Se `arr[meio]` é igual a `x`, retorna `meio`.
     - Se `arr[meio]` é maior que `x`, chama a função recursivamente para a metade esquerda.
     - Se `arr[meio]` é menor que `x`, chama a função recursivamente para a metade direita.

6. **Elemento Não Encontrado**:
   ```python
   else:
       return -1
   ```
   - Se `direita` é menor que `esquerda`, retorna `-1`, indicando que o elemento não foi encontrado.

### Passo a Passo

1. A função é chamada com a lista `[2, 3, 4, 10, 40]`, índices `0` e `4` (inicial e final), e o elemento `10` a ser buscado.
2. Calcula o índice do meio: `(0 + 4) // 2 = 2`.
3. Compara `arr[2]` (4) com `10`: como `4 < 10`, chama a função recursivamente para a metade direita.
4. Na próxima chamada, os índices são `3` e `4`. Calcula o novo meio: `(3 + 4) // 2 = 3`.
5. Compara `arr[3]` (10) com `10`: como são iguais, retorna `3`.

---

## Função 2: Cálculo do Fatorial Recursivo

```python
def fatorial(n):
    """
    Calcula o fatorial de um número de forma recursiva.
    
    :param n: Número inteiro não negativo.
    :return: Fatorial de n.
    """
    if n == 0 ou n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
print(f"Fatorial de 5: {fatorial(5)}")  # Output: 120
```

### Estrutura da Função

1. **Definição da Função**:
   ```python
   def fatorial(n):
   ```
   - Define a função `fatorial` com o parâmetro `n` (número inteiro não negativo).

2. **Docstring**:
   ```python
   """
   Calcula o fatorial de um número de forma recursiva.
    
   :param n: Número inteiro não negativo.
   :return: Fatorial de n.
   """
   ```
   - Explica o propósito da função e descreve o parâmetro e o valor de retorno.

3. **Condição Base**:
   ```python
   if n == 0 ou n == 1:
       return 1
   ```
   - Verifica se `n` é `0` ou `1`, e retorna `1`, pois `0!` e `1!` são ambos `1`.

4. **Chamada Recursiva**:
   ```python
   else:
       return n * fatorial(n - 1)
   ```
   - Para `n` maior que `1`, retorna `n` multiplicado pelo fatorial de `n-1`.

### Passo a Passo

1. A função é chamada com `5`.
2. Como `5` não é `0` nem `1`, calcula `5 * fatorial(4)`.
3. Para calcular `fatorial(4)`, calcula `4 * fatorial(3)`.
4. Para calcular `fatorial(3)`, calcula `3 * fatorial(2)`.
5. Para calcular `fatorial(2)`, calcula `2 * fatorial(1)`.
6. `fatorial(1)` retorna `1`.
7. Calcula `2 * 1 = 2`.
8. Calcula `3 * 2 = 6`.
9. Calcula `4 * 6 = 24`.
10. Calcula `5 * 24 = 120`.

O fatorial de `5` é `120`.