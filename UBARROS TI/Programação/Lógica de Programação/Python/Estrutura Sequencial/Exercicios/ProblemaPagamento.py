'''
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa
'''

nome = str(input("Nome: "))
valorPorHora = float(input("Valor por hora: "))
horasTrabalhadas = int(input("Horas trabalhadas: "))

pagamento = valorPorHora * horasTrabalhadas

print(f"O pagamento para {nome} deve ser R${pagamento}")