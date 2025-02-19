
# 🌤️ Weather App 🌍

A web application that shows the current weather in your city and in several European capitals. You can search for cities and toggle between Celsius and Fahrenheit to view the temperature in your preferred unit! 🌡️

## 🚀 Features

- 🌍 **Your Current Location:** The app automatically detects your location and displays the current weather.
- 🏙️ **Search Cities:** You can search for any city to see the weather forecast.
- 🌡️ **Temperature:** Toggle between Celsius and Fahrenheit to see the temperature in the desired unit.
- 🌆 **European Capitals:** The app displays the weather of some European capitals.

## 🛠️ Technologies Used

- **Python** - The main programming language.
- **Flask** - A framework for building web applications.
- **OpenWeatherMap API** - For fetching weather data.
- **HTML/CSS** - For the user interface.
- **Bootstrap** - For responsive and easy-to-use design.
- **JavaScript** - For managing the temperature unit toggle (Celsius/Fahrenheit).

## 🧰 Installation and Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/AguAlex/weather-app.git
cd weather-app
```

### 2. Create a Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage the dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install all necessary libraries:

```bash
pip install -r requirements.txt
```

### 4. Get an API Key from [OpenWeatherMap](https://openweathermap.org/)

- Sign up for an account on [OpenWeatherMap](https://openweathermap.org/).
- Get your **API Key** from the dashboard.
- Add the **API Key** in the `config.py` file or directly into the code.

### 5. Run the Application

Start the app locally on the development server:

```bash
python app.py
```

Access the app in your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## 🎨 Design

Used **Bootstrap** to create a responsive and modern design, ensuring that the app looks good on any device.

## ⚙️ Project Structure

```
weather-app/
│
├── app.py                # Main Flask application code
├── config.py             # Configuration for API key and other settings
├── requirements.txt      # List of dependencies
├── static/
│   ├── css/
│   │   └── style.css     # Custom CSS file
│   └── js/
│       └── script.js     # JavaScript for interactivity (e.g., temperature unit toggle)
└── templates/
    └── index.html        # Main HTML template
    └── base_layout.html  # Layout
```

## 🛠️ How the App Works

1. **User Location Detection:** The app uses a service to get your current location (e.g., through geolocation).
2. **Weather Data Fetching:** The app makes requests to the **OpenWeatherMap API** to fetch the weather data based on the chosen city.
3. **User Interface:** The app allows users to search for cities and view weather data. It also allows toggling between Celsius and Fahrenheit.

🌟 **Enjoy your weather app experience!** 🌟
