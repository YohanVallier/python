# Sequência de Fibonacci v1.0
print("-" * 25)
print("Sequência de Fibonacci")
print("-" * 25)

# Passo 1: Criação da variável de termos
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
c = 3
if n == 1:
    print("{}".format(t1))
elif n == 2:
    print("{} -> {}".format(t1, t2))
else:
    print("{} -> {}".format(t1, t2), end = "")

# Passo 2: Laço de repetição while
while c <= n:
    t3 = t1 + t2
    print(" -> ", end = "")
    print("{}".format(t3), end = "")
    c += 1
    t1 = t2
    t2 = t3
