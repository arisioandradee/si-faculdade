'''
Peça ao usuário para digitar seu peso em quilogramas e sua altura em metros. Calcule e exiba o 
Índice de Massa Corporal (IMC) usando a fórmula IMC = peso / altura²
'''

peso = float(input('Digite sua peso em kilos: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso * (altura ** 2)

print(f'O seu IMC è: {imc:.2f}')