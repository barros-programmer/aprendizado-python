Algoritmo "semnome"




Var

   preco, dinheiro, troco, total : real
   quantidade,codigo : inteiro
   nome1, nome2, opcao : caractere
   // Nome1 é do atendente e Nome2 é do cliente
   
Inicio



    // Boas Vindas ao Sistema
    escreval("Olá atendente, bem vindo a Mercearia Cesar. Informe seu nome: ")
    leia(nome1)
    escreval("Agora seu código de funcionario.")
    leia(codigo)
    escreva("Olá Atendente ", nome1," com o código", codigo, " o que deseja fazer?")
    escreval

    // Menu de Opções
    escreval("1-Pagamento")
    escreval("2-Sair")
    leia(opcao)
    
    // Condicional Para Escolha da Ação
    escolha opcao
    caso "1"
    
    // Processo de pagamento
    escreval("Informe o nome do cliente: ")
      leia(nome2)
      escreval("Digite o preço do produto: R$")
      leia(preco)
      escreval("Digite a quantidade comprada: ")
      leia(quantidade)
      
    // Calculando o total
    total <- preco * quantidade
    escreval("O valor total é: R$", total:0:2)

    // Recebendo pagamento
    escreval("Informe o valor em dinheiro recebido: R$")
    leia(dinheiro)
    
    // Verificando se o dinheiro é suficiente
    se dinheiro >= total entao
    troco <- dinheiro - total
    escreval("Troco a ser devolvido: R$", troco:0:2)
    escreval("Pagamento realizado com sucesso!")
    senao
    escreval("Dinheiro insuficiente. Por favor, peça mais dinheiro ao cliente.")
    fimse
    
    // Caso 2
    caso "2"
    escreval("Encerrando o sistema. Obrigado por usar a Mercearia Cesar!")
    outrocaso
    escreval("Opção inválida. Tente novamente.")
   fimescolha



Fimalgoritmo