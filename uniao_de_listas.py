# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# Resultado

#[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest #usado para pegar o tamanho maximo da lista mesmo que não possa iterar 

def zipper (lista1, lista2): 
    intervalo =  min(len(lista1),len(lista2))# Usado para pegar o valor minimo entre as lisatas podendo usar "max" também
    return [(l1[i],l2[i]) for i in range(intervalo)] #retorna a contagem de itens dentro de cada lista pelas posições
       
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1, l2))#este so funciona depois do import

print(list(zip(l1,l2)))#maneira mais simplificada de fazer tudo isso. 
print(list(zip_longest(l1,l2))) 