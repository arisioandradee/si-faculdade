'''
Um consultório tem uma meta mínima de atender ao menos 10 clientes por dia e uma meta ideal de 15
clientes por dia. Desenvolva um algoritmo que solicite ao usuário o número de clientes atendidos em cada
um dos cinco dias úteis e, se o valor for inferior a 10, exiba uma mensagem indicando a necessidade de
melhorar o atendimento. Se o valor estiver entre 10 e 14, exiba uma mensagem de incentivo para alcançar
a meta ideal. Se o valor for 15 ou mais, exiba uma mensagem de parabéns. Ao final, exiba o total de clientes
atendidos.
'''
total = 0
for i in range(0,5):
    quantidade = int(input(f'Informe a quantidade de clientes atendidos no {i+1}° dia: '))
    total += quantidade

    if quantidade < 10:
        print('É necessário melhorar o atendimento!')
    elif quantidade > 10 and quantidade <= 14:
        print('Falta pouco para atingir a meta ideal!')
    else:
        print('Parabéns, você atingiu a meta ideal!')

print(f'O total de pacientes atendidos foi: {total}')