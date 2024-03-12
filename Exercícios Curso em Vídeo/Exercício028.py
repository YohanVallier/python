import random
print('\033[0:36m-=-\033[m'*18)
print('\033[0:35mVou pensar em número entre 0 e 5. Tente advinhar...\033[m')
print('\033[0:36m-=-\033[m'*18)
d = random.randint(0, 5)
n = int(input('Informe um número: '))
if n == d:
    print('Você acertou, o número realmente é {}.'.format(n))
else:
    print('Você errou, o número que pensei era {} e não {}.'.format(d, n))
