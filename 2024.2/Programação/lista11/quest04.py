'''
Um site de comparação de preços de produtos deseja contratar você para desenvolver um programa.
Primeiramente, o algoritmo deverá solicitar quantos produtos o usuário deseja comparar. Em seguida, o
usuário deve digitar o nome do produto e o preço encontrado em duas lojas. Ao final, o programa deverá
informar, para cada produto, qual loja ele está com o preço menor.
'''
nomes = []
valoresLoja1 = []
valoresLoja2 = []
menorValor = []

quantidade = int(input('Informe quantos produtos deseja comprar: '))

for i in range(quantidade):
    nome = input(f'Infome o nome do {i+1}° produto: ')
    valorLoja1 = float(input(f'Informe o valor do produto na Loja 1: '))
    valorLoja2 = float(input(f'Informe o valor do produto na Loja 2: '))

    nomes.append(nome)
    valoresLoja1.append(valorLoja1)
    valoresLoja2.append(valorLoja2)

    if valorLoja1 < valorLoja2:
        menorValor.append((nome,'Loja 1', valorLoja1))
    else:
        menorValor.append((nome,'Loja 2', valorLoja2))

for nome, loja, valor in menorValor:
    print(f'O produto "{nome}" está mais barato na {loja} por R${valor:.2f}')