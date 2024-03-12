import time

op = 0
print("-==-"*8)
n1 = int(input("Primeiro Valor: "))
n2 = int(input("Segundo valor: "))
print("-==-"*8)
time.sleep(2)

while True:
    op = int(input("    [1] Somar"
                   "\n    [2] Multiplicar"
                   "\n    [3] Maior"
                   "\n    [4] Novos números"
                   "\n    [5] Sair do programa"
                   "\n>>>>>> Qual sua opção? "))

    time.sleep(1)
    print("...")
    time.sleep(1)

    if op == 1:
        s = n1 + n2
        print("-==-" * 8)
        print("{} + {} = {}".format(n1, n2, s))
        print("-==-" * 8)
        time.sleep(2)

    if op == 2:
        s = n1 * n2
        print("-==-" * 8)
        print("{} x {} = {}".format(n1, n2, s))
        print("-==-" * 8)
        time.sleep(2)

    if op == 3:
        if n1 > n2:
            print("-==-" * 8)
            print("O maior número é {}".format(n1))
            print("-==-" * 8)
            time.sleep(2)

        else:
            print("-==-" * 8)
            print("O maior número é {}".format(n2))
            print("-==-" * 8)
            time.sleep(2)

    if op == 4:
        print("-==-" * 8)
        n1 = int(input("Primeiro Valor: "))
        n2 = int(input("Segundo valor: "))
        print("-==-" * 8)
        time.sleep(2)

    if op == 5:
        break

