# Estrutura repetitiva (laços de repetição) é usada quando precisamos executar
# um bloco de código várias vezes de forma automática.
#
# No Python, temos principalmente dois tipos:
#
# 1. while (enquanto):
#    - Repete enquanto a condição for verdadeira.
#    - Usado quando NÃO sabemos quantas vezes vamos repetir.
#
# 2. for (para):
#    - Repete um número definido de vezes.
#    - Usado quando JÁ sabemos quantas repetições queremos.
#
# Exemplo de repetição com while

while True:
    idade = int(input("Digite sua idade (ou um número negativo para sair): "))

    if idade < 0:
        print("Programa encerrado.")
        break  # Encerra o laço
    elif idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

# Exemplo de repetição com for

quantidade = int(input("Quantas pessoas você quer verificar? "))

for i in range(quantidade):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    if idade >= 18:
        print("Maior de idade.")
    elif idade > 0:
        print("Menor de idade.")
    else:
        print("Idade inválida.")
