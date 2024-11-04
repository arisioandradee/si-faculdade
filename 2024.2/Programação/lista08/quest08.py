'''
Você, enquanto programador, decidiu desenvolver um algoritmo para sua economia financeira.
Seu algoritmo deve solicitar ao usuário a meta de economia que ele deseja (independente do
período) e a meta de economia mensal. As economias mensais devem ser somadas e acumuladas.
Enquanto o total economizado for menor que a meta da economia desejada, o programa deverá
ficar perguntando o valor mensal economizado. Sempre que o valor mensal economizado for
menor que a meta mensal, deve-se exibir um aviso informando quanto você economizou naquele
mês e o restatfe que faltou para atingir a meta mensal. Se a meta mensal for superada, uma
mensagem deve ser exibida informando este fato. O programa deve também, sempre informar o
total economizado todas as vezes que você inserir o valor economizado no mês.
'''
total = 0
metaGeral = float(input('Informe sua meta geral: '))

while True:
    metaMensal = float(input('Informe sua economia mensal: '))
    total += metaMensal

    if total < metaGeral:
        print(f'Nesse mês você economizou R${metaMensal:.2f} reais.')
        print(f'Ainda faltam ser economizados R${metaGeral - metaMensal:.2f} reais. ')

    if total >= metaGeral:
        print(f'Você atingiu sua meta geral! Valor economizado: R${total:.2f} reais.')
        break