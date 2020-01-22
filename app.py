from flask import Flask,jsonify,request
import json
from math import sin, cos, atan2, pow, sqrt, radians

app = Flask(__name__)

# Reuturn a json error message when 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"ERROR": "Page Not Found"}), 404

@app.route('/restaurants')
def restaurants():
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
    q = request.args.get('q', None)
    lat = request.args.get('lat', None)
    lon = request.args.get('lon', None)

    # Optional URL parameters
    max = request.args.get('max', 3.0) # Max distance instead of 3km
    online = request.args.get('online', 0) # Equal to 1 if only online restaurants should be returned
    # Check if required parameters are found
    if not q or not lat or not lon:
        return jsonify({"ERROR": "Bad Request"}), 400

    # Convert paramter types if possible and Check if they are legal
    try:
        postition = (float(lat), float(lon))
        max = float(max)
        online = int(online)
        if online < 0 or online > 1:
            raise ValueError
    except ValueError:
        return jsonify({"ERROR": "Bad Request"}), 400

    # Get restaurant data from jsonfile
    with open('data/restaurants.json') as json_file:
            data = json.load(json_file)

    restaurants = []
    for r in data['restaurants']:
        if q in r['tags'] or q in r['name'] or q in r['description']:
            # Convert the restaurant cordinates to floats from strings
            rest_cord = [float(i) for i in r['location']]
            rest_cord.reverse()
            dis = get_distance(postition, tuple(rest_cord))
            # Only return the restaurants near by and only online ones if online parameter == 1
            if dis < max and online == 0 or dis < max and r['online']:
                restaurants.append(r)
    return jsonify(restaurants), 200


if __name__ == "__main__":
    app.run(debug=False)