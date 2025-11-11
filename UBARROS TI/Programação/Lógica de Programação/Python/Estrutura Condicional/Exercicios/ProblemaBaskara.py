import math

a = float(input("Coeficiente A: "))
b = float(input("Coeficiente B: "))
c = float(input("Coeficiente C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Essa equação não possui raízes reais 😢")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("X1 = {:.2f}".format(x1))
    print("X2 = {:.2f}".format(x2))