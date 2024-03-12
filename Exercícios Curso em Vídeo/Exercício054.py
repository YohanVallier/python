# Grupo da maioridade
# Passo 1: variável de contagem 
s = 0  
k = 0
# Passo 2: criação de laço de repetição for mais estrtura if 
for c in range(1, 8):
    n = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
    if 2023 - n <= 18:
        s += 1
    else:
        k += 1
print("Ao todo tivemos {} pessoas de maior idade.\n E tambem tivemos {} pessoas menores de idade".format(s, k))
