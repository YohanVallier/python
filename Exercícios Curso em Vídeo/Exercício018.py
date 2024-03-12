from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
ang_rad = radians(ang)
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, sin(ang_rad)))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cos(ang_rad)))
print('O ângulo de {} tem o tangente de {:.2f}'.format(ang, tan(ang_rad)))