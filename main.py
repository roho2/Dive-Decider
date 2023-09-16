# stormglass.io API key - f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002 (10 requests/day)
# I want to create a program that allows you to choose a dive site and get back a response that says
# If it is a good day to dive or not based on data from stormglass.io. It will provide surf conditions.
import requests
import arrow

if __name__ == "__main__":
    start = arrow.now().floor('day')
    end = arrow.now().shift(days=1).floor('day')

    response = requests.get(
        'https://api.stormglass.io/v2/tide/extremes/point',
        params={
            'lat': 26.2055,
            'lng': -80.0851,
            'start': start.to('UTC').timestamp(),  # Convert to UTC timestamp
            'end': end.to('UTC').timestamp(),  # Convert to UTC timestamp
        },
        headers={
            'Authorization': 'f23856c2-543b-11ee-a654-0242ac130002-f2385780-543b-11ee-a654-0242ac130002'
        }
    )
    json_data = response.json()
    for i in json_data:
        print(i, ":", json_data[i])

