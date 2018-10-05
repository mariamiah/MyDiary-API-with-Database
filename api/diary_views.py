from flask import Blueprint, jsonify, request
from api.models import Diary
from datetime import datetime
from flasgger import swag_from

diary = Blueprint('diary', __name__)

diaries = []


@diary.route('/api/v1/diaries', methods=['POST'])
@swag_from('apidocs/diaries/create_diary.yml')
def create_diary():
    """ Adds a new diary to the system """
    data = request.get_json()
    if data['diary_name'] in diaries:
        return jsonify({"message": "Diary exists already!"}), 400
    if data['diary_name'] == "":
        return jsonify({"message": "diary_name cannot be blank"}), 400
    if isinstance(data['diary_name'], str):
        diary_id = len(diaries)
        diary_id += 1
        date_created = datetime.now()
        diary = Diary(diary_id, data['diary_name'], date_created)
        diaries.append(diary)
    return jsonify({"message": "New diary added successfully"}), 201


@diary.route('/api/v1/diaries', methods=['GET'])
@swag_from('apidocs/diaries/get_all_diaries.yml')
def fetch_diaries():
    """ This endpoint fetches all diaries """
    Diaries = [diary.serialize() for diary in diaries]
    return jsonify({"Diaries": Diaries}), 200


@diary.route('/api/v1/diaries/<int:diary_id>', methods=['GET'])
@swag_from('apidocs/diaries/get_one_diary.yml')
def fetch_diary_by_id(diary_id):
    """Returns one diary specified by the id"""
    fetched_diary = []
    if diary_id != 0 and diary_id <= len(diaries):
        diary = diaries[diary_id - 1]
        fetched_diary.append(diary.serialize())
        return jsonify({'Diary': fetched_diary, 'status': 'Succeeded'}), 200

    if diary_id == 0 or diary_id > len(diaries):
        return jsonify({"message": "Index out of range"}), 400


@diary.route('/api/v1/diaries/<int:diary_id>', methods=['DELETE'])
@swag_from('apidocs/diaries/delete_diary.yml')
def delete_diary(diary_id):
    if diary_id == 0 or diary_id > len(diaries):
        return jsonify({"message": "Index out of range"}), 400
    for diary in diaries:
        if diary.diary_id == diary_id:
            diaries.remove(diary)
    return jsonify({"message": "Diary deleted successfully"}), 200
