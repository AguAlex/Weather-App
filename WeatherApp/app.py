from flask import Flask, render_template, request
from services.weather_service import get_weather
from services.location_service import get_user_location

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_city = get_user_location()

    if request.method == "POST":
        user_city = request.form["city"]

    weather_data = get_weather(user_city)
    temperature = weather_data["main"]["temp"] if weather_data else "N/A"
    
    return render_template("index.html", city=user_city, temperature=temperature)

if __name__ == "__main__":
    app.run(debug=True)
