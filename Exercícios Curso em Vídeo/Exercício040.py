n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media == 10:
    print('BRABO DEMAISSS! GABARITOUUU! APROVADISSIMO!\n'
          'Quem tirou {} e {} tem a média {}.\n'
          'Isso ai Guerreiro!'.format(n1, n2, media))
elif media >= 7:
    print('Quem tirou {} e {} tem a média {}.\n'
          'Aprovado!'.format(n1, n2, media))
elif 5 < media < 7:
    print('Quem tirou {} e {}.\n'
          'Po mano estuda mais um pouco que tu consegue tá ligado, sua média foi {}. Recuperação...'.format(n1, n2, media))
else:
    print('Quem tirou {} e {}.\n'
          'Reprovado, sua média foi {}. Tenta de novo, não desista!'.format(n1, n2, media))
