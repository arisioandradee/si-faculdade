'''
Uma empresa de estacionamento privativo contratou você para desenvolver um algoritmo de
controle de fluxo de carros. O programa deve, inicialmente, solicitar o limite de vagas do
estacionamento e, em seguida, registrar sempre que entrar e sair um carro, mostrando quantas
vagas foram ocupadas e quantas ainda estão livres. Ao atingir 90% da sua capacidade, um alerta
deve ser emitido. O fluxo deve continuar até que o estacionamento esteja lotado
'''
vagas = 0
capacidade = int(input('Informe a capacidade de vagas do estacionamento: '))

while True:
    print(f'Vagas ocupadas: {vagas}, Vagas livres: {capacidade - vagas}')
    
    opcao = int(input('1 - Preencher vaga | 2 - Liberar vaga: '))
    quantidade = int(input('Informe a quantidade de vagas a serem ocupadas/liberadas: '))

    if opcao == 1:
        if vagas + quantidade > capacidade:
            print('Não há vagas suficientes disponíveis!')
        else:
            vagas += quantidade
            if vagas >= 0.9 * capacidade:
                print('Alerta: O estacionamento atingiu 90% da capacidade!')
    elif opcao == 2:
        if vagas - quantidade < 0:
            print('Não é possível liberar mais vagas do que o total ocupado!')
        else:
            vagas -= quantidade
    else:
        print('Opção inválida!')

    if vagas >= capacidade:
        print('Todas as vagas estão ocupadas no momento!')
        break