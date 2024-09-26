'''
Desenvolva um algoritmo que peça ao usuário para inserir o peso de um pacote. Se o peso for superior a 
5kg, cobre R$50 de frete. Caso contrário, cobre R$20.
'''

pesoPacote = float(input('Insira o peso do pacote(kg): '))

if pesoPacote > 5.0:
    print('Será cobrada uma taxa de frete de R$50.00.')
else:
    print('Será cobrada uma taxa de frete de R$20.00.')