salario = int(input("quanto e seu salario? "))
casa = int(input("qual valor da casa? "))
anos = int(input("em quantos anos vai pagar a casa? "))

prestacao= casa / (anos * 12)
minimo = salario * 30/100
print("para pagar uma casa de {} em {} anos".format(casa, anos), end=" " )
print("prestacao sera de R${:.2f}".format(prestacao))
if prestacao > minimo:
    print("emprestimo negado")
else:
    print("esprestimo liberadó")