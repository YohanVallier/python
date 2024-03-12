# Detector de Palindromo
# Passo 1: variável de recepção, variável de divisão, variável de aproximação de string, variável de tamanho de string
nome = str(input("Digite uma frase: ")).upper()
div = nome.split()
junt = "".join(div)
tam = len(junt) - 1
s = ""
# Passo 2: laço de repetição for
'''for palin in range(tam, -1, -1):
    s += junt[palin]'''
# Passo 2: usar método de fatiamento 
s = junt[::-1]
print("Você digitou a frase {}, esta frase de trás pra frente é {}".format(nome, s))
# Passo 3: laço de repetição if para informar se e um palindromo ou não
if s == junt:
    print("É um PALINDROMO")
else:
    print("Não é um PALINDROMO")
