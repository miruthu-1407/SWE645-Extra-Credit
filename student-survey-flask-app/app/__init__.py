from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:StrongPassword123!@database-3.cpmwkabzwidn.us-east-1.rds.amazonaws.com/database-3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import survey_bp
    app.register_blueprint(survey_bp)

    return app
