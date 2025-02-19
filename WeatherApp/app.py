from flask import Flask, render_template, request
from services.weather_service import get_weather
from services.location_service import get_user_location

app = Flask(__name__)
European_Capitals = ["London", "Paris", "Berlin", "Rome", "Madrid", "Amsterdam", "Vienna", "Warsaw"]

@app.route("/", methods=["GET", "POST"])
def index():
    user_city = get_user_location()

    if request.method == "POST":
        user_city = request.form["city"]

    weather_data, icon_url = get_weather(user_city)
    temperature = weather_data["main"]["temp"] if weather_data else "N/A"

    capitals_weather = []
    for city in European_Capitals:
        weather, _ = get_weather(city)
        if weather:
            capitals_weather.append({
                "city": city,
                "temperature": weather["main"]["temp"]
            })
    
    return render_template("index.html", city=user_city, temperature=temperature, icon_url=icon_url, capitals_weather=capitals_weather)

if __name__ == "__main__":
    app.run(debug=True)
