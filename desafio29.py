n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
opcao = 0
while opcao != 5:
    print('''[1] Somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] parar o sistema''')
    opcao = int(input("Digite sua opcao: "))
    if opcao == 1:
        print("{} + {} = {}".format(n1,n2,n1 + n2))
    elif opcao == 2:
        print("{} x {} = {}".format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print("o {} e maior".format(n1))
        else:
            print('o {} e maior'.format(n2))
    elif opcao == 4:
        print("digite novos numeros: ")
        n1 = (int(input("Primeiro numero")))
        n2 = (int(input("Segundo numero")))
    elif opcao == 5:
        print("Acabou!!")
    else:
        print("numero invalido digite novamente")


