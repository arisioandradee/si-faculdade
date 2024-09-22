'''
Solicite o peso e a altura do usuário e calcule o Índice de Massa Corporal (IMC). Classifique o IMC de 
acordo com as faixas: abaixo do peso (<18.5), peso normal (18.5 a 24.9), sobrepeso (25 a 29.9), e 
obesidade (>=30)
'''

peso =  float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): ')) 

imc = peso * (altura ** 2)

if imc < 18.5:
    print('A baixo do peso!')
elif imc >= 18.5 and imc < 24.9:
    print('Peso normal!')
elif imc >= 25 and imc <= 29.9:
    print('A cima do peso!')
else: 
    print('Obesidade!')