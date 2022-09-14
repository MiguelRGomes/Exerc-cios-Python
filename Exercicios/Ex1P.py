nome = input("Digite o seu nome: ")
salario = float(input("Digite o valor do seu salário: "))
filhos = int(input("Digite a quantidade de filhos: "))

if salario < 0:
    execute = False
    print("Erro, o salário não pode ser negativo!")

elif filhos == 0:
    resultadoTotal = salario + (salario * 0.1)
    print(nome)
    print("Parabéns! O seu novo salário é R$ ",resultadoTotal)

elif filhos == 1 or filhos == 2:
    resultadoTotal = salario + (salario * 0.2)
    print(nome)
    print("Parabéns! O seu novo salário é R$ ",resultadoTotal)

else:
    resultadoTotal = salario + (salario * 0.25)
    print(nome)
    print("Parabéns! O seu novo salário é R$ ",resultadoTotal)
