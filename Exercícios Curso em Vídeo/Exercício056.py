# Analisador completo
import math
s = 0
s1 = 0
for c in range(1, 5):
    print ("-" * 5, "{}ª PESSOA".format(c), "-" * 5)
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo =str(input("Sexo [M/F]: ")).upper()
    s += idade
    if "M" in sexo:
        if c == 1:
            maior = 1
            menor = 1
        if c > maior:
            maior = idade
        else:
            menor = idade
        if maior == maior:
            nome1 = nome.capitalize()
    if "F" in sexo:
        if idade < 20:
            s1 += 1
media = float(s / 4)  
print("A média de idade do grupo é de {} anos.".format(math.trunc(media)))
print("O homem mais velho tem {} anos e se chama {}.".format(maior, nome1))
print("Ao todo são {} mulheres com menos de 20 anos".format(s1))
