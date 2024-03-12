# Maior e menor sequência
for c in range(1, 6):
    n = int(input("Peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if n > maior:
            maior = n
        else:
            menor = n
print("O maior peso lido foi de {}Kg\nO menor peso lido foi de {}Kg".format(maior, menor))
