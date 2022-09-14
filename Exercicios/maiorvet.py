vet = []
cont = maior = 0
for i in range(3):
    vet.append(int(input('Informe um valor: ')))
    cont += 1
    if cont == 1:
        maior = vet[i]
    else:
        if vet[i] > maior:
            maior = vet[i]

print('O maior número é: ',maior)