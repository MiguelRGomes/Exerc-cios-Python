import random

palavra = ["ALGORITMO"]
palavra = random.choice(palavra)
esconder = ["_"] * len(palavra)

input('* Jogo da Forca *')
input('Você terá 15 chances disponível')
input('Dica: Lógica de Programação')
print('Palavra: \n',esconder)

chances = 15
tentativas = 0

while tentativas < chances and ''.join(esconder) != palavra:
        letra = input('Digite uma letra: ').upper()
        if letra in palavra:
            print('Você acertou uma letra')
            tentativas += 1
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    esconder[i] = letra
                    print('Palavra: ',esconder)
                    print('Tentativas: ', tentativas)
        else:
            print('Letra incorreta')
            tentativas += 1
            print('Palavra: ',esconder)
            print('Tentativas: ', tentativas)

if tentativas == chances:
    print('Infelizmente suas tentativas acabaram. Tente novamente!')
else:
    print('Você acertou a palavra. Parabèns!')

