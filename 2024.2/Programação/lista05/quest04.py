'''
Peça ao usuário para inserir o valor de uma compra. Se o valor for maior que R$100, aplique um desconto 
de 10%. Caso contrário, não aplique desconto. Exiba o valor final da compra.
'''

valor = float(input('Digite o valor da compra: '))

if valor > 100:
    desconto = 100 - (valor * 0.10)
    print(f'Você recebeu um desconto de 10%! O valor do produto agora é R${desconto:.2f}')
else:
    print(f'Infelizmente o valor de R${valor:.2f} não foi o suficiente para ganhar o desconto!')