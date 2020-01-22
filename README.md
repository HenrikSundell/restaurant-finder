# restaurant-finder
## Running the project
This project is written in Python 3, you should have it installed if you want to run this project.
https://www.python.org/

You can install all the packages needed with this command:
### `pip install -r requirements.txt`
After the packages are installed you should be able to run the project with this command:
### `python app.py`

You might have to use `pip3 install -r requirements.txt` and `python3 app.py` instead, depending on your system.

## or you can try it here

### https://restaurant-finder-wolt.herokuapp.com/

## URL Params

### required:
q=[string]

A querry string for the search e.g. q=pizza

lat=[float]

Latitude coordinate (customer's location) in decimal form e.g. lat=60.1704

lon=[float]

Longitude coordinate (customer's location) in decimal form e.g. lon=24.9322331121
### optional:

max=[float]

Max distance to search for restaurants in km instead of the default 3km e.g. max=0.5 for 0.5km

online=[integer]

By default even offline restaurants are returned if the parameter online is set to 1 (online=1)
only restaurants that are currently online are returned.

## Example querries:

### `/restaurants/search?q=sushi&lat=60.17045&lon=24.93147`
### `/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5`
### `/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5&online=1`

## Try them here:
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5&online=1

## Deployment
The current master branch is deployed using Heroku.
### https://restaurant-finder-wolt.herokuapp.com/

### A note on authorization
To make reviewing easier there is no authorization needed to use this api.
