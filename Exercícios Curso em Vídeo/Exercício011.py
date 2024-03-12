l = float(input('Informe a largura da parede: '))
a = float(input('Informe a altura da parede: '))
area = l*a
litro = area/2
print('Sua parede tem dimensões de {}x{} e sua área é de {}m².'.format(l, a, area))
print('Para pintar essa parede, será necessário {}l de tinta'.format(litro))