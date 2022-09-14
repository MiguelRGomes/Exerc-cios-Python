def valorPagamento(valor, dias):
    if dias > 0:
        multa = valor * 0.03
        juros = dias * 0.1
        return round((valor + multa + juros), 2)

    return round(valor, 2)


def execution():
    execute = True
    resultado = 0
    resultadoTotal = 0
    count = 0
    while execute:
        valor = int(input("Digite um valor da prestação: "))

        if valor < 0:
            execute = False
            print("Erro, o valor não pode ser negativo")

        elif valor == 0:
            execute = False
            print("Quantidade parcelas " + str(count) + ", valor total de parcelas R$" + str(round(resultadoTotal, 2)))

        elif valor > 0:
            count += 1
            dias = int(input("Digite a quantidade de dias em atraso: "))
            resultado = valorPagamento(valor, dias)
            print("valor a ser pago " + str(resultado))
            resultadoTotal += resultado


execution()