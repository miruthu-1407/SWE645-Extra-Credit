from flask import Flask, render_template, request, jsonify
import pymysql
import os

app = Flask(__name__)

# MySQL RDS configuration
DB_HOST = "database-3.cpmwkabzwidn.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "StrongPassword123!"  # Replace with your real password
DB_NAME = "surveydb"

# Route to confirm backend is running
@app.route('/')
def home():
    return "✅ Backend is up and running!"

# Render or submit the survey form
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=True)
        print("Received form data:", form_data)

        # Insert into RDS MySQL
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO surveys (
                        firstName, lastName, streetAddress, city, state, zip,
                        telephoneNumber, email, dateOfSurvey, campusLikes,
                        interestSource, recommendationLikelihood, raffle, comments
                    ) VALUES (
                        %(firstName)s, %(lastName)s, %(streetAddress)s, %(city)s, %(state)s, %(zip)s,
                        %(telephoneNumber)s, %(email)s, %(dateOfSurvey)s, %(campusLikes)s,
                        %(interestSource)s, %(recommendationLikelihood)s, %(raffle)s, %(comments)s
                    )
                """
                cursor.execute(sql, form_data)
                connection.commit()
        finally:
            connection.close()

        return "✅ Survey form submitted successfully!"

    return render_template('survey.html')

# API to return all surveys as JSON
@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    surveys = []
    try:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM surveys")
            surveys = cursor.fetchall()
    finally:
        connection.close()

    return jsonify(surveys)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
