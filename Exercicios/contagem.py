aux1 = 2
aux2 = 3.0
soma = 0
num = 0

while aux1 <= num:
        print (aux1, aux2)
        soma += aux1/aux2
        aux1 = aux1 + 1
        aux2 = aux2 + 2

num = input('Digite um valor: ')
while num < 0:
    num = input('Digite um valor positivo: ')
print (res)