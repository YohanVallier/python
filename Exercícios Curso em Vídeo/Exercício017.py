from math import hypot
cat1 = float(input('Qual é o cateto oposto? '))
cat2 = float(input('Qual é o cateto adjacente? '))
print('Sua hipotenusa é: {:.2f}'.format(hypot(cat1, cat2)))