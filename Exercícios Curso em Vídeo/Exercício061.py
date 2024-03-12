# Progressão Aritmética v2.0
print("Termos de uma P.A")
print("-=-" * 8)

# Passo 1: Criação da variável
a1 = int(input("Primeiro Termo: "))
r = int(input("Razão da P.A: "))
count = 1

# Passo 2: Laço de Repetição while
while count <= 10:
    print("{} -> ".format(a1), end = "")
    a1 += r
    count += 1
print(" FIM ", end = "")
