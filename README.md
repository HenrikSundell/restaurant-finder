# restaurant-finder
## running the project
To run this project you need to have python3 installed on your computer. If you don't have it installed
you can find it at https://www.python.org/

You can install all the packages needed with this command:
### `pip install -r requirements.txt`
After the packages are installed you should be able to run the project with this command:
### `python app.py`

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

Max distance to search for restaurnats in km instead of the defaut 3km e.g max=0.5 for 0.5km 

status=[integer]

By default only restaurants that are online are reutrned if ofline should be included add the parameter: status=0

## Example querries:

### `/restaurants/search?q=sushi&lat=60.17045&lon=24.93147`
### `/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5`
### `/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5&status=0`

## Try them here:
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=sushi&lat=60.17045&lon=24.93147
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5
### https://restaurant-finder-wolt.herokuapp.com/restaurants/search?q=pizza&lat=60.17045&lon=24.93147&max=0.5&status=0

## Deployment
The current master branch is deployed using heroku.
### https://restaurant-finder-wolt.herokuapp.com/

### A note on authorization
To make reviewing easier there is no authorization needed to use this api.
