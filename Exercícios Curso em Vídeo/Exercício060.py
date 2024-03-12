# Cálculo de Fatorial

# Passo 1: Importação de módulo
import time
f = 1
n1 = 1

# Passo 2: Estrutura while e variável
while n1 == 1:
     n = int(input("Digite o valor para eu calcular o Factorial: "))
     time.sleep(2)
     print("Calculando... {}! = ".format(n), end = "")
     c = n

     while c > 0:
          print("{}".format(c), end = "")
          print(" x " if c > 1 else " = ", end = "")
          time.sleep(0.5)
          f *= c
          c -= 1
     print("{}".format(f))

# Passo 3: Programa retorna
     print("Você quer que eu continue a calcular novos números?...")
     time.sleep(1)
     n1 = int(input("Se sim digite [1]"
                    "\nSe não digite [2]"
                    "\nQual sua opção: "))
     if n1 == 2:
          print("Uma pena que encerraremos por aqui")
          time.sleep(2)
          print("Adeus...")
          time.sleep(2)
          print("Volte Sempre! :)")
          break
