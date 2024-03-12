dia = float(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = dia*90 + (km/20)*30
print('O total a pagar é de R${}'.format(total))