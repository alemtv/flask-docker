from flask import request, jsonify, make_response
from .. import db
from .models import Maker
from app import app
from sqlalchemy.exc import IntegrityError

def list_all_makers_controller():
    makers = Maker.query.all()
    response = []
    for maker in makers: response.append(maker.toDict())
    return make_response(jsonify(response), 200)

def create_maker_controller():
    args = request.args
    app.logger.info(f'{args =}')
    
    new_maker = Maker(name=args.get('name'))

    try:
        db.session.add(new_maker)
        db.session.commit()
        statusCode = 201
    except IntegrityError:
        db.session.rollback()
        statusCode = 400
        response = 'Could not save information'

    if new_maker.id:
        app.logger.info(f'{new_maker =}')
        response = Maker.query.get(new_maker.id).toDict()

    return make_response(jsonify(response), statusCode)