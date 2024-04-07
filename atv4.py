"""
 coloque seu nome e retorne cada letra com asteriscos entre eles 
"""
nome = input('digite seu nome: ')
condicao = 0
novo_nome = '' #começa com espaços vazios mas a cada iteração do while ele adiciona uma letra para ficar na mesma linha
while condicao < len(nome):
    
    letra = nome[condicao] #adiciona cada letra digitada 
    novo_nome += f'*{letra}' #pegada cada letra acrescentada em letra e coloca nos espaços vazios 
    condicao +=1 #para rodar ate o final do nome
novo_nome += '*' #asterisco no final do nome 
print(novo_nome)