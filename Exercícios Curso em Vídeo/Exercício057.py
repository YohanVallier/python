#Validação de Dados 
sexo = str(input("Informe o seu sexo [M/F]: ")).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input("Opção inválida. Digite novamente, sexo [M/F]: ")).upper().strip()[0]
print("Seu sexo é {}. Foi registrado com sucesso!".format(sexo))
