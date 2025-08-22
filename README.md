# 🌦️ Django Weather App

A simple weather application built with **Django** that fetches real-time weather data from external APIs and displays it on a clean HTML page.

## 🚀 Features
- Search for weather by city name.
- Fetches real-time weather data from a weather API (e.g., OpenWeatherMap).
- Displays temperature, humidity, weather condition, and more.
- Simple and minimal HTML template for UI.

  ## 📸 Screenshot

![Weather App Screenshot](/screenshot.png)


## 🛠️ Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (basic styling)
- **API**: OpenWeatherMap API (or any weather API you are using)

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/your-username/django-weather-app.git
   cd django-weather-app
   
Create a virtual environment:
python -m venv venv

source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

Install dependencies:
pip install -r requirements.txt
Add your weather API key in settings.py or .env file.

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

Open in browser:
http://127.0.0.1:8000/

🔑 API Key Setup
Sign up at OpenWeatherMap (or your chosen provider).

Get your API key.
Add it to your Django settings or an .env file:
WEATHER_API_KEY=your_api_key_here
