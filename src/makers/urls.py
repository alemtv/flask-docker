from flask import request
from app import app
from .controllers import list_all_makers_controller, create_maker_controller

@app.route("/makers", methods=['GET', 'POST'])
def list_create_makers():
    if request.method == 'GET': 
        return list_all_makers_controller()
    elif request.method == 'POST': 
        return create_maker_controller()
    else: 
        return 'Method is Not Allowed'