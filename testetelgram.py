from datetime import datetime

hoje= datetime.now()
aula =datetime(year=2023,month=3, day=2, hour=17)
atraso =aula-hoje
print(atraso)

