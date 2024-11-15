'''
Desenvolva um algoritmo que solicite ao usuário o saldo de sua conta corrente. Em seguida, o algoritmo
deve perguntar quantos depósitos ele deseja efetuar. Logo após, solicite o valor de cada depósito e exiba o
saldo total ao final dos depósitos.
'''
total = 0

saldo = float(input('Informe o saldo da sua conta(R$): '))
quantidade = int(input('Informe a quantidade de depositos que deseja efetuar: '))

for i in range(0, quantidade):
    valor = float(input('Informe o valor do deposito: '))
    total += valor

print(f'Seu saldo final é: R${total + saldo:.2f}')