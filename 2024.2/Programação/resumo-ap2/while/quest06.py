'''
Desenvolva um algoritmo que solicite o consumo de dados em GB e aplique as seguintes tarifas:
I) R$ 5,00 por GB para até 10 GB.
II) R$4,00 por GB acima de 10 e até 30 GB.
III) R$3,00 por GB acima de 30 GB.
O programa deve mostraro valor total da conta e continuar perguntando se o usuário deseja realizar outro
cálculo de tarifas até que algum comando seja inserido para o encerramento.
'''

validacao = input('Deseja ver suas tarifas de consumo? (sim/nao)').lower()

while validacao != 'nao':
    consumo = float(input('Informe seu consumo de dados(GB):'))
    if consumo <= 10:
        tarifa = consumo * 5
    elif consumo > 10 and consumo <= 30:
        tarifa = consumo * 4
    else:
        tarifa = consumo * 3

    print(f'Total da conta: R${tarifa:.2f}')
    validacao = input('Deseja ver mais tarifas de consumo? (sim/nao)').lower()

    