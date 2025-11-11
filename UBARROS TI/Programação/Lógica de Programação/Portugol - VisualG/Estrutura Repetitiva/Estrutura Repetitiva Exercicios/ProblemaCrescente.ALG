Algoritmo "ProblemaCrescente"


Var

   x, y : inteiro

Inicio

   escreval("Digite dois números : ")
   leia(x)
   leia(y)
   
   enquanto (x <> y) faca
      se y < x entao
        escreval("DECRESCENTE!")
      senao entao
        escreval("CRESCENTE!")
      fimse
      
      escreval("Digite dois números : ")
      leia(x)
      leia(y)
   fimenquanto


Fimalgoritmo