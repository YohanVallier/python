# Progressão Aritmética
print("=" * 26)
print("   10 TERMOS DE UMA PA")
print("=" * 26)
# Passo 1: variável de recepção
t1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
# Passo 2: laço de repetição com variável de recepção
for c in range(1, 11):
   p = t1 + (c - 1) * r
   print(p, end = " -> ")
print("ACABOU!")
