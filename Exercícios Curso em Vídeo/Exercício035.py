print('\033[0:35m-=-\033[m'*12)
nome = ('\033[0:33mAnalisador de Triângulos\033[m')
print('{:^44}'.format(nome))
print('\033[0:35m-=-\033[m'*12)
n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
if abs(n2 - n3) < n1 < n2 + n3 and abs(n1 - n3) < n2 < n1 + n3 and abs(n1 - n2) < n3 < n1 + n2:
    print('')
    print('Os segmentos podem formar um triângulo!')
else:
    print('')
    print('Os segmentos não podem formar um triângulo!')
