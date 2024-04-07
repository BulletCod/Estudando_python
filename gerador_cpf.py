import random
import sys # importe que tem a função q sai do programa

cpf = ''
for i in range(9):
    cpf += str(random.randint(0, 9))

print(cpf)

#pega somente 9 digitos do cpf
soma_de_numeros = 0
i = 10

for numeros_cpf in cpf: 
    soma_de_numeros += int(numeros_cpf)*i
    i -= 1
digito = (soma_de_numeros * 10) % 11
novo_digito = digito if digito <= 9 else 0


cpf_10 = cpf + str(novo_digito)
soma_de_numeros_2 = 0
i_2 = 11

for numeros_cpf_2 in cpf_10: 
    soma_de_numeros_2 += int(numeros_cpf_2)*i_2
    i_2 -= 1
digito_2 = (soma_de_numeros_2 * 10) % 11
novo_digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_gerado = f'{cpf}{novo_digito}{novo_digito_2}'

print(cpf_gerado)