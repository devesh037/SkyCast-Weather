from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_msg = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = "3f367154128a43b88e8174126252612"
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if "current" in data:
                weather_data = {
                    'city': data['location']['name'],
                    'temp': data['current']['temp_c'],
                    'desc': data['current']['condition']['text'],
                    'icon': data['current']['condition']['icon']
                }
            else:
                error_msg = "❌ Shehar nahi mila. Spelling check karein!"
        except:
            error_msg = "❌ Internet connection check karein."
            
    return render_template('index.html', weather=weather_data, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)