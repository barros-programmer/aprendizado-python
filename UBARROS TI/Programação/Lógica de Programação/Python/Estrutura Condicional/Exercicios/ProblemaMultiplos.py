numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

if numero1 % numero2 == 0 or numero2 % numero1 == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")