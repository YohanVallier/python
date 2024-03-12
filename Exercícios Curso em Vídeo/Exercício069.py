# Análise de dados do grupo
total_idade = total_masculino = total_feminino = 0
while True:
    print("-" * 30)
    print("     CADASTRE UMA PESSOA")
    print("-" * 30)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().split()[0]
    print("-" * 30)
    op = str(input("Quer Continuar? [S/N] ")).upper().split()[0]

    if idade > 18:
        total_idade += 1

    if sexo == "M":
        total_masculino += 1
        if total_masculino == 1:
            M = str("homen")
        else:
            M = str("homens")

    if sexo == "F" and idade < 20:
        total_feminino += 1
        if total_feminino == 1:
            F = str("mulher")
        else:
            F = str("mulheres")

    if op == "N":
        break
print("-" * 30)
print(f"Total de pessoas com mais de 18 anos é igual a {total_idade}."
      f"\nAo todo temos {total_masculino} {M} cadastrados."
      f"\nE temos {total_feminino} {F} com menos de 20 anos.")
