dia = float(input("quantos dias o carro foi usado? "))
km = float(input("quantos quilometros percorridos? "))

preco = (dia * 60) + (km * 0.15)
print("o valor a pagar e {} reais".format(preco))