'''
Um usuário deseja monitorar seu consumo de água para economizar. Inicialmente, solicite a quantidade de
dias que ele deseja realizar o monitoramento. Em seguida, solicite o consumo diário de água em litros e, ao
final, exiba quantos dias ele consumiu mais de 100 litros. Sempre que o consumo for acima de 100 litros,
emita um alerta. Quando o consumo for abaixo, mostre uma mensagem informando que o consumo está
dentro da média.
'''
consumoTotal = 0
qtdDias = int(input('Informe a quantidade de dias: '))

for i in range (0,qtdDias):
    consumoDiario = float(input(f'Informe seu consumo diário no {i+1}° dia: '))
    consumoTotal += consumoDiario


if consumoTotal > 100:
    print('!!! CUIDADO !!!')
    print('Seu consumo é maior que 100 litros!')
else:
    print('Seu consumo está dentro da média!')