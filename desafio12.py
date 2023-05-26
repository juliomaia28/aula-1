velocidade = float(input("qual a velocidade do carro? "))
if velocidade >80:
    print("Voce foi multado")
    multa = (velocidade - 80)*7
    print ("voce deve pagar R${:.2f}".format(multa))
else:
    print("Tenha um bom dia")