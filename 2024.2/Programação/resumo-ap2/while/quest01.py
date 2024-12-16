'''
Você foi solicitado pelo seu líder de equipe para desenvolver um algoritmo de inclusão e soma de itens de
um caixa de supermercado. O algoritmo deve perguntar ao usuário se ele deseja incluir um item. Em seguida,
deve solicitar o valor do item e perguntar novamente se ele deseja adicionar outro item. Use o laço de
repetição while para continuar até que o usuário indique que não deseja adicionar mais itens. Exiba o valor
total da compra.
'''
total = 0
inicio = input('Você deseja incluir um item(sim/nao)?').lower()

while inicio != 'nao':
    valor = float(input('Informe o valor do item: '))
    total += valor
    inicio = input('Você deseja incluir um item(sim/nao)?').lower()

print(f'O total é R${total:.2f}')