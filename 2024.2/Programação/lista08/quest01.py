'''
O cheque especial é quando o banco fornece ao seu cliente um limite de gastos a mais na conta
corrente, a partir do momento que o saldo é zerado. Dessa forma, o cliente pode continuar
utilizando sua conta corrente com o cheque especial, porém, o saldo fica negativo. Sabendo disso,
desenvolva um algoritmo de controle de gastos diários com o uso do cartão de débito. O algoritmo
deve realizar as seguintes ações:
I) Solicitar o valor do saldo em conta corrente;
II) Perguntar se o usuário deseja iniciar o controle de gastos diários;
III) Solicitar o valor de cada gasto;
IV) Sempre que o usuário informar o valor gasto, mostrar o percentual que já foi utilizado do seu
saldo;
V) Sempre que o usuário informar o valor gasto, mostrar o valor dos gastos totais até o momento
e o saldo restante em conta.
VI) Caso os gastos tenham ultrapassado o saldo, informar que o saldo foi ultrapassado e o cliente
está utilizando o cheque especial.
'''
gasto, percentual, totalGasto = 0.0, 0.0, 0.0

saldoContaCorrente = float(input('Informe o saldo na conta corrente: '))
escolha = input('Você deseja iniciar o controle de gastos diários? (sim/nao) ').lower()

while escolha != 'nao':
    print('0 - Parar de digitar gastos!')
    
    while True:
        gasto_input = input('Informe o valor de um gasto: ')
        
        if gasto_input == '0':
            break  

        if gasto_input.replace('.', '', 1).isdigit(): 
            gasto = float(gasto_input) 
            totalGasto += gasto 

            percentual = (totalGasto / saldoContaCorrente) * 100

            print(f'Esse gasto equivale a {percentual:.2f}% do seu saldo!')
            print(f'O total gasto até agora é: R${totalGasto:.2f}')
            saldoRestante = saldoContaCorrente - totalGasto
            print(f'Seu saldo restante é: R${saldoRestante:.2f}')

            if totalGasto > saldoContaCorrente:
                print('Seu saldo foi ultrapassado, você está usando o cheque especial!')
        else:
            print("Por favor, insira um valor numérico válido.")
    
    escolha = input('Você deseja fazer outro controle de gastos diários? (sim/nao) ').lower()

print('Programa encerrado!')