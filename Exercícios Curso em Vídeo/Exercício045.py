import random 
n = random.randint(1, 3)
if n == 1:
    n ='PEDRA'
elif n == 2:
    n = 'PAPEL'
else:
    n = 'TESOURA'
print('=' * 10, 'ACERTE O MEU JOGO', '=' * 12)
escolha = str(input('[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA\n'
                    'Escolha uma opção: '))
if escolha == 1:
    escolha ='PEDRA'
elif escolha == 2:
    escolha = 'PAPEL'
else:
    escolha = 'TESOURA'
if 'PEDRA' in escolha and n == 'PAPEL' :
    print('Você perdeu. Sua escolha foi {} e eu escolhi {}'.format(escolha, n))
elif 'PAPEL' in escolha and n == 'TESOURA':
    print('Você perdeu. Sua escolha foi {} e eu escolhi {}'.format(escolha, n))
elif 'TESOURA' in escolha and n == 'PEDRA':
    print('Você perdeu. Sua escolha foi {} e eu escolhi {}'.format(escolha, n))
else:
    print('Você ganhou. Sua escolha foi {} e eu escolhi {}'.format(escolha, n))
