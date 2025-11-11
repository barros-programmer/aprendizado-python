precoUnitario = float(input("Preço unitário do produto: "))
quantidadeComprada = int(input("Quantidade comprada: "))
dinheiroRecebido = float(input("Dinheiro recebido: "))

totalCompra = precoUnitario * quantidadeComprada
troco = dinheiroRecebido - totalCompra

if troco >= 0:
    print("TROCO = R${}".format(troco))
elif troco == 0:
    print("Dinheiro Suficiente")
else:
    falta = totalCompra - dinheiroRecebido
    print("Dinheiro insuficiente. Faltam R${}".format(falta))