distancia_km = float(input('Qual a distância da sua viagem em Km: '))
if distancia_km < 200:
    val = distancia_km * 0.5
    print('O preço da viagem vai ser de R${}'.format(val))
else:
    val = distancia_km * 0.45
    print('O preço da viagem vai ser de R${}'.format(val))
