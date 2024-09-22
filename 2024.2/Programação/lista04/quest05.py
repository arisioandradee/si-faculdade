'''
Uma pessoa vende um produto com uma margem de lucro. Peça ao usuário para informar o custo 
do produto e a porcentagem de lucro que deseja. Calcule e exiba o preço de venda.
'''

custoProduto = float(input('Digite o custo do produto: '))
margem = float(input('Digite a margem que deseja aplicar ao produto: '))

valorDeVenda = custoProduto + (custoProduto * (margem / 100))
print(f'O valor de venda do produto é: R${valorDeVenda:.2f} reais.')