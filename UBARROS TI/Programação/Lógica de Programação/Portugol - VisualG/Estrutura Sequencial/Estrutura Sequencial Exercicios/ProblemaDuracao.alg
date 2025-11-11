Algoritmo "semnome"



Var

duracao, horas, resto, minutos, segundos : inteiro


Inicio

escreval("Digite a duracao em segundos : ")
leia(duracao)

horas <- duracao \ 3600
resto <- duracao mod 3600

minutos <- resto \ 60
segundos <- resto mod 60


escreval(horas, ":", minutos, ":", segundos)


Fimalgoritmo
// 1 minuto = 60 segundos
// 1 hora = 60 minutos
// 1 hora = 3600 segundos