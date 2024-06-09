import datetime

data_hora_atual = datetime.datetime.now()

data_formatada = data_hora_atual.strftime("%d/%m/%Y")

hora_formatada = data_hora_atual.strftime("%H:%M")

print("Data:", data_formatada)
print("Hora:", hora_formatada)