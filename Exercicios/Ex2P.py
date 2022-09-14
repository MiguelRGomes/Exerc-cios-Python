opcao = 0
print("1. Calcule a área do triângulo")
print("2. Calcule a soma dos elementos pares")
print("3. Encontre os dois maiores números no vetor")
print("4. Sair")
opcao = int(input("Selecione a opção desejada: "))

while opcao < 4:
    if opcao == 1:
        base = 0
        altura = 0
        area = 0
        base = int(input("Digite a base do triângulo: "))
        altura = int(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print("A área do triângulo é: ", area)

    elif opcao == 2:
        vet = []
        soma = 0
        i = 0
        for i in range(50):
            vet.append(int(input('Informe um valor: ')))
            if vet[i] % 2 == 0:
                soma = soma + vet[i]
        print("A soma dos números pares é", soma)

    elif opcao == 3:
        vet = []
        soma = 0
        i = 0
        maior = 0
        maiordois = 0
        aux = 0
        for i in range(30):
            vet.append(int(input('Informe um valor: ')))
            if vet[i] > maior:
                maior = vet[i]

                if vet[i] != maior:
                    maior = vet[i]
                    aux = maior

        print("O primeiro maior número é", maior)
        print("O segundo maior número é", aux)









