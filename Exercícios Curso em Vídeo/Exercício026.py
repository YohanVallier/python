nom = input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} vezes na frase.'.format(nom.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(nom.find('A')+1))
print('A primeira letra A apareceu na última posição {}.'.format(nom.rfind('A')+1))
