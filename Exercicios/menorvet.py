vet = []
cont = menor = 0
for i in range(3):
    vet.append(int(input('Informe um valor: ')))
    cont += 1
    if cont == 1:
        menor = vet[i]
    else:
        if vet[i] < menor:
            menor = vet[i]

print('O menor número é: ',menor)