'''
Um motorista deseja calcular o custo total de uma viagem. Peça ao usuário para informar a 
distância a ser percorrida (em km), o consumo do carro (km/l) e o preço do combustível. Calcule e 
exiba o custo total.
'''

distancia = float(input('Digite a distância a ser percorrida(em km): '))
consumo = float(input('Digite o consumo do carro(km/l): '))
valorCombustivel = float(input('Digite o valor do combustivel: '))

totalLitros = distancia / consumo
valorTotal = totalLitros * valorCombustivel
print(f'O custo total da viagem será R${valorTotal:.2f} reais.')