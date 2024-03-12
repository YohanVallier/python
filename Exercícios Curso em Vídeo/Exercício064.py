# Tratando vários valores v1.0

# Passo 1: Criação da variável
a1 = s = 0

# Passo 2: Laço de repetição infinito + variável de quebra de laço de repetição
while True:
    n = int(input("Digite um número para eu realizar a soma, dígite [999] para parar de somar: "))
    if n == 999:
        break
    a1 += n
    s += 1

print("Você digitou {} números e a soma entre eles é igual a {}".format(s, a1))
