from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "OPENWEATHER_API_KEY"  #Change and Put your API_Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.json.get('city')
    if not city:
        return jsonify({'error': 'city not provided'}), 400
    
    params = {
        'q': city,
        'appid': "OPENWEATHER_API_KEY",  #Change and Put your API_Key
        'units': 'metric'
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity']
    }

    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)