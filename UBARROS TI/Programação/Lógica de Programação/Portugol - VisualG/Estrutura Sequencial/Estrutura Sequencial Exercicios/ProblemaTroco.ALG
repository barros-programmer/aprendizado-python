Algoritmo "ProblemaTroco"



Var

 preco, dinheiro, troco : real
 quantidade : inteiro

Inicio
escreval("Preço unitário do produto: ")
    leia(preco)
    escreva("Quantidade comprada: ")
    leia(quantidade)
    escreva("Dinheiro recebido: ")
    leia(dinheiro)

    troco <- dinheiro - (quantidade * preco)

    escreval("TROCO = ",troco:4:2)


Fimalgoritmo