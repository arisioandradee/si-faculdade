ladoA = float(input('Digite o valor do lado A  do triângulo: '))
ladoB = float(input('Digite o valor do lado B do triângulo: '))
ladoC = float(input('Digite o valor do lado C do triângulo: '))

if ladoA == ladoB == ladoC:
    print('O triângulo é equilátero!')
elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!')