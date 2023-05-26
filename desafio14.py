distancia = float(input("qual a distancia da viagem? "))
print ("a sua viagem e de {}km".format(distancia))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("o preco da viagem e {}".format(preco))
    