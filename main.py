# stormglass.io API key - f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002 (10 requests/day)

# Host on AWS or Heroku?
# OAuth or JWT for authentication. pytest to test code?

# Start: 9/15/2023
# Spent about 5 hours so far
# Landing page image: Image by joakant from Pixabay

# Search for best dive conditions and create a list of variables we NEED to get, and what
# nominal values are for those variables (etc. wave height: 1-2ft (not actually nominal idk)).

from flask import Flask, render_template, request, redirect, url_for
import requests

import arrow
import json
import pprint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST'])
def weather():
    selected_location = request.form.get('location')  # Is this the DOM? I forgot
    # Make API call here to gather info using location info
    return render_template('weather.html', weather_info=selected_location)


start = arrow.now().floor('day')
end = arrow.now().ceil('day')

if __name__ == "__main__":

    app.run()

    # response = requests.get(
    #     'https://api.stormglass.io/v2/weather/point',
    #     params={
    #         'lat': 26.2055,
    #         'lng': -80.0851,
    #         'params': ['waveHeight', 'waterTemperature', 'wavePeriod', 'windWaveHeight', 'windSpeed',
    #                    'currentDirection', 'currentSpeed', 'visibility'],
    #         'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
    #         'end': end.to('UTC').timestamp(),  # Convert to UTC timestamp
    #         # waveHeight is in meters
    #         # It's only printing waveHeight for now, ugh.
    #     },
    #     headers={
    #         'Authorization': 'f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002'
    #     }
    # )

    # if response.status_code == 200:
    #     json_data_response = response.json()
    #     print(json_data_response)
    #     print("-------------------------------------------------------")
    #     json_data = json.loads(response.text)  # json_data is a dictionary
    #     pprint.pprint(json_data)
    #     # as an example of how to get the data (this is not real variable names from API
    #     # name = json_data['name']
    #     # print(f"{name} is the name")
    # else:
    #     print(f"Error:  {response.status_code}")  # Formatted string literal. contain replacement filed

    # for i in json_data:
    #     print(i, ":", json_data[i])
