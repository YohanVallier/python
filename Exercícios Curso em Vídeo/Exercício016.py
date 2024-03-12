'''val = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {:.0f}'.format(val, val))
import math
val = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(val, math.trunc(val)))'''
from math import trunc
val = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(val, trunc(val)))