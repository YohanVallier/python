# Soma dos Pares
# Passo 1: variável de recepção mais variável de contagem
n = int(input("Digite um valor pra eu realizar a soma de todos os seus números pares: "))
s = 0
# Passo 3: Criação do laço de repetição para realização da soma de pares
for c in range(0, n):
    if c % 2 == 0:
        s += 1
print("A soma de todo os pares é igual a {}".format(s))
