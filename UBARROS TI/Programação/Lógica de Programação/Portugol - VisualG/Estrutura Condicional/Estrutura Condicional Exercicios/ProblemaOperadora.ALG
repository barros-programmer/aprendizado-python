Algoritmo "semnome"



Var

minutos : inteiro
valorPago : real

Inicio

escreva("Quantidade de minutos : ")
leia(minutos)

valorPago <- 50
 se minutos > 100 entao
   valorPago <- valorPago + 2 * (minutos - 100)
 fimse
 
escreval("Valor a pagar : ",valorPago:4:2)



Fimalgoritmo