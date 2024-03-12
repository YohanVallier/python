# Soma dos números múltiplos de 3 no intervalo de 1 até 500
# Passo 1: Definir a variável
s = 0
c = int()
k = 0
# Passo 2: Criação do laço de repetição de 1 a 500 mais variável de contagem
for c in range(1, 501):
# Passo 3: Estrutura if para dar a condição do múltiplo de 3
    if c % 3 == 0 and c % 2 != 0:
        k += 1
        s += c
print("A soma de todos os {} valores é igual a {}".format(k, s))
