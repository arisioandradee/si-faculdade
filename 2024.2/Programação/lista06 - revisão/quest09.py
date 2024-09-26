'''
Solicite ao usuário o número de dias em que ele pretende alugar um carro. O custo por dia é R$100. Se o 
aluguel for por mais de 7 dias, ele ganha um desconto de R$50 no total. Exiba o valor final a ser pago.
'''

qtdDias = int(input('Digite por quantos dias deseja alugar o carro: '))

custoDiario = 100.00

if  qtdDias > 7:
    valorComDesconto = (custoDiario * qtdDias) - 50
    print(f'O valor a ser pago com o desconto é: R${valorComDesconto:.2f}')
else:
    print(f'O valor a ser pago com o desconto é: R${qtdDias*custoDiario:.2f}')
