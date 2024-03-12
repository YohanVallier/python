sal = float(input('Me informe o seu salário para eu fazer o cálculo de aumento: R$'))
if sal > 1250:
    sal_aumento = sal + (sal * 0.1)
    print('O aumento foi de 10% do seu salário e passa a ser R${}'.format(sal_aumento))
else:
    sal_aumento = sal + (sal * 0.15)
    print('O aumento foi de 15% do seu salário e passa a ser R${}'.format(sal_aumento))
