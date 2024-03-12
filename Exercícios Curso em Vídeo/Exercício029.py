km = float(input('Inform sua velocidade atual? '))
if km <= 80:
    print('\033[0:32mÓtimo! Dirija com segurança.\033[m')
else:
    pre = (km - 80) * 7
    print('\033[0:31mMULTADO! Você ultrapassou o limete QUE É DE 80Km/h. A multa a ser paga é de R${}\033[m'.format(pre))
