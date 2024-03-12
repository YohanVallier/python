# Tabuada v.2.0

# Passo 1: Criar variável de recepção
n = int(input("Digite um valor para eu lhe informar a tabuada: "))

# Passo 2: Criar laço de repetição mais variável de multiplicação
for c in range(1, 11):
    v = n * c
    print("{} x {} = {}".format(n, c, v))
