from flask import Flask, render_template, request, abort, Response
import urllib, json, constants

app = Flask(__name__)

@app.route("/forecast", methods=['GET'])
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


