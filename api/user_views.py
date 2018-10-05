from flask import request, jsonify, Blueprint, make_response
from api.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import swag_from
import datetime
import re

user = Blueprint('user', __name__)

users = []


@user.route('/api/v1/signup', methods=['POST'])
@swag_from('apidocs/users/create_user.yml')
def register_user():
    data = request.get_json()
    if len(data.keys()) == 0:
        return jsonify({"message": "No user added"}), 400

    if data['user_name'] == "":
        return jsonify({"message": "username cannot be blank"}), 400

    if data['email'] == "":
        return jsonify({"message": "Email cannot be blank"}), 400

    if data['password'] == "":
        return jsonify({"message": "password cannot be blank"}), 400

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", data['email']):
        return jsonify({"message": "Invalid email format"}), 400

    if not re.match(r"([a-zA-Z0-9])", data['user_name']):
        return jsonify({
            "message": "Please enter alphanumerical characters for username"
            }), 400

    if re.match(r"([0-9])", data['user_name']):
        return jsonify({
            "message": "user name cannot contain numbers only"}), 400

    if len(data['password']) < 5:
        return jsonify({"message": "Password too short"}), 400

    for user in users:
        if user.email == data['email']:
            return jsonify({"message": "user already exists!"})

        if user.user_name == data['user_name']:
            return jsonify({"message": "User_name already exists"}), 400

    if isinstance(data['user_name'], str):
        user_id = len(users)
        user_id += 1
        hashed_password = generate_password_hash(data['password'],
                                                 method='sha256')
        user = User(user_id, data['user_name'], data['email'], hashed_password)
        users.append(user)
        return jsonify({"message": "User added successfully"}), 201
    return jsonify({"message": "Invalid fields"}), 400


@user.route('/api/v1/users', methods=['GET'])
@swag_from('apidocs/users/get_users.yml')
def get_users():
    """This endpoint fetches all users"""
    Users = [user.get_dict() for user in users]
    return jsonify({"message": Users}), 200
