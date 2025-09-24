import os
import datetime

os.system('clear')

from datetime import datetime

data_ini_str = input('Por favor, insira a data inicial no formato DD/MM/AAAA (ex: 25/12/2024): ')
try:
    data_ini_obj = datetime.strptime(data_ini_str, "%d/%m/%Y")
    #print(f'Data inicial: {data_ini_obj}')
except ValueError:
    print(f'Formato de data inválido. Por favor, insira no formato DD/MM/AAAA.')

data_fim_str = input('Por favor, insira a data final no formato DD/MM/AAAA (ex: 25/12/2024): ')
try:
    data_fim_obj = datetime.strptime(data_fim_str, "%d/%m/%Y")
    #print(f'Data final: {data_fim_obj}')
except ValueError:
    print(f'Formato de data inválido. Por favor, insira no formato DD/MM/AAAA.')

if data_ini_obj <= data_fim_obj:
    dias = data_fim_obj - data_ini_obj
    print(f'A diferença entre {data_ini_obj.strftime("%d/%m/%Y")} e {data_fim_obj.strftime("%d/%m/%Y")} são {dias.days} dias')
    proxima_troca = data_fim_obj + dias
    print(f'A próxima troca prevista será em {proxima_troca.strftime("%d/%m/%Y")}')
else:
    print('A data inicial é maior que a data final')






