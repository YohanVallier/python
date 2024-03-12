sal = float(input('Qual o salário de um funcionário? R$'))
aumento = sal + sal*(15/100)
print('Um funcionário que ganhava R${}, com aumento de 15%, passa a ganhar R${:.2f}!'.format(sal, aumento))