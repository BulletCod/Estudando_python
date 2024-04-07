import os

lista = []

while True:
    opcoes= input('Selecione uma opção: [i]nserir [a]pagar [l]istar [s]air: ')

    opcoes_validas ='ials'
    if opcoes not in opcoes_validas: 
        print('digite somente as letras dadas no menu!')
    
    elif opcoes == 'i':
        os.system('clear')
        item = input('valor: ')
        lista.append(item)

    elif opcoes == 'a':
        os.system('clear')
        excluir_item_str = input ('digite o indice: ')
        
    
        try:
            excluir_item_int = int(excluir_item_str)
            lista.pop(excluir_item_int)

        except ValueError:
          print('digite um numero inteiro')  
        except IndexError:
            print('digite um indice não existe na lista')


    elif opcoes == 'l':
        os.system('clear')
        if lista == []:
            print('não a nada para listar')
            continue
           
        for indice, itens in enumerate(lista): 
            print(indice,itens)
            
    if opcoes == 's':
        break






             