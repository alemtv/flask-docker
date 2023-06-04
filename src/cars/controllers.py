from flask import request, jsonify, make_response
from .. import db
from .models import Car
from app import app
from sqlalchemy.exc import IntegrityError

def list_all_cars_controller():
    cars = Car.query.all()
    response = []
    for car in cars: response.append(car.toDict())
    return make_response(jsonify(response), 200)

def create_car_controller():
    args = request.args
    app.logger.info(f'{args =}')
    
    new_car = Car(  name=args.get('name'),
                    year=args.get('year'),
                    make_id=args.get('make_id'),
                    )

    try:
        db.session.add(new_car)
        db.session.commit()
        statusCode=201
    except IntegrityError:
        db.session.rollback()
        statusCode=400
        response = 'Could not save information'

    if new_car.id:
        app.logger.info(f'{new_car =}')
        response = Car.query.get(new_car.id).toDict()

    return make_response(jsonify(response), statusCode)

def retrieve_car_controller(car_id):
    response = Car.query.get(car_id).toDict()
    return make_response(jsonify(response), 200)

def update_car_controller(car_id):
    args = request.args
    car = Car.query.get(car_id)

    car.name = args.get('name')
    car.year = args.get('year')
    db.session.commit()

    response = Car.query.get(car_id).toDict()
    return make_response(jsonify(response), 200)

def delete_car_controller(car_id):
    Car.query.filter_by(id=car_id).delete()
    db.session.commit()

    response = f'Car with Id {format(car_id)} deleted successfully!'
    return make_response(jsonify(response), 200)