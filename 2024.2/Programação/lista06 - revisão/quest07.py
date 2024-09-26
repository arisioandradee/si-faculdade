'''
Solicite o valor total de uma compra ao usuário. Se o valor for maior que R$200, aplique um desconto de 
20%. Se for entre R$100 e R$200, aplique 10%. Caso contrário, não aplique desconto. Exiba o valor final.
'''

valorCompra = float(input('Digite o valor da compra: '))

if valorCompra > 200:
    desconto = valorCompra - valorCompra * 0.20
    print(f'Você recebeu um desconto de 20%! Valor final: {desconto:.2f}')
elif valorCompra >= 100 and valorCompra <= 200:
    desconto = valorCompra - valorCompra * 0.10
    print(f'Você recebeu um desconto de 10%! Valor final: {desconto:.2f}')
else:
    print('Não foi aplicado desconto em cima da compra!')