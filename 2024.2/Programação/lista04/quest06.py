'''
Um investidor aplica um valor e quer saber quanto terá após um período com juros simples. Peça o 
valor inicial, a taxa de juros ao ano e o número de anos. Calcule e exiba o valor final.
'''

valorInicial = float(input('Digite o valor inicial: '))
taxaAno = float(input('Digite a taxa anual: '))
qtdAno= float(input('Digite a quantidade de anos: '))

totalTaxa = taxaAno * qtdAno
valorFinal = valorInicial + totalTaxa

print(f'O valor final será R${valorFinal:.2f} reais.')