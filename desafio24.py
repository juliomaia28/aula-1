num = int(input("Digite um numero inteiro: "))
print(''' Escolha uma base de conversao: 
[1] converter para binario
[2] converter para octal
[3] converter para hexadecimal''')
opcao = int(input("sua opcao :"))
if opcao == 1:
    print("o numero {} em binario e {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("o numero {} em octal e {}",format(num, oct(num)[2:]))
elif opcao == 3:
    print("o numero {} em hexa decimal e {}".format(num, hex(num)[2:]))
else:
    print("escolha invalida, selecione outra opcao! ")