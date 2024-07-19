# Explicação dos Algoritmos de Ordenação em Python

# Sumário

- [Bubble Sort](#algoritmo-1-bubble-sort)
- [Insertion Sort](#algoritmo-2-insertion-sort)
- [Merge Sort](#algoritmo-3-merge-sort)
- [Quick Sort](#algoritmo-4-quick-sort)
- [Selection Sort](#algoritmo-5-selection-sort)
- [Shell Sort](#algoritmo-6-shell-sort)

## Algoritmo 1: Bubble Sort

```python
def bubble_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Bubble Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def bubble_sort(arr):
   ```
   - Define a função `bubble_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Bubble Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Obter o Comprimento da Lista**:
   ```python
   n = len(arr)
   ```
   - Obtém o número de elementos na lista.

4. **Loop Externo**:
   ```python
   for i in range(n):
   ```
   - Itera sobre cada elemento da lista, realizando várias passagens de bolhas.

5. **Loop Interno**:
   ```python
   for j in range(0, n - i - 1):
   ```
   - Itera até o elemento não ordenado mais distante, empurrando o maior elemento para o final da lista.

6. **Comparação e Troca de Elementos**:
   ```python
   if arr[j] > arr[j + 1]:
       arr[j], arr[j + 1] = arr[j + 1], arr[j]
   ```
   - Compara e troca elementos adjacentes se estiverem na ordem errada.

### Passo a Passo

1. A função é chamada com a lista `[64, 34, 25, 12, 22, 11, 90]`.
2. Durante a primeira passagem, o maior elemento (90) é movido para o final da lista.
3. Em cada passagem subsequente, os próximos maiores elementos são movidos para a posição correta.
4. Após várias passagens, a lista fica completamente ordenada.

---

## Algoritmo 2: Insertion Sort

```python
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
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def insertion_sort(arr):
   ```
   - Define a função `insertion_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Insertion Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Loop Externo**:
   ```python
   for i in range(1, len(arr)):
   ```
   - Itera sobre cada elemento a partir do segundo, considerando-o como chave para inserção.

4. **Definir a Chave e Índice Anterior**:
   ```python
   key = arr[i]
   j = i - 1
   ```
   - Define a chave como o elemento atual e o índice anterior para comparação.

5. **Loop Interno para Inserção**:
   ```python
   while j >= 0 and key < arr[j]:
       arr[j + 1] = arr[j]
       j -= 1
   arr[j + 1] = key
   ```
   - Move elementos maiores que a chave para a direita e insere a chave na posição correta.

### Passo a Passo

1. A função é chamada com a lista `[12, 11, 13, 5, 6]`.
2. Começa com o segundo elemento (11) e insere na posição correta.
3. Continua com cada elemento subsequente, inserindo-os na posição correta em relação aos anteriores.
4. Após processar todos os elementos, a lista fica ordenada.

---

## Algoritmo 3: Merge Sort

```python
def merge_sort(arr):
    """
    Ordena uma lista de elementos utilizando o algoritmo Merge Sort.
    
    :param arr: Lista de elementos a serem ordenados.
    :return: Lista ordenada.
    """
    if len(arr) > 1:
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(f"Array ordenado: {arr}")  # Output: [5, 6, 7, 11, 12, 13]
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def merge_sort(arr):
   ```
   - Define a função `merge_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Merge Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Condição Base**:
   ```python
   if len(arr) > 1:
   ```
   - Verifica se a lista tem mais de um elemento para continuar com a divisão.

4. **Dividir a Lista**:
   ```python
   meio = len(arr) // 2
   esquerda = arr[:meio]
   direita = arr[meio:]
   ```
   - Divide a lista em duas metades: esquerda e direita.

5. **Chamada Recursiva**:
   ```python
   merge_sort(esquerda)
   merge_sort(direita)
   ```
   - Chama a função recursivamente para as duas metades até que cada sublista tenha um único elemento.

6. **Mesclagem das Sublistas**:
   ```python
   i = j = k = 0

   while i < len(esquerda) and j < len(direita):
       if esquerda[i] < direita[j]:
           arr[k] = esquerda[i]
           i += 1
       else:
           arr[k] = direita[j]
           j += 1
       k += 1

   while i < len(esquerda):
       arr[k] = esquerda[i]
       i += 1
       k += 1

   while j < len(direita):
       arr[k] = direita[j]
       j += 1
       k += 1
   ```
   - Mescla as sublistas ordenadas de volta na lista original.

### Passo a Passo

1. A função é chamada com a lista `[12, 11, 13, 5, 6, 7]`.
2. Divide a lista repetidamente até que cada sublista tenha um único elemento.
3. Mescla as sublistas de volta, comparando e ordenando os elementos.
4. Continua a mesclagem até que toda a lista esteja ordenada.

---

## Algoritmo 4: Quick Sort

```python
def quick_sort(arr):
    """
    Ordena uma lista de elementos utilizando

 o algoritmo Quick Sort.
    
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
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def quick_sort(arr):
   ```
   - Define a função `quick_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Quick Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Condição Base**:
   ```python
   if len(arr) <= 1:
       return arr
   ```
   - Verifica se a lista tem um único elemento ou está vazia, retornando-a como está.

4. **Escolha do Pivô**:
   ```python
   pivo = arr[len(arr) // 2]
   ```
   - Escolhe o elemento do meio como pivô.

5. **Dividir a Lista**:
   ```python
   menores = [x for x in arr if x < pivo]
   iguais = [x for x in arr if x == pivo]
   maiores = [x for x in arr if x > pivo]
   ```
   - Cria três sublistas: `menores`, `iguais` e `maiores`, em relação ao pivô.

6. **Chamada Recursiva e Combinação**:
   ```python
   return quick_sort(menores) + iguais + quick_sort(maiores)
   ```
   - Ordena recursivamente as sublistas e as combina.

### Passo a Passo

1. A função é chamada com a lista `[10, 7, 8, 9, 1, 5]`.
2. Escolhe `8` como pivô.
3. Divide a lista em sublistas: `[7, 1, 5]` (menores), `[8]` (iguais) e `[10, 9]` (maiores).
4. Ordena recursivamente as sublistas menores e maiores.
5. Combina as sublistas ordenadas para formar a lista final ordenada.

---

## Algoritmo 5: Selection Sort

```python
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
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def selection_sort(arr):
   ```
   - Define a função `selection_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Selection Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Loop Externo**:
   ```python
   for i in range(len(arr)):
   ```
   - Itera sobre cada elemento da lista, considerando-o como a posição atual.

4. **Encontrar o Índice do Menor Elemento**:
   ```python
   min_idx = i
   for j in range(i + 1, len(arr)):
       if arr[j] < arr[min_idx]:
           min_idx = j
   ```
   - Encontra o índice do menor elemento na sublista não ordenada.

5. **Troca de Elementos**:
   ```python
   arr[i], arr[min_idx] = arr[min_idx], arr[i]
   ```
   - Troca o menor elemento encontrado com o elemento na posição atual.

### Passo a Passo

1. A função é chamada com a lista `[64, 25, 12, 22, 11]`.
2. Encontra o menor elemento (11) e troca com o primeiro elemento (64).
3. Continua encontrando e trocando o próximo menor elemento com a próxima posição não ordenada.
4. Após iterar sobre toda a lista, ela fica completamente ordenada.

---

## Algoritmo 6: Shell Sort

```python
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
```

### Explicação da Função

1. **Definição da Função**:
   ```python
   def shell_sort(arr):
   ```
   - Define a função `shell_sort` com o parâmetro `arr` (lista de elementos a serem ordenados).

2. **Docstring**:
   ```python
   """
   Ordena uma lista de elementos utilizando o algoritmo Shell Sort.
    
   :param arr: Lista de elementos a serem ordenados.
   :return: Lista ordenada.
   """
   ```
   - Explica o propósito da função e descreve os parâmetros e o valor de retorno.

3. **Inicialização do Gap**:
   ```python
   n = len(arr)
   gap = n // 2
   ```
   - Define o tamanho do gap inicial como metade do comprimento da lista.

4. **Loop Principal**:
   ```python
   while gap > 0:
   ```
   - Continua enquanto o gap for maior que zero, reduzindo o gap em cada iteração.

5. **Loop Interno para Inserção**:
   ```python
   for i in range(gap, n):
       temp = arr[i]
       j = i
       while j >= gap and arr[j - gap] > temp:
           arr[j] = arr[j - gap]
           j -= gap
       arr[j] = temp
   gap //= 2
   ```
   - Realiza inserções deslocadas de acordo com o gap atual e reduz o gap para a próxima iteração.

### Passo a Passo

1. A função é chamada com a lista `[12, 34, 54, 2, 3]`.
2. Inicia com um gap de 2, realizando inserções deslocadas.
3. Reduz o gap para 1 e realiza inserções como no Insertion Sort.
4. Continua até que o gap seja zero e a lista fique completamente ordenada.