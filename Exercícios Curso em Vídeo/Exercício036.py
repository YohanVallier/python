valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Quanto você recebe de salário? R$'))
valor_anos = int(input('Quantos anos de financiamento? '))
prest = valor_casa / (valor_anos * 12)
#Multiplicou o valor_anos por 12 para transformar em meses
salario_limitante = salario * 0.3
if prest <= salario_limitante:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor_casa, valor_anos, prest))
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(valor_casa, valor_anos, prest))
    print('Empréstim NEGADO!')
