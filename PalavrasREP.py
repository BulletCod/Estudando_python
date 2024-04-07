""" 
verifique nessa frase qual foi a letra mais repetidas

"""
frase = 'O python é uma linguagem de programação' \
'multipragmatica'\
'Python foi criado por PowerGuido Van Rossum.'
i = 0
qtd_maior_repetidas = 0 #declaro a variavel com o valor zero
letras_mais_repetidas = '' # declaro esta sendo uma string vazia pois irei armazenar ela a letra mais repetida 
while i < len(frase): #executa ate ser menor que o tamanho da frase
    
    letra_atual = frase[i] #pega a letra atual incrementada no contador i pois o i é o indice da frase

    if  letra_atual == ' ': #criado  para que os espaços nao seja o maior repetido
        i+=1 #criado para quando o maior repetido por o espaço ja incremantar mais um e contiar o codigo depois de incrementado e nao da bug
        continue #vai daqui pro inicio pulando os codigos abaixo dele 
        

    qtd_vezes_repetidas = frase.count(letra_atual) #com o comando count conto quantas vezes uma letra repetiu por toda a frase e coloco nesta variavel

    if qtd_vezes_repetidas > qtd_maior_repetidas: #if criado para armazenar o valor da ultima letra mais repetida e verificar com a proxima a ser contada pelo count
        qtd_maior_repetidas = qtd_vezes_repetidas # troco o valor incial dele que foi declarado como 0 e substituo o valor da quatidade de letra maior repetida para verificar novamente quando esse if for repetido
        letras_mais_repetidas = letra_atual #substituo o valor de letra_mais_repetida que antes era espaço vazio pela letra mais repetida atualmente

   
    i += 1
print(f'a letra mais repetida foi " {letras_mais_repetidas} " e esta foi repitada {qtd_maior_repetidas} vezes')