'''
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.
'''
# Programa para converter segundos em horas:minutos:segundos

segundos = int(input("Digite a duracao em segundos: "))

horas = segundos // 3600            # 1 hora = 3600 segundos
resto = segundos % 3600             # o que sobra depois de tirar as horas
minutos = resto // 60               # 1 minuto = 60 segundos
segundos_finais = resto % 60        # o que sobra são os segundos

print(f"{horas}:{minutos}:{segundos_finais}")
