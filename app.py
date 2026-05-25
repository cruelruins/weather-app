from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

@app.route("/weather", methods=["GET"])
def get_weather():

    city = request.args.get("city")

    # Virhe: käyttäjä ei kirjoita mitään
    if not city:
        return jsonify({
            "error": "Kaupungin nimi puuttuu"
        }), 400

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric&lang=fi"
    )

    try:
        response = requests.get(url)

        # Virhe: API ei vastaa oikein
        if response.status_code != 200:
            return jsonify({
                "error": "Kaupunkia ei löydy tai API-virhe"
            }), 404

        data = response.json()

        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }

        return jsonify(weather_data)

    except requests.exceptions.RequestException:
        return jsonify({
            "error": "Sääpalveluun ei saada yhteyttä"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)