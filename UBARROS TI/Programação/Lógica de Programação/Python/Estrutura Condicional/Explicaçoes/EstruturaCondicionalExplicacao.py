# Estrutura condicional (if, elif, else) é usada para tomar decisões no código.
# O programa verifica se uma condição é verdadeira (True) e executa um bloco de comandos.
# - if: executa se a condição for verdadeira.
# - elif: usado para testar outra condição caso o if anterior seja falso.
# - else: executa se nenhuma das condições anteriores for verdadeira.
#
# Exemplo de estrutura condicional em Python

idade = int(input("Digite sua idade: "))

# Estrutura condicional decide o que fazer dependendo da idade informada
if idade >= 18:
    print("Você é maior de idade.")
elif idade > 0:
    print("Você é menor de idade.")
else:
    print("Idade inválida.")



