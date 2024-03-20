#Número por extenso
num = int(input('Digite um número entre 0 e 20: '))

lista_tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dolze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    if 0 <= num <= 20:
        break
    num = int(input('Tente novamente. Digite um número entre 0 e 20: '))


print(f'Você digitou o número {lista_tupla[num]}!')
