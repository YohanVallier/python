n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
'''if n1 > n2 and n1 > n3 and n2 < n3:
    print('O maior valor é {} e o menor valor é {}'.format(n1, n2))
if n1 > n2 and n1 > n3 and n3 < n2:
    print('O maior valor é {} e o menor valor é {}'.format(n1, n3))
if n2 > n1 and n2 > n3 and n1 < n3:
    print('O maior valor é {} e o menor valor é {}'.format(n2, n1))
if n2 > n1 and n2 > n3 and n3 < n1:
    print('O maior valor é {} e o menor valor é {}'.format(n2, n3))
if n3 > n1 and n3 > n2 and n2 < n1:
    print('O maior valor é {} e o menor valor é {}'.format(n3, n2))
else:
    print('O maior valor é {} e o menor valor é {}'.format(n3, n1))'''
#Valores Menores
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Valores Maiores
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))
