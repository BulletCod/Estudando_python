def multiplicacao (*args):
    resultado = 1
    for numeros in args:
        resultado *= numeros 
       
    return resultado

multiplicacao_1 = multiplicacao(2,3,4,5,6)
print(multiplicacao_1)   
