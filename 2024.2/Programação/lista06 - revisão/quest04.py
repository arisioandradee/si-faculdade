'''
O restaurante Good Food oferece ao cliente a possibilidade de um atendimento exclusivo de garçom, 
através de uma política de gorjeta. Caso o cliente solicite este tipo de serviço, a cobrança é feita da 
seguinte forma: se o consumo for acima de R$ 200,00, deverá ser acrescentada uma taxa de 15% no 
valor, que será repassada ao garçom, pelo próprio restaurante. Caso contrário, será acrescentada uma 
taxa de 10% no valor do consumo. Desenvolva um algoritmo para solicitar o valor do consumo e atribuir a 
taxa específica de acordo com as regras citadas.
'''

valorConta = float(input('Digite o valor da conta(R$): '))

if valorConta > 200.0:
    valorComTaxa = valorConta + valorConta * 0.15
    print(f'O valor final com a utilização do serviço exclusivo é: R${valorComTaxa:.2f}')
else:
    valorComTaxa = valorConta + valorConta * 0.10
    print(f'O valor final com a utilização do serviço exclusivo é: R${valorComTaxa:.2f}')