
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    
    print(f'pergunta: {pergunta['Pergunta']}')

    opcoes = pergunta['Opções']
    

    for i , opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')

    escolha = input('escolha uma opcao: ') 

    escolha_int = None
    qtd_opcoes = len(opcoes)
    acertou = False

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                    acertou = True
                 
                    
    if acertou:
        qtd_acertos += 1 
        print('voce acertou')
    else:
        print('voce errou')

print (f'voce acertou {qtd_acertos} de {len(pergunta)} perguntas')
    
                          


   
        
    
