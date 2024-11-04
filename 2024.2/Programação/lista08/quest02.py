'''
Você foi contratado para fazer parte da equipe de desenvolvimento da operadora TIM. A sua
primeira atribuição será desenvolver um algoritmo que realize o controle de dados móveis do
cliente de acordo com seu limite mensal. O algoritmo deverá solicitar o limite mensal e registrar,
diariamente, o consumo de dados em GB do cliente, informando quantos GB já foram consumidos
e quantos ainda estão disponíveis. Quando o consumo atingir 80%, o cliente deve ser informado
sobre a porcentagem consumida. Ao atingir o limite de dados, uma mensagem deverá ser exibida.
'''
contDias, somaDiaria = 1, 0
limiteMensal = float(input('Infome seu limite mensal(GB): '))

while limiteMensal > 0:

    limiteDiario = float(input(f'Informe o consume de dados(GB) do dia {contDias}: '))
    contDias += 1

    somaDiaria += limiteDiario
    print(f'Já foram consumidos {somaDiaria} GB, restam ainda {limiteMensal - somaDiaria}')

    porcentConsumida = (somaDiaria / limiteMensal) * 100
    porcentRestante = 100 - porcentConsumida

    if porcentConsumida > limiteMensal * 0.8:
        print(f'Sua porcentagem consumida é: {porcentConsumida:.2f}%')
        print(f'Sua porcentagem restante é: {porcentRestante:.2f}%')

    if somaDiaria >= limiteMensal:
        print(f'Você atingiu todo seu limite mensal! ')
        break