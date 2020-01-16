from flask import Flask,jsonify,request
import json
from math import sin, cos, atan2, pow, sqrt, radians

app = Flask(__name__)

@app.route('/')
def index():
    # Get restaurant data from jsonfile
    with open('data/restaurants.json') as json_file:
        data = json.load(json_file)

    return jsonify(data), 200

#calculates distance between to cordinates
#input two tuples with latitude and longitude of the cordinates
#returns the distance between them in kilometers
def get_distance(start, end):
    start_lat, start_lon = radians(start[0]), radians(start[-1])
    end_lat, end_lon = radians(end[0]), radians(end[-1])

    lat_diff = start_lat - end_lat
    lon_diff = start_lon - end_lon

    a = pow(sin(lat_diff/2), 2) + cos(start_lat) * cos(end_lat) * pow(sin(lon_diff/2), 2)
    earth_radius = 6371
    distance = earth_radius * 2* atan2(sqrt(a), sqrt(1 - a))

    return distance


@app.route('/restaurants/search', methods=['GET'])
def search():
    tag = request.args.get('q')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Get restaurant data from jsonfile
    with open('data/restaurants.json') as json_file:
        data = json.load(json_file)

    restaurants = []
    cordinates = (float(lat), float(lon))
    for r in data['restaurants']:
        if tag in r['tags']:
            rest_cord = [float(i) for i in r['location']]
            rest_cord.reverse()
            dis = get_distance(cordinates, tuple(rest_cord))
            print(r['name'], " is : ", dis, " km from you")
            if dis < 3.0:
                restaurants.append(r)
    return jsonify(restaurants), 200


if __name__ == "__main__":
    app.run(debug=True)