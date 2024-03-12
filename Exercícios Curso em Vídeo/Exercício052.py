# Números Primos
# Passo 1: variável de recepção e variável de contagem
n = int(input("Digite um número: "))
s = 0
c = int()
# Passo 2: laço de repetição for e if
for c in range(1, n + 1): 
    if n % c == 0:
        print("\033[32m", end = " ")
        s += 1
    else:
        print("\033[31m", end = " ")
    print("{}\033[m".format(c), end = " ") 
print("\nO número {} foi divisível {} vezes".format(n, s))
# Passo 3: laço de repetição if 
if  s > 2:
        print("\nE por isso ele NÃO È PRIMO")
else:
     print("\nEle foi divisível apenas por 1 e ele mesmo. Logo, ele é primo!")

