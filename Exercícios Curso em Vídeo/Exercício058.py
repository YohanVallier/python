import random
comp = random.randint(0, 10)
s = 1
num = int(input("Sou seu computador..."
                "\nAcabei de pensar em um número entre 0 e 10"
                "\nSerá que você consegue advinhar ?"
                "\nQual seu palpite? "))

if num == comp:
        print("Você acertou de primeira! O valor realmente era {}".format(comp))

while num < comp:
    num = int(input("Mais... Tente mais uma vez."
                        "\nQual o seu palpite? "))
    s += 1

while num > comp:
    num = int(input("Menos... Tente mais uma vez."
                        "\nQual o seu palpite? "))
    s += 1

if num == comp and s >= 2:
    print("Você acertou o valor realmente era {}."
            "\nSeu número de tentativas foram iguais á {}".format(comp, s))
