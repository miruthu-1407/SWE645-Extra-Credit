from flask import Blueprint, request, jsonify
from . import db
from .models import StudentSurvey

survey_bp = Blueprint('survey_bp', __name__)

@survey_bp.route('/survey', methods=['POST'])
def create_survey():
    data = request.get_json()
    survey = StudentSurvey(**data)
    db.session.add(survey)
    db.session.commit()
    return jsonify({"message": "Survey created successfully"}), 201

@survey_bp.route('/surveys', methods=['GET'])
def get_surveys():
    surveys = StudentSurvey.query.all()
    return jsonify([{
        "id": s.id,
        "first_name": s.first_name,
        "last_name": s.last_name,
        "email": s.email,
        "telephone": s.telephone
    } for s in surveys])

@survey_bp.route('/survey/<int:id>', methods=['GET'])
def get_survey(id):
    survey = StudentSurvey.query.get_or_404(id)
    return jsonify({
        "id": survey.id,
        "first_name": survey.first_name,
        "last_name": survey.last_name,
        "email": survey.email,
        "telephone": survey.telephone
    })

@survey_bp.route('/survey/<int:id>', methods=['PUT'])
def update_survey(id):
    survey = StudentSurvey.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(survey, key, value)
    db.session.commit()
    return jsonify({"message": "Survey updated successfully"})

@survey_bp.route('/survey/<int:id>', methods=['DELETE'])
def delete_survey(id):
    survey = StudentSurvey.query.get_or_404(id)
    db.session.delete(survey)
    db.session.commit()
    return jsonify({"message": "Survey deleted successfully"})
