from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
api_key = '407f90971905b74d58b93fa147f6a1e0'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    weather_data = get_weather(city)
    if weather_data:
        return render_template('weather.html', weather_data=weather_data)
    else:
        error_message = f"Unable to fetch weather data for {city}. Please make sure the city name is correct and try again."
        return render_template('error.html', error_message=error_message)

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data.get('cod') == 200:
        weather = {
            'city': city,
            'country': data['sys']['country'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
            'icon': data['weather'][0]['icon'],
            'coordinates': {'lon': data['coord']['lon'], 'lat': data['coord']['lat']},
            'timezone': data['timezone']
        }
        return weather
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)