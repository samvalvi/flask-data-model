"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    user=User.query.all()
    all_users=list(map(lambda x: x.serialize(), user))
    return jsonify(all_users), 200

@app.route('/user/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_user(id):
    specified_user = User.query.get(user_id)
    request_update_user = request.get_json()

    if specified_user is None:
        raise APIException('User not found', status_code=404)
    
    if request.method == 'GET':
        return jsonify(specified_user.serialize()), 200  

    if request.method == 'DELETE':
        db.session.delete(specified_user)
        db.session.commit()
        return jsonify('Successfuly Deleted'), 200
    
    if request.method == 'PUT':
        if 'username' in request_update_user:
            specified_user.username = request_update_user['username']

        if 'first_name' in request_update_user:
            specified_user.first_name = request_update_user['first_name']

        if 'last_name' in request_update_user:
            specified_user.last_name = request_update_user['last_name']

        if 'password' in request_update_user:
            specified_user.password = request_update_user['password']
        
        db.session.commit()

        return jsonify('Successfully Updated'), 200

@app.route('/planet', methods=['GET'])
def get_planets():
    planet=Planet.query.all()
    all_planets=list(map(lambda x: x.serialize(), planet))
    return jsonify(all_planets), 200

@pp.route('/character', methods=['GET'])
def get_characters():
    character=Character.query.all()
    all_characters=list(map(lambda x: x.serialize(), character))
    return jsonify(all_characters), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
