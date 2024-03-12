# Maior e menor valor

# Passo 1: Criação das variáveis
op = str("s")
s = a1 = mai = 0

# Passo 2: Laço de repetição while
while True:
    n = int(input("Digite um número: "))
    op = str(input("Quer continuar [S/N]? ")).upper().lower()
    s += 1
    a1 += n
    men = mai

# Passo 3: Estrutura if que define maior e menor
    if mai < n:
        mai = n
    if men > n:
        men = n

# Passo 4: Estrutura que define quando o comando irá parar
    if op == "n":
        break

# Passo 5: Menasagem que irá mostrar a quantidade de números, a média entre eles, maior e menor valor
med = a1/s
print("~" * 60)
print("Você digitou {} números e a média entre eles é igual a {}."
      "\nO maior valor foi {} e o menor foi {}.".format(s, med, mai, men))
print("~" * 60)
