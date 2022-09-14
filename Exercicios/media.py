"""Construa um programa que calule a média aritmética de um conjunto de numeros pares fornecidos pelo usario.
O usuário irá fornecer um total de 10 números."""

cont = soma = 0

for i in range(10):
    n = int(input('Digite um número: '))
    if n%2 == 0:
        soma += n
        cont += 1

if cont > 0:
    media = soma/cont
    print('A média é %.1f' %media)
else:
    print('Nenhum número par foi digitado')