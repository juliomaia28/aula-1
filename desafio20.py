preco = float(input("qual o preco do produto? "))
desconto = preco - (preco* 5/100)
print("o preco do produto e {} reais, porem com o desconto de 5%, o preco novo sera {:.1f}".format(preco, desconto))