alt = float(input('Qual sua altura em métros (m)? '))
peso = int(input('Qual seu peso (Kg)? '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Está abaixo do peso!')
elif 18.5 < imc < 25:
    print('está com o peso normal')
elif 25 < imc < 30:
    print('Está em sobrepeso')
elif 30 < imc < 40:
    print('Está em obesidade')
else:
    print('Está em obesidade mórbida')