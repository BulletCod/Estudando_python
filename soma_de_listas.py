

def soma_lista(lista1, lista2):
    intervalo = min (len(lista1),len(lista2))
    soma = [ l1[i] + l2[i] for i in range(intervalo)]
    return soma 
 

l1 = [3, 2.2, 4, 6, 1]
l2 = [1, 2, 4, 5, 3, 8, 10, 15]
print(soma_lista(l1,l2))