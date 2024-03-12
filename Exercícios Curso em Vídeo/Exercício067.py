# Tabuada v3.0
print("Tabuada da Braba v3.0")

# Passo 1: Importar Biblioteca
import time

# Passo 2: Criação da variável
tab = int(input("Digite o valor para eu calcular a tabuada: "))
cont = 1

# Passo 3: Estrutura while para tabuada
while True:
    if tab == -9:
        print("-" * 34)
        print("Finalizamos por aqui então! :)")
        print("-" * 34)
        break
    print("-" * 15)
    while cont != 11:
        mult = cont * tab
        print(f"{tab} x {cont} = {mult}")
        cont += 1
        time.sleep(0.35)
    print("-" * 15)
    cont = 1
    tab = int(input("Qual número você quer que eu calcule a tabuada agora? "))
    if tab == -9:
        print("-" * 34)
        print("Finalizamos por aqui então! :)")
        print("-" * 34)
        break
