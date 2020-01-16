from flask import Flask,jsonify,request
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Get restaurant data from jsonfile
    with open('data/restaurants.json') as json_file:
        data = json.load(json_file)

    return jsonify(data), 200




@app.route('/restaurants/search', methods=['GET'])
def search():
    tag = request.args.get('q')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # Get restaurant data from jsonfile
    with open('data/restaurants.json') as json_file:
        data = json.load(json_file)

    restaurants = []

    for r in data['restaurants']:
        if tag in r['tags']:
            restaurants.append(r)
    return jsonify(restaurants), 200


if __name__ == "__main__":
    app.run(debug=True)