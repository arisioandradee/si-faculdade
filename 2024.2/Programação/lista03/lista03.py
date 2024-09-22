#1 Desenvolva um algoritmo que solicite ao usuário para digitar os coeficientes “a”, “b” e “c” de uma 
#equação do segundo grau. Calcule e mostre em tela o valor do delta (Δ = b² − 4*a*c)
a = int(input('Digite o valor do coeficiente A: '))
b = int(input('Digite o valor do coeficiente B: '))
c = int(input('Digite o valor do coeficiente C: '))

delta =  (b**2) - 4 * a * c
print(f'O resultado da equação de segundo grau é: {delta}')
print('')

#2) Desenvolva um algoritmo que peça ao usuário para digitar a temperatura em graus Celsius. Calcule 
#e mostre em tela a temperatura equivalente em Fahrenheit. Dica: Use a fórmula F = (C * 1,8) + 32.
tempCelcius = float(input('Digite a temperatura em graus Celcius: '))
tempFah = (tempCelcius * 1.8) + 32
print(f'O valor convertido para Fahrenheit é: {tempFah}°F')
print('')

#3) Desenvolva um algoritmo que solicite ao usuário para digitar o valor de um produto em dólares e a 
#taxa de câmbio atual. Calcule e mostre em tela o valor do produto em reais.

valorDolar = float(input('Digite o valor do produto em dólares: '))
taxaCambio = float(input('Digite a taxa de câmbio atual: '))
valorReal = valorDolar * taxaCambio
print(f'O valor convertido é: R${valorReal:.2f} reais')     
print('')

#4) Desenvolva um algoritmo que peça ao usuário para digitar a quantidade de litros de combustível 
#comprados e o preço por litro. Calcule e mostre em tela o valor total pago
qtdLitros = float(input('Digite a quantidade de litros comprados: '))
valorLitro = float(input('Digite o valor do litro: '))
valorFinal = qtdLitros * valorLitro
print(f'O valor da compra foi: R${valorFinal:.2f} reais.')
print('')

#Desenvolva um algoritmo que solicite ao usuário para digitar a capacidade de um tanque de 
#combustível e o consumo médio de combustível de um veículo (km por litro). Calcule e mostre em 
#tela a autonomia do veículo (quantos quilômetros ele pode percorrer com um tanque cheio).
capacidadeTanque = float(input('Digite a capacidade total do tanque: '))
consumoMedio = float(input('Digite o consumo médio do veículo(km/litro): '))
autonomia = capacidadeTanque / consumoMedio
print(f'O veículo pode percorrer {autonomia:.2f}km com o tanque cheio.')
print('')

#6) Desenvolva um algoritmo que peça ao usuário para digitar a quantidade de quilômetros percorridos 
#por um veículo e o tempo gasto na viagem em horas. Calcule e mostre em tela a velocidade média 
#do veículo em km/h
qtdKm = float(input('Digite a quantidade de km percorrido pelo veículo: '))
tempoGasto = float(input('Digite o tempo gasto na viagem(em horas):'))
velocidadeMedia = qtdKm / tempoGasto
print(f'A velocidade média durante a viagem foi de {velocidadeMedia:.2f}km/h.')