Algoritmo "semnome"


Var

primeiraNota, segundaNota, notaFinal : real

Inicio

escreval("Digite a primeira nota : ")
leia(primeiraNota)

escreval("Digite a segunda nota : ")
leia(segundaNota)

notaFinal <- primeiraNota + segundaNota

escreval("NOTA FINAL : ", notaFinal:5:1)

  se notaFinal >=60 entao
    escreva("Aprovado!")
      senao entao
        escreva("Reprovado!")
     fimse

// Poderiamos usar na linha 20, senao <=60 entao, mas para simplificar, usamos isso que coloquei para evitar muitas palavras e tirar mais um fimse do algoritimo

Fimalgoritmo