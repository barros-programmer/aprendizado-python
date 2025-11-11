Algoritmo "semnome"




Var

  primeiroValor, segundoValor, terceiroValor, menor : inteiro

Inicio

escreval("Primeiro valor : ")
leia(primeiroValor)
escreval("Segundo Valor : ")
leia(segundoValor)
escreval("Terceiro Valor : ")
leia(terceiroValor)

   se (primeiroValor < segundoValor) e (primeiroValor < segundoValor) entao
   menor <- primeiroValor
   
   senao
     se segundoValor < terceiroValor entao
       menor <- segundoValor
     senao
       menor <- terceiroValor
     fimse
   fimse
   
escreval("MENOR = ", menor)


Fimalgoritmo