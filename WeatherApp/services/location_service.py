import requests

def get_user_location():
    url = "http://ip-api.com/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["city"]
    return "Bucharest"
