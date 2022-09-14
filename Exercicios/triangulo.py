lado1 = int(input('Primeito número: '))
lado2 = int(input('Segundo número: '))
lado3 = int(input('Terceiro número: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 != lado2 != lado3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Esses valores não formam um triângulo')

