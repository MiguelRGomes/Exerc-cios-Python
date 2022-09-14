vet = []
par = []
impar = []

for i in range(5):
    vet.append(int(input('Informe um valor: ')))
    if vet[i] % 2 == 0:
        par.append(vet[i])
    else:
        impar.append(vet[i])

print('Os números pares são: ',par)
print('Os números ímpares são: ',impar)





if cont > 0:
    media = soma/cont
print('A média das notas dos alunos é: ',media)


