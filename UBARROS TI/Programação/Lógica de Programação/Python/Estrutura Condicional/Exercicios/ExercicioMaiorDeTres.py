x = int(input("Primeiro valor: "))
y = int(input("Segundo valor: "))
z = int(input("Terceiro valor: "))

if (x < y) and (x < z):
    print("Menor = {}".format(x))
elif (y < x) and (y < z):
    print("Menor = {}".format(y))
elif (z < x) and (z < y):
    print("Menor = {}".format(z))
elif x == y == z:
    print("Menor = {}".format(x))