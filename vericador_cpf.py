import re # importe que substitui os caracteres
import sys # importe que tem a função q sai do programa

cpf_enviado = input('digite seu cpf no formato XXX.XXX.XXX-XX ou sem caracteres: ')

cpf = re.sub(
    r'[^0-9]', '', cpf_enviado #substitui os caracteres por espaços vazios 
)
digitos_sequencial = cpf_enviado == cpf_enviado[0]* len(cpf_enviado) #verifica se  o usuario digitou o mesmo caracter repetidas vezes

if digitos_sequencial:
     print('Você enviou dados sequenciais.')
     sys.exit() #sai do programa 
if len(cpf_enviado)> 14:
    print('Seu cpf possui numeros a mais')
    sys.exit()

cpf_9 = cpf[:9] #pega somente 9 digitos do cpf
soma_de_numeros = 0
i = 10

for numeros_cpf in cpf_9: 
    soma_de_numeros += int(numeros_cpf)*i
    i -= 1
digito = (soma_de_numeros * 10) % 11
novo_digito = digito if digito <= 9 else 0


cpf_10 = cpf[:10]
soma_de_numeros_2 = 0
i_2 = 11

for numeros_cpf_2 in cpf_10: 
    soma_de_numeros_2 += int(numeros_cpf_2)*i_2
    i_2 -= 1
digito_2 = (soma_de_numeros_2 * 10) % 11
novo_digito_2 = digito_2 if digito_2 <= 9 else 0


cpf_completo = f'{cpf_9}{novo_digito}{novo_digito_2}'

if cpf == cpf_completo:
    print('CPF é valido')
else: 
    print('CPF invalido')

