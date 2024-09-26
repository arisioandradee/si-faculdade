'''
Solicite ao usuário que insira os três lados de um triângulo. Verifique se o triângulo é equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).
'''

lado1 = float(input('Digite o primeiro lado do triângulo: '))
lado2 = float(input('Digite o segundo lado do triângulo: '))
lado3 = float(input('Digite o terceiro lado do triângulo:'))

if (lado1 == lado2 == lado3):
    print('O triangulo é é equilátero!')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print('O triangulo é é isósceles!')
else:
    print('O triangulo é é escaleno!')

    