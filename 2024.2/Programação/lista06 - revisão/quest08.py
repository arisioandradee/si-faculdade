'''
Desenvolva um algoritmo que solicite o valor do salário mensal do usuário. Se for maior que R$5.000,00,
calcule um imposto de 20%. Caso contrário, calcule 10%. Exiba o valor do imposto
'''

salario = float(input('Digite seu salário mensal: '))

if salario > 5000.0:
    imposto = salario * 0.20
    print(f'O valor do imposto é: R${imposto}.')
else:
    imposto = salario * 0.10
    print(f'O valor do imposto é: R${imposto}.')