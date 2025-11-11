codigoProduto = int(input("Codigo do produto comprado: "))

if codigoProduto == 1:
    quantidadeComprada = int(input("Quantidade comprada: "))
    valorPagar = quantidadeComprada * 5
    print("Valor a pagar : {}".format(valorPagar))
elif codigoProduto == 2:
    quantidadeComprada = int(input("Quantidade comprada: "))
    valorPagar = quantidadeComprada * 3.50
    print("Valor a pagar : {}".format(valorPagar))
elif codigoProduto == 3:
    quantidadeComprada = int(input("Quantidade comprada: "))
    valorPagar = quantidadeComprada * 4.80
    print("Valor a pagar : {}".format(valorPagar))
elif codigoProduto == 4:
    quantidadeComprada = int(input("Quantidade comprada: "))
    valorPagar = quantidadeComprada * 8.90
    print("Valor a pagar : {}".format(valorPagar))
elif codigoProduto == 5:
    quantidadeComprada = int(input("Quantidade comprada : "))
    valorPagar = quantidadeComprada * 7.32
    print("Valor a pagar : {}".format(valorPagar))
else:
    print("Codigo Invalido")