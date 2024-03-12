n1 = int(input('Digite um número inteiro: '))
escolha = str(input('Escolha uma das bases para conversão:\n'
                    '[1] converter para Binário\n'
                    '[2] converter para OCTAL\n'
                    '[3]  converter para HEXADECIMAL \n'
                    'Qual sua opção:'))
if '1' in escolha:
    n = bin(n1)[2:]
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, n))
elif '2' in escolha:
    n = oct(n1)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(n1, n))
elif '3' in escolha:
    n = hex(n1)[2:]
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n1, n))
