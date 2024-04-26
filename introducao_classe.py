class Carro:
    def __init__(self,nome,cor):

        self.nome = nome
        self.cor = cor

fusca = Carro('Fusca','amarelo')
print(f'{fusca.nome} de cor {fusca.cor}')

celta = Carro(nome='celta', cor='azul')
print(f'{celta.nome} de cor {celta.cor}')
