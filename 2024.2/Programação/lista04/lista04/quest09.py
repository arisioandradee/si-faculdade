'''
Peça ao usuário para digitar uma quantidade de dias e converta para horas, minutos e segundos. 
Mostre em tela, quantas horas, minutos e segundos, contém nos dias que o usuário digitou.
'''

qtdDias = int(input('Digite a quantidade de dias: '))

qtdHoras = qtdDias * 24
qtdMinutos = qtdHoras * 60
qtdSegundos = qtdMinutos *60

print(f'{qtdDias} dias equivalem a {qtdHoras} horas, {qtdMinutos:.2f} minutos e {qtdSegundos:.2f} segundos!')