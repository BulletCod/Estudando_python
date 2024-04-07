# Lista de números
lista_numeros = [1, 2, 3, 4, 5]

# Variável para armazenar a soma
soma = 0

# Laço de repetição para percorrer a lista
for numero in lista_numeros:
    # Armazena o número da lista
    numero_armazenado = numero
    
    # Soma o número armazenado com outro número (nesse caso, 10)
    resultado = numero_armazenado + 10
    
    # Adiciona o resultado à soma total
    soma += resultado

# Imprime o resultado final
print("A soma total é:", soma)
