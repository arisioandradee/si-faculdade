quantidade = int(input('Informe quantos produtos deseja registrar: '))

nomes = []
quantidades = []

for i in range(quantidade):
    nome = input(f'Informe o nome do {i+1}° produto: ')
    quantidade = int(input(f'Informe a quantidade do {i+1}° produto: '))

    nomes.append(nome)
    quantidades.append(quantidade)

maiorQuantidade = quantidades.index(max(quantidades))

print(f'O produto com mais quantidades em estoque é o {nomes[maiorQuantidade]}, com {quantidades[maiorQuantidade]} unidades!')
