import datetime
sexo = str(input('Você é Homem/Mulher? ')).capitalize()
if 'Homem' in sexo:
    n = int(input('Em que ano você nasceu? '))
    ano_atual = datetime.date.today().year
    idade = ano_atual - n
    idade_alist = abs(18 - idade)
    ano_alist = ano_atual + idade_alist
    if idade < 18:
        if idade_alist > 1:
            an = ('anos')
            print('Quem nasceu em {} tem {} anos em {}.\n'
                  'Ainda faltam {} {} para o seu alistamento.\n'
                  'Seu alistamento será em {}.'.format(n, idade, ano_atual, idade_alist, an, ano_alist))
        else:
            an = ('ano')
            print('Quem nasceu em {} tem {} anos em {}.\n'
            'Ainda faltam {} {} para o seu alistamento.\n'
            'Seu alistamento será em {}.'.format(n, idade, ano_atual, idade_alist, an, ano_alist))
    elif idade == 18:
        if idade_alist > 1:
            an = ('anos')
            print('Quem nasceu em {} tem {} anos em {}.\n'
            'Você tem que se alistar IMEDIATAMAENTE. OBS: sem pressão...'.format(n, idade, ano_atual, idade_alist, ano_alist))
        else:
            an = ('ano')
            print('Quem nasceu em {} tem {} anos em {}.\n'
            'Você tem que se alistar IMEDIATAMAENTE. OBS: sem pressão...'.format(n, idade, ano_atual, idade_alist, ano_alist))
    else:
        print('Quem nasceu em {} tem {} anos em 2023.\n'
        'Você já deveria ter se alistado a {} {}.\n'
        'Seu alistamento foi em {}.'.format(n, idade, ano_atual, idade_alist, ano_alist))
elif 'Mulher' in sexo:
    print('Deu sorte... Tu não precisa se alistar mané')
