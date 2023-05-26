sexo = str(input("digite seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("sexo invalido digite corretamente: "))
else:
    print("o sexo {} foi salvo, obrigado".format(sexo))