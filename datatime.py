from datetime import datetime, timedelta

hoje = datetime.now()
print(hoje.date())


data_aula = datetime(year=2023,month=3, day=1,hour=14)
regressiva = data_aula-hoje
print(regressiva)