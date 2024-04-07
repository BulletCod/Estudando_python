entrar_sair = input('Se deseja entrar na calculadora digite "entrar " ou "sair" para encerar o programa: ')

while entrar_sair == 'entrar': 
    num1 =input('digite o primeiro numero: ')
    num2 =input('digite o segundo numero: ')
    operacao = input('digite qual operação voce deseja realizar: \n "a"- adição \n "s" - subtração \n "m"- multiplicação \n "d" - divisão: ')
    
    Numeros_validos = None

    try:
        Numeros_validos = True

    except: 
        Numeros_validos = None
        

    if Numeros_validos is None:
        print('Você não digitou numeros tente novamente')
        continue
    
    operadores_validos = 'asmd'

    if operacao not in operadores_validos:
        print('Você digitou uma operação ivalida tente novamente com os permitidos')
        continue
    #começa a operação:
     
    num1 = float(num1)
    num2 = float(num2)     
    if operacao =='a':
            adicao = num1 + num2
            print(adicao)

    elif operacao == 's':
            subtracao = num1 - num2
            print(subtracao)

    elif operacao == 'm':
            multiplicao = num1 * num2
            print(multiplicao)

    elif operacao == 'd':
            divisao = num1 / num2
            print(divisao)
    #termina as operações 
    
    programa = input('Se deseja continuar na calculadora digite "sim " ou "sair" para encerar o programa: ')
    if programa == 'sair':
        break

print('voce saiu do programa')