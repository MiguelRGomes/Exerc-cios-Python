import statistics

vet = []

for i in range(10):
    vet.append(int(input('Digite 10 números para poder qual é a MODA: ')))
    moda = statistics.mode(vet)

print('Os números digitados foram: ', vet)
print('A MODA do vetor é: ', moda)



