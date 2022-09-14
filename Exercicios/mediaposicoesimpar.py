vet = []
vet1 = []
cont = soma = 0
for i in range(3):
    vet.append(int(input('Entre com um número: ')))
    if (vet[i] % 2 == 0):
       vet1[i] += vet[i]
    else:
    soma += vet[i]
    cont += 1

if cont > 0:
    media = soma/cont
print('A média das notas dos alunos é: ',media)


