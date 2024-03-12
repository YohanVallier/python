print('=' * 10, 'LOJAS VALLIER', '=' * 12)
n = float(input('Preço das compras: R$'))
forma_pagamento = int(input('FORMAS DE PAGAMENTO\n'
                        '[1] á vista deinheiro ou cheque\n'
                        '[2] á vista cartão\n'
                        '[3] 2x no cartão\n'
                        '[4] 3x ou mais no cartão\n'
                        'Qual é a opção? '))
if forma_pagamento == 1:
    k = n - (n * (10 / 100))
    print('Sua compra de {} vai custar {} no final.'.format(n, k))
elif forma_pagamento == 2:
    k = n - (n * (5/ 100))
    print('Sua compra de {} vai custar {} no final.'.format(n, k))
elif forma_pagamento == 3:
    d = n / 2
    print('Sua compra será parcelada em 2x de {} sem juros\n Sua compra vai custar R${}'.format(d, n))
else:
    d = int(input('Quantas parcelas?'))
    k = n + (n * (20 / 100))
    l = k / d
    print('Sua compra será parcelada em {}x de {} com juros\n Sua compra de R${} vai passar a custar R${}'.format(d, l, n, k))
