from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  
from os import environ

app = Flask(__name__)
CORS(app) 
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def json(self):
        return {"id": self.id, "name": self.name, "email": self.email}
    
db.create_all()

# create a test route
@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "You have reached the test route"})

# create a user
@app.route('api/flask/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.json()), 201
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# get all users
@app.route('api/flask/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.json() for user in users]), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# get a user by id
@app.route('api/flask/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return jsonify(user.json()), 200
        
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# update a user by id
@app.route('api/flask/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return jsonify({"message": "User updated"}), 200
        
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

# delete a user by id
@app.route('api/flask/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted"}), 200
        
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500