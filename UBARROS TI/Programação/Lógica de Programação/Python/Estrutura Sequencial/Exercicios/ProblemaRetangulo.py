'''
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais
'''
import math

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = math.sqrt((perimetro / 2) ** 2 - (2 * area))

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
