# Jogo par ou ímpar
print("-=-" * 9)
print(str("VAMOS JOGAR PAR OU IMPAR?"))
print("-=-" * 9)

# Passo 1: Importação de biblioteca
import random


v = 0
while True: 
    val = int(input("Digite um valor: "))
    comp = random.randint(0, 10)
    soma = val + comp
    op = " "
    while op not in "PI":
        op = str(input("Digite [P] para par e [I] para ímpar: ")).upper()
    print(f"Você jogou {val} e o computador {comp}. A soma deu {soma}")
    if op == "P":
        if soma % 2 == 0:
            v += 1
            print("Você venceu!")
        else:
            print("Você perdeu!")
            break
    elif op == "I":
        if soma % 2 == 1:
            v += 1
            print("Você venceu!")
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
