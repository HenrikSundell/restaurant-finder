from app import app, get_distance
from jsonschema import validate
import json

def test_get_distance():
    d1 = get_distance((59.990967, 24.463767), (60.993223, 25.463767))
    d2 = get_distance((60.17045, 24.93147), (60.16898783926865, 24.939225018024445))
    d3 = get_distance((60.16923121347787, 24.944517016410828), (60.16898783926865, 24.939225018024445))
    d4 = get_distance((59.990967, 24.463767), (59.990967, 24.463767))
    # Distances compared to a online calculator https://gps-coordinates.org/distance-between-coordinates.php
    assert round(d1) == 124
    assert round(d2,3) == 0.459
    assert round(d3,3) == 0.294
    assert d4 == 0.0

def test_if_search_returns_valid_json():
    response = app.test_client().get('/restaurants/search?q=sushi&lat=60.17045&lon=24.93147')
    data = json.loads(response.get_data(as_text=True))

    schema =  {} # If this passes it is valid JSON as {} means any JSON
    return validate(data, schema)

def test_search():
    # Test if a querry return some restourants
    response = app.test_client().get('/restaurants/search?q=sushi&lat=60.17045&lon=24.93147')
    data = json.loads(response.get_data(as_text=True))
    assert len(data) > 0
    # Test if no restaurants are returned when searching for food that does not exist
    response = app.test_client().get('/restaurants/search?q=notfoodfood&lat=60.17045&lon=24.93147')
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 0
    # Test if no restourants are returned if cordinates are more tha 3km from any restaurants
    response = app.test_client().get('/restaurants/search?q=sushi&lat=60.17045&lon=25.93147')
    data = json.loads(response.get_data(as_text=True))
    assert len(data) == 0


