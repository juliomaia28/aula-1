salario = float(input("Digite o valor do salário: "))

porcentagem = float(input("Digite a porcentagem do aumento: "))



aumento = salario * (porcentagem / 100)

promocao = salario + aumento



inss = promocao * 0.14

irpf = promocao * 0.225

descontos = inss + irpf



salario_liquido = promocao - descontos



print("Salário líquido: R$ {:.2f}".format(salario_liquido))
