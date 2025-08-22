import requests
from django.shortcuts import render
from datetime import datetime


def index(request):
    data = {}
    city = ""

    if request.method == "POST":
        city = request.POST.get("city")

        # Direct API key here (⚠️ not safe for production!)
        api_key = "9eaac3b0270973148a26ae70c6443059"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            json_data = response.json()

            sunrise = datetime.fromtimestamp(json_data["sys"]["sunrise"]).strftime("%H:%M:%S")
            sunset = datetime.fromtimestamp(json_data["sys"]["sunset"]).strftime("%H:%M:%S")

            data = {
                "city": json_data["name"],
                "country": json_data["sys"]["country"],
                "coordinate": f"{json_data['coord']['lat']}°, {json_data['coord']['lon']}°",
                "temp": round(json_data["main"]["temp"], 1),
                "feels_like": round(json_data["main"]["feels_like"], 1),
                "temp_min": round(json_data["main"]["temp_min"], 1),
                "temp_max": round(json_data["main"]["temp_max"], 1),
                "pressure": json_data["main"]["pressure"],
                "humidity": json_data["main"]["humidity"],
                "visibility": json_data.get("visibility", "N/A"),
                "wind_speed": json_data["wind"]["speed"],
                "wind_deg": json_data["wind"].get("deg", "N/A"),
                "weather": json_data["weather"][0]["description"].title(),
                "icon": json_data["weather"][0]["icon"],
                "sunrise": sunrise,
                "sunset": sunset,
                "time": datetime.fromtimestamp(json_data["dt"]).strftime("%Y-%m-%d %H:%M:%S"),
            }

        except requests.exceptions.RequestException:
            data = {"error": "Weather service unavailable. Please try again."}
        except KeyError:
            data = {"error": "Invalid response. Please check the city name."}

    return render(request, "index.html", {"city": city, "data": data})
