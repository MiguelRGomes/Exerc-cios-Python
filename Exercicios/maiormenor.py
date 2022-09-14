vet = []
cont = maior = menor = 0
for i in range(3):
    vet.append(int(input('Informe um valor: ')))
    cont += 1
    if cont == 1:
        maior = menor = vet[i]
    else:
        if vet[i] > maior:
            maior = vet[i]
        if vet[i] < menor:
            menor = vet[i]

print('O menor número é: ',menor)
print('O maior número é: ',maior)





if cont > 0:
    media = soma/cont
print('A média das notas dos alunos é: ',media)


