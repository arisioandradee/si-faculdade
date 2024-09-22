'''
Em um restaurante, o cliente pode dar uma gorjeta opcional de 10% sobre o valor da conta. Peça 
ao usuário para informar o valor da conta e calcule o total com a gorjeta.
'''

valorConta = float(input('Digite o valor da conta: '))
gorjeta = valorConta * 0.10

print(f'O valor da gorjeta com 10% será: R${gorjeta}')
