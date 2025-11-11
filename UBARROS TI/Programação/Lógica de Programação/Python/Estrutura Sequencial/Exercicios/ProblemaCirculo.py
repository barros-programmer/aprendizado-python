'''
Fazer um programa para ler o valor "r" do raio de um círculo, e depois mostrar o valor da área do
círculo com três casas decimais. A fórmula da área do círculo é a seguinte: 𝑎𝑟𝑒𝑎 = 𝜋. 𝑟
ଶ
. Você pode
usar o valor de 𝜋 fornecido pela biblioteca da sua linguagem de programação, ou então, se preferir, use
diretamente o valor 3.14159
'''

raio = float(input("Digite o valor do raio do circulo: "))
pi = 3.14159
areaCirculo = pi * raio ** 2

print(f"AREA = {areaCirculo:.3f}")