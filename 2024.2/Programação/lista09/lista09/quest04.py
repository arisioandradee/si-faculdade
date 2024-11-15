'''
Um vendedor tem uma meta mínima de vendas de R$ 200,00 por dia e uma meta ideal de R$ 500,00.
Desenvolva um algoritmo que solicite ao usuário o valor das vendas diárias. Se ele não atingir a meta mínima,
exiba uma mensagem de incentivo. Se ele atingir a meta mínima, mas não a ideal, exiba uma mensagem de
motivação. E, se ele atingir a meta ideal, exiba uma mensagem de parabéns. Ao final, exiba o total das
vendas da semana (considere a semana de trabalho, os dias de segunda a sábado).
'''
total = 0
for i in range(0, 6):
    venda = float(input('Informe o valor da venda: '))
    total += venda

    if venda < 200:
        print('Você está quase conseguindo! Se esforçe um pouco mais!')
    elif venda >= 200 and venda < 500:
        print('Você realizou uma boa venda, mas pode melhorar!')
    else:
        print('Parabéns! Você atingiu a meta ideal!')

print(f'O valor total das suas vendas é: R${total:.2f}')