# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def adiar(y):
        return funcao(x , y) 
    return adiar


    

soma_com_cinco = criar_funcao(soma, 5)
print(soma_com_cinco(7))
multiplica_por_dez = criar_funcao(multiplica, 10)
print(multiplica_por_dez(10))
