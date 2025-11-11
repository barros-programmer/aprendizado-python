
# FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO INTEIRO, INFORME SE ESSE NÚMERO É PAR OU ÍMPAR.
# CASO O USUÁRIO NÃO DIGITE UM NÚMERO INTEIRO, INFORME QUE NÃO É UM NÚMERO INTEIRO.

numero_str = str(input("Digite um número inteiro: "))

try:
    numero = int(numero_str)

    if numero % 2 == 0:
        print("NÚMERO PAR")
    else:
        print("NÚMERO ÍMPAR")
except ValueError:
    print("Nao é um numero inteiro")