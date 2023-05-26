ano = int(input("Ano de nascimento: "))
idade = 2022 - ano
faltam = 18 - idade
print("quem nasceu em {} tem {} anos em 2022".format(ano, idade))
if idade > 17:
    print("voce devera se apresentar na junta para o alistamento obrigatorio ")
else:
    print("ainda faltam {} anos para voce se alistar".format(faltam))