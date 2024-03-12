#Estatísticas em produtos
print("-" * 40)
print(' ' * 8,'LOJA SUPER BARATÃO')
print("-" * 40)


c = total = cont_menor = 0
p = str('produto')


while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    
    total += preco
    cont_menor += 1 

    
    if cont_menor == 1:
        menor = preco
        produto_menor = produto

    elif preco < menor:
        produto_menor = produto
        menor = preco

    if preco > 1000:
        c += 1

    if c > 1:
        p = str('produtos')
            
    conti = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    if conti == 'N':
        break


print('-------FIM DO PROGRAMA-------')
print(f'O total da compra foi de R${total}'
      f'\nTemos {c} {p} custando mais de R$1000'
      f'\nO produto mais barato foi {produto_menor} custando R${menor}')


