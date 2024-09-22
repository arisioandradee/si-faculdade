'''
Peça ao usuário para inserir a temperatura atual em graus Celsius. Se a temperatura for inferior a 18°C, 
exiba "Frio". Se estiver entre 18°C e 28°C, exiba "Agradável". Caso contrário, exiba "Calor".
'''

temperatura = float(input('Digite a temperatura em Celcius(°C): '))

if temperatura < 18:
    print('Frio!')
elif temperatura >= 18 and temperatura <=28:
    print('Agradável!')
else:
    print('Calor!')