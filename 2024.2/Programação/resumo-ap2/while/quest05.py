'''
Desenvolva um algoritmo que solicite ao usuário a velocidade do carro e compare com o limite de 80 km/h,
de acordo com as seguintes condições:
I) Se a velocidade estiver até 10 km/h acima do limite, aplique multa de R$50,00.
II) Se a velocidade estiver acima de 10 e até 30 km/h acima, aplique multa de R$100,00.
III) Se a velocidade estiver acima de 30 km/h, aplique multa de R$200,00.
Após a aplicação da multa, o programa deve mostrar o valor a ser pago e perguntar ao usuário se ele quer
verificar outra velocidade. O fluxo deve se repetir até que algum comando seja inserido para o encerramento
do programa.
'''
limite = 80
validacao = input('Você deseja verificar uma velocidade? (sim/nao)')

while validacao != 'nao':
    velocidade = float(input('Informe a velocidade do carro: '))

    if velocidade <= (limite + 10):
        print('Sua multa é de R$50,00')
    elif velocidade > (limite + 10) and velocidade < (limite +30): 
        print('Sua multa é de R$100,00')
    else:
        print('Sua multa é de R$200,00')
    validacao = input('Você deseja verificar outra velocidade? (sim/nao)')