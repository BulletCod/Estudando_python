"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

hora_str = input('Inforome a hora exata: ')
hora_float = float(hora_str)

hora_dia = 0<= hora_float and hora_float <= 11
hora_tarde = hora_float >=12 and hora_float <=17
hora_noite = hora_float >= 18 and hora_float<= 23
 
if hora_str.isdigit():
    if hora_dia: 
        print('Bom dia!')
    elif hora_tarde:
        print('boa tarde!')
    elif hora_noite:
        print('boa noite!')
    else:
        print('digite uma hora valida')        
else:
    print('digite uma hora inteira')
