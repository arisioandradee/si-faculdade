'''
Um organizador de festas quer calcular o custo total de um evento. Peça ao usuário para digitar o 
número de convidados e o custo por convidado. Calcule e exiba o custo total da festa.
'''

qtdConvidados = int(input('Digite a quantidade de convidados: '))
custoConvidado = float(input('Digite o custo por convidado: '))
valorTotal = qtdConvidados * custoConvidado
print(f'O valor total da festa é: R${valorTotal:.2f} reais.')