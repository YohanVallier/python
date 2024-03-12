#Simulador de Caixa Eletrônico
print('=' * 40)
print('{:^40}'.format('CAIXA ELETRÔNICO CEV'))
saque = int(input('Qual o valor a ser sacado? R$'))
ced = int(50)
total_ced = int(0)
while True:
    if saque >= ced:
        total_ced += 1
        saque -= ced
    else:
        if total_ced > 0:
            print(f'{total_ced} cédula de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if saque == 0:
            break