import math
ad= float(input("quanto mede o cateto adjascente: "))
co= float(input("quanto mede o cateto oposto: "))
hip = math.hypot(co, ad)
print("o adjascente mede {} e o oposto mede {} portanto a hipotenusa e {}".format(ad,co,hip))