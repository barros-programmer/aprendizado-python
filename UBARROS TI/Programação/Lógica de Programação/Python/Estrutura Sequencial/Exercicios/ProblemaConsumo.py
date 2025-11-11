'''
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais. 
'''

distancia_percorrida = float(input("Distancia percorrida: "))
combustivel_gasto = float(input("Combustivel gasto: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Consumo médio = {consumo_medio:.3f}")