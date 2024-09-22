'''
Um pintor deseja calcular o custo de pintar uma parede. Peça ao usuário para digitar a altura e a 
largura da parede em metros, e o preço por metro quadrado da pintura. Calcule e exiba o custo total 
da pintura
'''

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
valorMetro = float(input('Digite o valor da pintura por m²: '))

metroQuadrado = altura * largura
valorTotal = valorMetro * metroQuadrado

print(f'O valor total para pintar a parede é R${valorTotal} reais.')