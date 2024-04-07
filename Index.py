nome = input("digite seu nome: ")
idade = (input("digite sua idade: "))
if nome and idade:
    print(f'seu nome é: {nome}')
    print (f'seu nome invertido é: {nome[::-1]}')

    espacos = ' ' in nome 

    if  espacos == True:
        print('seu nome contém espaços')
    else:
        print('seu nome não contem espaços')

    print(f' seu nome tem {len(nome)} letras')
    print(f' a primeira letra do seu nome é {nome[0]}')
    print(f'sua ultima letra do seu nome é {nome[-1]}')

else:
    print("você asuihasuih")   


 


