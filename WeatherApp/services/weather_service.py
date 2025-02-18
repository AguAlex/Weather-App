import requests
from config import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    return None
