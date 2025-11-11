# Faça um programa que peça o nome do usuário.
# Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"
# Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"
# Se for maior que 6 escreva "Seu nome é muito grande"

nome = str(input("Digite o seu nome: "))
letras_nome = (len(nome))

if letras_nome <= 4:
    print("Seu nome é curto.")
elif (letras_nome >= 5) and (letras_nome <= 6):
    print("Seu nome é normal.")
elif letras_nome >= 7:
    print("Seu nome é grande")