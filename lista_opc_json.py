import json

def adicionar_tarefa(escolha):
    tarefas.append(escolha)
    print("Tarefas:")
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa}")

def exibir_tarefas(tarefas):
    if not tarefas:
        print("Lista de tarefas está vazia.")
    else:
        print("Lista de Tarefas:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")

def desfazer_tarefas(tarefas, tarefa_apagada):
    if not tarefas:
        print('Não a nada para desfazer')
        return
    escolha = tarefas.pop()
    tarefa_apagada.append(escolha)
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa}")

def refazer_tarefas(tarefas, tarefa_apagada):
    if not tarefa_apagada:
        print('Não a nada para refazer')
        return
    escolha = tarefa_apagada.pop()
    tarefas.append(escolha)
    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa}")

def ler_json(tarefas, caminho_arq):
    try:
        dados = []
        with open('lista_opc.json', 'r', encoding='utf8') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        salvar_json(tarefas,caminho_arq)
    return dados

def salvar_json(tarefas, caminho_arquivo):
    dados = tarefas
    with open('lista_opc.json', 'w') as arquivo:
        json.dump(
            tarefas,
            arquivo,
            ensure_ascii= False,
            indent= 2,
    )
    return dados #para retornar os dados q tenho na lista

CAMINHO_ARQ = 'lista_opc.json'
tarefas = ler_json([], CAMINHO_ARQ)
tarefa_apagada = []

while True:
    
    print('Comandos: Listar , desfazer, Refazer')
    escolha = input('Digite a tarefa ou o comando: ')
    
 
    
    if escolha == 'listar':
        exibir_tarefas(tarefas)

    elif escolha == 'desfazer':
        desfazer_tarefas(tarefas, tarefa_apagada)

    elif escolha == 'refazer':
        refazer_tarefas(tarefas , tarefa_apagada)
    else:
        adicionar_tarefa(escolha)

    salvar_json(tarefas, CAMINHO_ARQ)
