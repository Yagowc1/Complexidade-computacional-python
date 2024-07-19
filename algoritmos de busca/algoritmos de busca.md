# Algoritmos de busca

## Função 1: Busca Binária

```python
def busca_binaria(arr, x):
    """
    Realiza uma busca binária em um array ordenado.
    
    :param arr: Lista de elementos ordenados.
    :param x: Elemento a ser buscado.
    :return: Índice do elemento, se encontrado. Caso contrário, -1.
    """
    esquerda = 0
    direita = len(arr) - 1

    enquanto esquerda <= direita:
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
```

### Estrutura da Função

1. **Definição da Função**:
   ```python
   def busca_binaria(arr, x):
   ```
   - Define a função `busca_binaria` com os parâmetros `arr` (lista ordenada) e `x` (elemento a ser buscado).

2. **Docstring**:
   ```python
   """
   Realiza uma busca binária em um array ordenado.
    
   :param arr: Lista de elementos ordenados.
   :param x: Elemento a ser buscado.
   :return: Índice do elemento, se encontrado. Caso contrário, -1.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Inicialização dos Índices**:
   ```python
   esquerda = 0
   direita = len(arr) - 1
   ```
   - Define os índices `esquerda` e `direita` para a pesquisa.

4. **Loop While**:
   ```python
   enquanto esquerda <= direita:
   ```
   - Executa enquanto a porção da lista a ser buscada é válida.

5. **Calcular o Índice do Meio**:
   ```python
   meio = (esquerda + direita) // 2
   ```
   - Calcula o índice do meio da porção atual da lista.

6. **Comparar o Elemento do Meio**:
   ```python
   if arr[meio] == x:
       return meio
   elif arr[meio] < x:
       esquerda = meio + 1
   else:
       direita = meio - 1
   ```
   - Compara o elemento do meio com `x`:
     - Se `arr[meio]` é igual a `x`, retorna `meio`.
     - Se `arr[meio]` é menor que `x`, atualiza `esquerda` para `meio + 1`.
     - Se `arr[meio]` é maior que `x`, atualiza `direita` para `meio - 1`.

7. **Elemento Não Encontrado**:
   ```python
   return -1
   ```
   - Se o loop termina sem encontrar o elemento, retorna `-1`.

### Passo a Passo

1. A função é chamada com a lista `[2, 3, 4, 10, 40]` e o elemento `10` a ser buscado.
2. Inicializa `esquerda` em `0` e `direita` em `4`.
3. Calcula o índice do meio: `(0 + 4) // 2 = 2`.
4. Compara `arr[2]` (4) com `10`: como `4 < 10`, atualiza `esquerda` para `3`.
5. Calcula o novo meio: `(3 + 4) // 2 = 3`.
6. Compara `arr[3]` (10) com `10`: como são iguais, retorna `3`.

---

## Função 2: Busca Sequencial

```python
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
```

### Estrutura da Função

1. **Definição da Função**:
   ```python
   def busca_sequencial(arr, x):
   ```
   - Define a função `busca_sequencial` com os parâmetros `arr` (lista) e `x` (elemento a ser buscado).

2. **Docstring**:
   ```python
   """
   Realiza uma busca sequencial em um array.
    
   :param arr: Lista de elementos.
   :param x: Elemento a ser buscado.
   :return: Índice do elemento, se encontrado. Caso contrário, -1.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Loop For**:
   ```python
   for i in range(len(arr)):
   ```
   - Itera sobre cada índice `i` da lista.

4. **Comparação do Elemento**:
   ```python
   if arr[i] == x:
       return i
   ```
   - Se `arr[i]` é igual a `x`, retorna o índice `i`.

5. **Elemento Não Encontrado**:
   ```python
   return -1
   ```
   - Se o loop termina sem encontrar o elemento, retorna `-1`.

### Passo a Passo

1. A função é chamada com a lista `[2, 3, 4, 10, 40]` e o elemento `10` a ser buscado.
2. Itera sobre cada índice da lista:
   - `i = 0`: `arr[0]` (2) não é igual a `10`.
   - `i = 1`: `arr[1]` (3) não é igual a `10`.
   - `i = 2`: `arr[2]` (4) não é igual a `10`.
   - `i = 3`: `arr[3]` (10) é igual a `10`, então retorna `3`.