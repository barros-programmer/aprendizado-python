temperatura = str(input("Voce vai digitar a temperatura em qual escala (C/F)? "))
if temperatura == "F":
    temperaturaF = float(input("Digite a temperatura em Fahrenheit: "))
    temperaturaC = (temperaturaF - 32) * 5 / 9
    print("Temperatura equivalente em Celsius: {:.1f}".format(temperaturaC))
elif temperatura == "C":
    temperaturaC = float(input("Digite a temperatura em Celsius: "))
    temperaturaF = (temperaturaC * 9 / 5) + 32
    print("Temperatura equivalente em Fahrenheit: {:.1f}".format(temperaturaF))