from math import factorial
n = int(input("Digite um valor para ver seu fatorial: "))
c = n
f = factorial(n)
while c > 0:
    print("{}".format(c), end=" ")
    c-=1
    print(" x " if c > 0 else " = ", end=" ")
print(f)



