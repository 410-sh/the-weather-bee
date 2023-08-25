from flask import Flask, render_template, request, abort, Response, redirect, url_for
import urllib, json, constants

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def homepage():
    if request.method == "POST":
        city = request.form.get('city')
        if not city:
            return "Please provide a city"
        return redirect(url_for('getWeather', city=city))
    return """ 
    <form method="POST">
        <label for="city">Enter a city:</label>
        <input type="text" id="city" name="city">
        <button type="submit">Get Weather</button>
    </form>
    """

@app.route("/forecast", methods=['GET','POST'])
def getWeather():
    city = request.args.get('city')
    if not city:
        abort(400, "No city provided")
    
    data = {}
    data['q'] = request.args.get('city')
    data['appid'] = constants.api_key
    data['units'] = 'imperial'

    url_values = urllib.parse.urlencode(data)
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    full_url = url + '?' + url_values
    data = urllib.request.urlopen(full_url)

    resp = Response(data)
    resp.status_code = 200
    return render_template('index.html', title='The Weather Bee', data=json.loads(data.read().decode('utf-8')))


