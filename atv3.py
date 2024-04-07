"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

nome = input('digite seu nome: ')

qtd_letras_nome = len(nome)

nome_curto = qtd_letras_nome<= 4
nome_normal= 5<=qtd_letras_nome<=6

if nome_curto:
    print('seu nome é curto')
elif nome_normal:
    print('seu nome é normal')
else:
    print('seu nome é gigante por favor mude-o')