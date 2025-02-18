import requests
from config import API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Icon for temp
        icon_code = data["weather"][0]["icon"]
        # URL for icon request
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        return data, icon_url
    return None, None
