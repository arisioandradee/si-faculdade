'''
Desenvolva um algoritmo que solicite a idade do usuário. Verifique se ele é maior de 18 anos para 
determinar se pode obter uma carteira de habilitação. Em seguida, mostre em tela se, de acordo com a 
idade, ele pode ou não, iniciar o processo de habilitação.
'''

idade = int(input('Digite sua idade: '))

if idade > 18:
    print('Você pode iniciar o processo de habilitação!')
else:
    print('Você não pode iniciar o processo de habilitação!')