#Função que soma os elementos de um vetor
def soma(vet):
    s = 0
    for i in range(5):
        s += vet[i]
    return s

#Função que calcula a média dos elementos de um vetor
def calc_media(vet):
    s = soma(vet)
    med = s/5
    return med

vet = []
for i in range(5):
    vet.append(int(input('Numero: ')))

resp = soma(vet)
print('A soma é %d' %resp)

m = calc_media(vet)
print('A média é %.2f' %m)