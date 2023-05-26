from random import randint
from time import sleep

computador = randint(0,5)
print("="*20)
print("vou programar um numero de 0 a 5, tente acertar")
print("="*20)
jogador=int(input("que numero eu programei? "))
print("Programando...")
sleep(3)
if jogador== computador:
    print("parabens voce acertou!!" )
else:
    print("voce errou eu pensei no numero {} e nao no {}".format(computador,jogador))