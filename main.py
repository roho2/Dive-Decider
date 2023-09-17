# stormglass.io API key - f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002 (10 requests/day)
# I want to create a program that allows you to choose a dive site and get back a response that says
# If it is a good day to dive or not based on data from stormglass.io. It will provide surf conditions.

# Tech ideas, Django for web. MySQL or PostgreSQL to store data (dive sites?, even users info (fav dive sites?)).
# Django ORM help database operations by allowing you to interact using python objects
# Host on AWS or Heroku?
# OAuth or JWT for authentication. pytest to test code?

# If I were to do an app, I would probably do it all with just AWS and Python Lambdas lol
# Run a SUPER light app
# You can use API gateway to handle the API calls and routing, DynamoDB for your database,
# and just use Python Lambdas to handle your backend service code

# Start: 9/15/2023
# Spent about 3 hours so far

from flask import Flask
import requests

import arrow
import json
import pprint

start = arrow.now().floor('day')
end = arrow.now().ceil('day')

# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#
# app.run()

if __name__ == "__main__":

    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': 26.2055,
            'lng': -80.0851,
            'params': ['waveHeight', 'waterTemperature', 'wavePeriod', 'windWaveHeight', 'windSpeed',
                       'currentDirection', 'currentSpeed', 'visibility'],
            'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
            'end': end.to('UTC').timestamp(),  # Convert to UTC timestamp
            # waveHeight is in meters
            # It's only printing waveHeight for now, ugh.
        },
        headers={
            'Authorization': 'f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002'
        }
    )

    if response.status_code == 200:
        json_data_response = response.json()
        print(json_data_response)
        print("-------------------------------------------------------")
        json_data = json.loads(response.text)  # json_data is a dictionary
        pprint.pprint(json_data)
        # as an example of how to get the data (this is not real variable names from API
        # name = json_data['name']
        # print(f"{name} is the name")
    else:
        print(f"Error:  {response.status_code}")  # Formatted string literal. contain replacement filed

    # for i in json_data:
    #     print(i, ":", json_data[i])
