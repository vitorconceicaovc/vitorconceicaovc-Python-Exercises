import requests
import datetime

API_URL = "https://api.open-meteo.com/v1/forecast"

# Portugal Coordinates
latitude = 39.6945
longitude = -8.1306

# Obter a data e hora atual
# current_date = datetime.datetime.now()
# https://strftime.org/
current_date = datetime.datetime.now().strftime("%d-%m-%YT%H:%M")
print(f"\nData e hora atual: {current_date}")

# Construir a URL para a API
API_URL_COUNTRY_DATA = f"{API_URL}?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
print(f"\nLink da API para informações do país: {API_URL_COUNTRY_DATA}\n")

# Fazer a requisição à API
response = requests.get(API_URL_COUNTRY_DATA)

# Verificar se a requisição foi bem sucedida
if response.status_code == 200:
    print("Requisição à API bem sucedida!\n")
    data = response.json()
    
    # Obter a temperatura na hora corrente
    # current_hour_index = (current_date.hour + 1) % 24  # Índice da hora corrente

index = 0

for i in range(len(data['hourly']['time'])):
	if data['hourly']['time'][i] == current_date:
		index = i
		break

current_temperature = data['hourly']['temperature_2m'][index]

# Formatar e imprimir a temperatura
print(f"Temperatura na hora corrente em Portugal: {current_temperature} °C")
