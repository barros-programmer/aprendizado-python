Algoritmo "semnome"

Var



Inicio

 escreval("Hora inicial : ")
 leia(x)   // x = hora inicial
 escreval("Hora final : ")
 leia(y)   // y = hora final
 
 se x < y entao
    duracao <- y - x
 senao
    duracao <- 24 - x + y
 fimse
 
 escreval("O JOGO DUROU ", duracao, " HORA(S)")

Fimalgoritmo