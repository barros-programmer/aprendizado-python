quantidadeMinutos = int(input("Digite a quantidade de minutos: "))
planoBasico = 50

if quantidadeMinutos <= 100:
    print("Valor a pagar = R${}".format(planoBasico))
elif quantidadeMinutos > 100:
    valorExcedido = (quantidadeMinutos - 100) * 2 + 50
    print("Valor a pagar = R${}".format(valorExcedido))