'''
A Companhia Elétrica da sua cidade convidou você para fazer parte da equipe de desenvolvimento
e a sua primeira atribuição será desenvolver um algoritmo de controle de gastos diários por parte
do usuário. O algoritmo deverá solicitar ao usuário o consumo diário de energia elétrica em KWh.
Sempre que o usuário digitar o seu consumo diário, o algoritmo deverá exibir o consumo
acumulado e o valor atual da conta (considere R$ 0,60 por KWh). Se o consumo diário for maior
que 50KWh, exiba uma mensagem de alerta de alto consumo. O programa deverá continuar
regitrando até que o total mensal ultrapasse 1.500KWh. Ao ultrapassar, o algoritmo deve exibir o
total consumido de KWh e o valor total da conta.
'''
consumoAculumado, valorAtual = 0, 0.0

while True:
    consumoDiario = float(input('Informe seu consumo diário(KWh): '))
    consumoAculumado += consumoDiario
    valorAtual = consumoAculumado * 0.60
    print(f'Consumo acumulado: {consumoAculumado} | Valor atual: {valorAtual:.2f} reais.')

    if consumoDiario > 50:
        print('Seu consumo diário está alto, cuidado!')

    if consumoAculumado >= 1500.00:
        print('Seu total mensal ultrapassou 1.500Kwh!')
        print(f'Consumo total: {consumoAculumado} | Valor total: {valorAtual:.2f} reais.')
        break