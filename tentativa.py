produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''def filtrar (produto):
    for produto in produtos:
        if produto ['preco'] > 10 :
            print(produto)
        
filtrar(produtos)'''



'''def filtrar_produtos_por_preco(produto):
    return produto['preco'] > 100 



novos_produtos = filter(
    filtrar_produtos_por_preco,
    produtos
)

print(*list(novos_produtos))'''

def print_iter(iterador):
    print(*list(iterador),sep='\n')
    print()

novo_produto = filter(
    lambda p: p ['preco'] > 10,
    produtos

)
#print_iter(novo_produto)

print(*list(novo_produto),sep='\n')