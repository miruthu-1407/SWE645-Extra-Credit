from . import db

class StudentSurvey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    street_address = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    survey_date = db.Column(db.String(20), nullable=False)
    liked_most = db.Column(db.String(50), nullable=False)
    interest_source = db.Column(db.String(50), nullable=False)
    recommendation = db.Column(db.String(50), nullable=False)
