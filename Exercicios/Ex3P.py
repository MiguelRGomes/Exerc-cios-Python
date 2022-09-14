idade = []
altura = []
cont = soma = 0

for i in range(40):
    idade.append(int(input('Informe sua idade: ')))
    altura.append(int(input('Informe sua altura: ')))
    soma += altura[i]
    media = soma / 3
    if idade[i] > 25:
        if media > altura[i]:
            cont = cont + 1
print("A média das altura é ", media)
print("A seguir está a quantidade de pessoas com altura menor que a média ", cont)








