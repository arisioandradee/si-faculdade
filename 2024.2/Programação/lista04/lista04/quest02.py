'''
Uma companhia aérea limita o peso máximo da bagagem em 23 kg. Peça ao usuário para informar 
o peso da sua bagagem em quilogramas. Em seguida, calcule e exiba quanto ele precisa remover 
(se necessário) para atingir o limite. Oriente o usuário sobre os possíveis resultados que ele poderá 
ver em tela, no seguinte sentido: caso o resultado dê negativo ou zero, não há a necessidade de 
remover pesos da bagagem. Caso o resultado seja positivo, o usuário deverá remover alguns quilos.
'''

pesoMaximo = 23
pesoBagagem = float(input('Digite o peso, em kilos, da sua bagaem: '))
pesoFinal = pesoBagagem - pesoMaximo

print(f'A quantidade em Kg a ser removida é: {pesoFinal}')
print('OBS: Se o resultado for negativo ou zero, não há a necessidade de remover pesos da bagagem')