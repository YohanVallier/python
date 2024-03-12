# Super Progressão Aritmética v3.0
print("Gerador de P.A de 10 termos")
print("-=-" * 8)

# Passo 2: Criação da variável
a1 = int(input("Primeiro termo: "))
r = int(input("Digite a razão da P.A: "))
c = 0
op = 9
s = 0

# Passo 3: Laço de repetição while com aplicação de P.A
while True:
    while c <= op:
        print("{}".format(a1),end = "")
        print(" -> ", end = "")
        a1 += r
        c += 1
        s += 1
    c = 1
    print("PAUSA")
    op = int(input("\nQuanto termos você quer mostrar a mais? "))

# Passo 4: Quebra no laço de repetição
    if op == 0:
        break
print("Progressão finalizada com {} termos mostrados.". format(s))
