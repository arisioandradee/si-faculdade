'''
Determinada empresa realiza o pagamento de seus funcionários a partir da quantidade de horas trabalhadas
e turnos trabalhados. Desenvolva um algoritmo que, primeiramente, deverá perguntar quantos funcionários
a empresa irá realizar o cálculo de pagamento. Em seguida, o cálculo deverá levar em consideração as
seguintes condições:
I) Perguntar o turno trabalhando (1 para diurno e 2 para noturno);
II) Valor por hora (R$ 30,00 para diurno e R$ 40,00 para noturno);
III) Benefício adicional de 10% para quem trabalhou mais de 180 horas no mês, independente do turno.
'''
salario, bonus = 0, 0.10
numeroFuncionaros = int(input('Informe o número de funcionários que deseja realizar o calculo: '))

for i in range(0, numeroFuncionaros):
    turno = int(input('Informe o turno do funcionário(1 - Diurno / 2 - Noturno): '))
    horas = float(input('Informe a quantidade de horas trabalhadas: '))

    if turno == 1:
        salario = horas * 30
    elif turno == 2:
        salario = horas * 40
    else:
        print('O código não existe para nenhum turno! Tente novamente!')
        continue

    if horas > 180:
        salario *= 1 + bonus

    print(f'Salário do funcionário {i+1}: R${salario:.2f}')