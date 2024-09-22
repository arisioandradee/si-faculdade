'''
Um banco oferece um empréstimo com juros simples. Peça ao usuário para digitar o valor do 
empréstimo, a taxa de juros ao mês, e o número de meses. Calcule e exiba o valor final a ser pago.
'''

valorEmprestimo = float(input('Digite o valor do empréstimo: '))
taxaPorMes = float(input('Digite a taxa mensal do empréstimo(%): '))
qtdMeses = float(input('Digite a quantidade de meses do empréstimo: '))

juros = (taxaPorMes * qtdMeses)
valorFinal = valorEmprestimo + juros

print(f'O valor final do emprestimo será: R${valorFinal:.2f} reais.')
