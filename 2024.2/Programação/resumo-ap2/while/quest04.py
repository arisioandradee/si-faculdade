'''
Desenvolva um algoritmo para um restaurante que solicite o gasto de cada pedido e classifique-os de acordo
com o seguinte:
I) Até R$ 15,00: lanche;
II) Acima de R$ 15,00 e até R$ 50,00: refeição simples.
III) Acima de R$ 50,00: refeição VIP.
O programa deve ficar acumulando os valores de cada tipo de pedido e informar, ao final, o total vendido de
cada um, assim que um comando de encerramento for inserido para este fim.
'''
lanche, refSimples, vip = 0,0,0

while True:
    gasto = float(input('Informe o gasto do pedido: '))
    print('OBS: Informe o 0 para encerrar o programa!')

    if gasto < 15:
        lanche += gasto
    elif gasto > 15 and gasto <= 50:
        refSimples += gasto
    else:
        vip += gasto

    if gasto == 0:
        break

print(f'LANCHES: {lanche:.2f} - REFEIÇÃO SIMPLES: {refSimples:.2f} - VIP: {vip:.2f}')