'''
O restaurante Good Food oferece ao cliente a possibilidade de um atendimento exclusivo de garçom,
através de uma política de gorjeta. Caso o cliente solicite este tipo de serviço, a cobrança é feita da seguinte forma: se o consumo for acima de R$ 200,00, deverá ser acrescentada uma taxa de 15% no valor, que será repassada ao garçom, pelo próprio restaurante. Caso contrário, será acrescentada uma taxa de 10% no valor do consumo. Desenvolva um algoritmo para solicitar o valor do consumo e atribuir a taxa específica de acordo com as regras citadas.
'''

consumo = float(input('Digite o consumo(R$):'))

if consumo > 200.0:
    gorjeta = consumo * 0.15
    valorFinal = consumo + gorjeta
    print(f'O valor final é: R${valorFinal:.2f}')
else:
    gorjeta = consumo * 0.10
    valorFinal = consumo + gorjeta
    print(f'O valor final é: R${valorFinal:.2f}')