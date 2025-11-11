Algoritmo "semnome"



Var

preco, dinheiro, troco, resto : real
quantidade : inteiro


Inicio

escreval("Preço unitario do produto : ")
leia(preco)
escreval("Quantidade comprada : ")
leia(quantidade)
escreval("Dinheiro recebido : ")
leia(dinheiro)

 se dinheiro >= (preco * quantidade) entao
   troco <- preco * quantidade - dinheiro
     escreval("Troco = ", troco)
 senao
   resto <- preco * quantidade - dinheiro
     escreval("DINHEIRO INSUFICIENTE. FALTAM", resto:4:2 ," REAIS")
 fimse


Fimalgoritmo