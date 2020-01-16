from flask import Flask,jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/restaurants.json') as json_file:
        data = json.load(json_file)
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)