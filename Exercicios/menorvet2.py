def menor_valor(vet, N):
    menor = vet[0]
    for i in range(1,N):
        if vet[i] < menor:
            menor = vet[i]
    return menor

vet = []
N = int(input('Digite a quantidade de elementos do vetor: '))
for i in range(N):
    vet.append(int(input('Digite um número: ')))

menor = menor_valor(vet, N)
print('O menor elemento do vetor é %d' %menor)