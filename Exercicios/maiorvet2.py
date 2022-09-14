def maior_valor(vet, N):
    maior = vet[0]
    for i in range(1,N):
        if vet[i] > maior:
            maior = vet[i]
    return maior

vet = []
N = int(input('Digite a quantidade de elementos do vetor: '))
for i in range(N):
    vet.append(int(input('Digite um número: ')))

maior = maior_valor(vet, N)
print('O maior elemento do vetor é %d' %maior)