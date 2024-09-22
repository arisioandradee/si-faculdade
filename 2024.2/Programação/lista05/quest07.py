'''
Peça ao usuário para inserir o valor de um pedido. Se o valor for menor que R$50, adicione uma taxa de 
entrega de R$10. Exiba o valor total.
'''

valor = float(input('Digite o valor do pedido: '))

if valor < 50:
    valor_total = valor + 10
    print(f'O valor inicial era R${valor:.2f}, porém com a taxa de entrega ficou R${valor_total:.2f}')
else:
    print(f'O valor do pedido ficou R${valor:.2f}, sem taxas')
