from flask import request, jsonify, make_response
import uuid
from .. import db
from .models import Car
from app import app

def list_all_cars_controller():
    cars = Car.query.all()
    response = []
    for car in cars: response.append(car.toDict())
    return jsonify(response)

def create_car_controller():
    message = 'Done'
    args = request.args
    try:
        new_car = Car(name=args.get('name'),year=args.get('year'))
        db.session.add(new_car)
        db.session.commit()
        statusCode=201
    except:
        statusCode=500
        message = 'Could not save information'

    # # response = Car.query.get(id).toDict()
    data = {'message': message}
    return make_response(jsonify(data), statusCode)

def retrieve_car_controller(car_id):
    response = Car.query.get(car_id).toDict()
    return jsonify(response)

def update_car_controller(car_id):
    request_form = request.form.to_dict()
    car = Car.query.get(car_id)

    car.name = request_form['name']
    car.year = request_form['year']
    db.session.commit()

    response = Car.query.get(car_id).toDict()
    return jsonify(response)

def delete_car_controller(car_id):
    Car.query.filter_by(id=car_id).delete()
    db.session.commit()

    return ('Car with Id "{}" deleted successfully!').format(car_id)