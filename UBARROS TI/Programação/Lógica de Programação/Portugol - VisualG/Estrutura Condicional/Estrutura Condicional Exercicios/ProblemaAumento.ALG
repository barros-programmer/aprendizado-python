Algoritmo "semnome"

Var

    salario, novoSalario, aumento : real
    porcentagem : real
    
Inicio

 escreval("Digite o salario da pessoa : ")
 leia(salario)
 
    se salario <= 1000 entao
       aumento := salario * 0.20
    senao
         se (salario > 1000) e (salario <= 3000) entao
         aumento := salario * 0.15
    senao
         se (salario > 3000) e (salario <= 8000) entao
         aumento := salario * 0.10
    senao
         se salario > 8000 entao
         aumento := salario * 0.05
         fimse
        fimse
      fimse
    fimse
 
   novoSalario := salario + aumento
   porcentagem := (aumento * 100) / salario

 escreval("Novo salario = ", novoSalario)
 escreval("Aumento = ", aumento)
 escreval("Porcentagem", porcentagem:0:2, "%")

Fimalgoritmo