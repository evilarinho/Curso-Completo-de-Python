import os
os.system('clear')

# entrar no Python
import datetime
datetime.MINYEAR
datetime.MAXYEAR

datetime.date(2025,9,20)
datetime.date(2025, 9, 20)
data = datetime.date(2025,9,20)
print(data)
data.year
data.day
data.month
datetime.date.today()
datetime.date(2023, 12, 11)
print(datetime.date.today())
print(datetime.date.min)
print(datetime.date.max)
print(datetime.datetime.now())
print(datetime.datetime.today())
data_completa = datetime. datetime (2023, 11, 1, 13, 15, 55)
print(data_completa)
print(data_completa.month)
print(data_completa.hour)
agora = datetime.datetime.today()
print(agora)
print(agora.strftime("%d/%d/%Y"))
print(agora.strftime("%d/%d/%y"))
print(agora.strftime("%H:%M:%S"))

# https://docs.python.org/3/library/datetime.html

hoje = datetime.datetime.now()
festa = datetime.datetime(2025,10,1,18,00)
dias = festa - hoje
type(dias)
print(f'Fatam {dias.days} para a festa.')
dias.seconds
62652

from datetime import datetime, timedelta
delta_days = timedelta(days=5)
print(delta_days.days)
delta_horas = timedelta(hours=2)
agora = datetime.now()
vencimento = agora + timedelta(days=42)
print(vencimento)
print(f'O boleto vence em {vencimento.strftime("%d/%m/%Y")}')

import time
print(time.gmtime())
print(time.gmtime(0))
# para imprimir a quantidade de segundos desde a contagem inicial do sistema em 01/01/1970 00:00:00 
print(time.time())
1758494056.9189494
# Para trabalhar com bando de dados é recomendado armazenar data e hora utilziando esse formato mais preciso
segundos = time.ctime(1702299273)
print(f'Data: {segundos}')
