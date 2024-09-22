'''
Peça ao usuário para informar uma quantidade de metros existente em uma pista de corrida de 
atletismo. Converta o valor para centímetros e milímetros, e exiba o resultado
'''

tamanhoPista = float(input('Digite a quantidade de metros da pista de atletismo: '))

tamanhoCem = tamanhoPista * 100
tamanhoMil = tamanhoPista * 1000

print(f'Uma pista com {tamanhoPista}m tem {tamanhoCem} cm e {tamanhoMil} ml!')