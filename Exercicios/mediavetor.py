vet = []
cont = soma = 0
N = int(input('Insira a quantidade de alunos: '))
for i in range(N):
    vet.append(int(input('Entre com um número: ')))
    soma += vet[i]
    cont += 1

if cont > 0:
    media = soma/cont
print('A média das notas dos alunos é: ',media)


