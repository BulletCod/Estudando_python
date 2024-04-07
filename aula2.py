"""informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('digite um numero: ')
numero_float= float(numero_str)


if numero_str.isdigit():

    divisao_por_dois= numero_float%2

    if divisao_por_dois == 0:
        print('o numero é par')
    else:
        print('o numero é impar')

else:
    print('Por favor digite um inteiro!')