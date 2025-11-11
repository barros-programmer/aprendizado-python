"""
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C 
"""

medida_A = float(input("Digite a medida A: "))
medida_B = float(input("Digite a medida B: "))
medida_C = float(input("Digite a medida C: "))

area_quadrado = medida_A ** 2
area_trianguloRetangulo = (medida_A * medida_B) / 2
area_trapezio = (medida_A + medida_B) * medida_C / 2

print(f"AREA DO QUADRADO = {area_quadrado:.4f}")
print(f"AREA DO TRIANGULO = {area_trianguloRetangulo:.4f}")
print(f"AREA DO TRAPEZIO = {area_trapezio:.4f}")



