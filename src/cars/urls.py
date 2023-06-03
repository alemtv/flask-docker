from flask import request
from app import app
from .controllers import list_all_cars_controller, create_car_controller, retrieve_car_controller, update_car_controller, delete_car_controller

@app.route("/cars", methods=['GET', 'POST'])
def list_create_cars():
    if request.method == 'GET': 
        return list_all_cars_controller()
    elif request.method == 'POST': 
        return create_car_controller()
    else: 
        return 'Method is Not Allowed'

@app.route("/cars/<car_id>", methods=['GET', 'PUT', 'DELETE'])
def retrieve_update_destroy_cars(car_id):
    if request.method == 'GET': 
        return retrieve_car_controller(car_id)
    elif request.method == 'PUT': 
        return update_car_controller(car_id)
    elif request.method == 'DELETE': 
        return delete_car_controller(car_id)
    else: 
        return 'Method is Not Allowed'