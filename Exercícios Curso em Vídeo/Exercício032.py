ano = int(input('Me informe um ano que vou te dizer se é um ano bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim o ano de {} é um ano bissexto.'.format(ano))
else:
    print('Não, o ano {} não é um ano bissexto.'.format(ano))