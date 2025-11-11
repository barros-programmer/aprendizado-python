nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

notaTotal = nota1 + nota2

if notaTotal >= 60:
    print("Passou de ano!")
elif notaTotal < 60:
    print("Reprovou.")