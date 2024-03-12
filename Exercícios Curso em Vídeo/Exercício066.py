# Vários números com flag

# Passo 1: Criação da variável
k = s = 0

# Passo 2: Laço de repetição while mais estrutura break quebra de laço infinito
while True:
    n = int(input("Digite um número, digite [999] para parar: "))
    if n == 999:
        break
    s += 1
    k += n
print(f"A soma dos {s} valores foi igual a {k}!.")
