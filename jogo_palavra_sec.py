palavra_secreta = 'urdino'
letra_correta = ''
i = 0 #Contador do codigo
while True:

    letra_digitada = input(' Digite uma letra: ')
    i+=1 #Faz com que a letra digitada seja incrementada de um em um
        
    if len(letra_digitada) > 1: #garante que o usuario digite apenas uma letra
        print('digite apenas uma letra!')
        i += 1
        continue #Volta ao inicio do while se ele for verdadeiro
    if letra_digitada in palavra_secreta: #procura a letra que o usuario digitou na palavra correta
        letra_correta += letra_digitada #Serve para concatenar a letra e trocar o valor vazio anterior pela petra que foi digitada corretamente

    palavra_formada = ''
    for letra_secreta in palavra_secreta: #esse for é usado para verificar se a letra que o usuario digitou esta dentro das letras da palavra informada no codigo.
        if letra_secreta in letra_correta: #Tem o papel de verificar se a letra que o usuario digitou é correta
            palavra_formada += letra_secreta #adiciona a letra que foi encontrada e é correta a palavra que vai se formar quando ele acertar a palavra
        else:
            palavra_formada+= '*' #para caso ele não acertar uma das letras presentes na palavra secreta, no print as letras estarão representadas por um *
    print(palavra_formada)

    if palavra_formada == palavra_secreta: #No momento em que ele acertar a palavra secreta aparecerá a mensagen parabenizando. 
        print(f'parabens voce acertou!! A palavra secreta escolhida era "{palavra_secreta}" e o seu total de tentativas foi {i} vezes')
    


   