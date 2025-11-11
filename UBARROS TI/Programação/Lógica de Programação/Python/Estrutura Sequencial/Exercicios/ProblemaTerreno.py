'''
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular, bem como o valor do metro quadrado do terreno. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais.
'''

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimenton do terreno: "))
valor_metroQuadrado = float(input("Digite o valor do metro quadrado: "))

valorArea = largura * comprimento
preco_do_terreno = valor_metroQuadrado * valorArea

print(f"Valor da área do terreno: {valorArea:.2f}R$")
print(f"Preço do terreno: {preco_do_terreno:.2f}R$")