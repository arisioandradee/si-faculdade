'''
Solicite ao usuário o valor de um produto e sua categoria (1 para alimentação, 2 para vestuário, 3 para 
eletrônicos). Aplique uma taxa de imposto: 5% para alimentação, 10% para vestuário e 20% para 
eletrônicos. Exiba o valor final com imposto
'''

print('Categorias:')
print('  1- Alimentação')
print('  2- Vestuário')
print('  3- Eletrônicos') 
print('')

valor = float(input('Digite o valor do produto: '))
categoria = int(input('Digite o número correspondente a categoria: '))

if categoria == 1:
    valorComImposto = valor + valor * 0.05
    print(f'O valor com o imposto é: R${valorComImposto:.2f}')
elif categoria == 2:
    valorComImposto =  valor + valor * 0.10
    print(f'O valor com o imposto é: R${valorComImposto:.2f}')
elif categoria == 3:
    valorComImposto =  valor + valor * 0.20
    print(f'O valor com o imposto é: R${valorComImposto:.2f}')
else:
    print('Categoria inválida!')