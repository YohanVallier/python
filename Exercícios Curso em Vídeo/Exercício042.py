n1 = int(input('Primeiro segmento: '))
n2 = int(input('Segundo segmento: '))
n3 = int(input('Terceiro segmento: '))
if abs(n1 - n3) < n2 < n1 + n3 or abs(n2 - n3) < n1 < n2 + n3 or abs(n1 - n2) < n3 < n1 + n2:
    if n1 == n2 == n3:
        equi = 'equilátero!'
        print('Os segmentos acima podem formar um triângulo {}'.format(equi))
    elif n1 == n2 or n2 == n3 or n1 == n3:
        iso = 'isósceles!'
        print('Os segmentos acima podem formar um triângulo {}'.format(iso))
    elif n1 != n2 != n3:
        esc ='escaleno!'
        print('Os segmentos acima podem formar um triângulo {}'.format(esc))
else:
    print('Os segmentos não formam triângulo')