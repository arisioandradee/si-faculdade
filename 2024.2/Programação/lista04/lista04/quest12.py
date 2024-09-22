'''
Peça ao usuário para informar a largura e o comprimento de um terreno, assim como o preço total 
do terreno. Calcule e exiba o preço por metro quadrado
'''

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite a comprimento do terreno: '))
valorTerreno = float(input('Digite o valor total do terreno: '))

valorPorMetro = valorTerreno / (largura * comprimento)

print(f'O valor por m² é R${valorPorMetro} reais.')