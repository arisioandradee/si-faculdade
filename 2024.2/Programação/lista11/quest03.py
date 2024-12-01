nomes = []
consumos = []
acimaDaMedia = []

quantidade = int(input('Infome a quantidade de meses para realizar a consulta: '))

for i in range(quantidade):
    nome = input('Informe o nome do mês: ')
    consumo = float(input('Informe a quantidade de consumo: '))

    nomes.append(nome)
    consumos.append(consumo)

media = sum(consumos) / len(consumos)

for i in range(quantidade):
    if consumos[i] > media:
        acimaDaMedia.append((nomes[i], consumos[i]))

print(f'MESES A CIMA DA MÉDIA: ')
for mes, consumo in acimaDaMedia:
    print(f'{mes}: {consumo}')