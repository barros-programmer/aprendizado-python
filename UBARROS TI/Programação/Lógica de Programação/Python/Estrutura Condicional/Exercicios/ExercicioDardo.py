distancia1 = float(input("Digite a primeira distancia: "))
distancia2 = float(input("Digite a segunda distancia: "))
distancia3 = float(input("Digite a terceira distancia: "))

if (distancia1 > distancia2) and (distancia1 > distancia3):
    maior = distancia1
    print("MAIOR DISTANCIA = {}".format(distancia1))
elif (distancia2 > distancia1) and (distancia2 > distancia3):
    maior = distancia2
    print("MAIOR DISTANCIA = {}".format(distancia2))
elif (distancia3 > distancia1) and (distancia3 > distancia2):
    maior = distancia3
    print("MAIOR DISTANCIA = {}".format(distancia3))

