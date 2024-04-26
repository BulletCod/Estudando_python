class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando   
    def filmagem (self):
        if self.filmando:
            print(f'{self.filmando} Já está filmando')
            return
        
        print(f'{self.nome} Já está filmando')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.filmando} Não está filmando')
            return
        print(f'{self.nome} Está parando de filmar')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando')
            return
        print(f'{self.nome}Pode fotografar')

c1 = Camera('Canon')
c1.filmagem()

