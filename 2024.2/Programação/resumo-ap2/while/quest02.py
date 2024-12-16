'''
O banco GoodMoney precisa reajustar seu algoritmo de depósitos no caixa eletrônico. Você, enquanto
desenvolvedor da equipe, precisará criar um algoritmo, com o laço de repetição while, que solicite ao usuário
o saldo inicial de sua conta e pergunte se ele deseja realizar algum depósito. Caso o usuário informe que
deseja, o algoritmo deve solicitar o valor do depósito e, em seguida, mostrar o saldo atual. Após isso, o
usuário deverá ser perguntado se deja realizar outro depósito. Em caso positivo, o programa deve solicitar
novamente o valor do depósito e mostrar o saldo atual. O fluxo deverá se repetir até que o usuário informe
que não deseja mais realiazar qualquer depósito. Ao final, o algoritmo deve mostrar o saldo atual.
'''
saldo = 0

saldo = float(input('Informe o saldo em sua conta: '))

validacao = input('Você deseja realizar um depósito? (sim/nao)').lower()

while validacao != 'nao':
    deposito = float(input('Informe o valor do deposito: '))
    saldo += deposito

    validacao = input('Você deseja realizar um depósito? (sim/nao)').lower()

print(f'O seu saldo atual é R${saldo:.2f}')