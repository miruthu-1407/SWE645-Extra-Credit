from flask import Flask, request, render_template, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL RDS credentials
DB_HOST = "database-3.cpmtwkabzwidn.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "StrongPassword123!"  # 🔁 REPLACE with your RDS password
DB_NAME = "surveydb"

@app.route('/')
def home():
    return "✅ Flask backend running"

@app.route('/survey', methods=['GET'])
def serve_form():
    return render_template('survey.html')

@app.route('/api/surveys', methods=['POST'])
def submit_survey():
    try:
        form_data = request.form.to_dict()
        
        # Handle checkboxes and multiple values
        campusLikes = request.form.getlist("campusLikes")
        form_data["campusLikes"] = ",".join(campusLikes)

        # Connect to MySQL RDS
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        insert_query = """
            INSERT INTO surveys (
                firstName, lastName, streetAddress, city, state, zip,
                telephoneNumber, email, dateOfSurvey, campusLikes,
                interestSource, recommendationLikelihood, raffle, comments
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            form_data.get('firstName'),
            form_data.get('lastName'),
            form_data.get('streetAddress'),
            form_data.get('city'),
            form_data.get('state'),
            form_data.get('zip'),
            form_data.get('telephoneNumber'),
            form_data.get('email'),
            form_data.get('dateOfSurvey'),
            form_data.get('campusLikes'),
            form_data.get('interestSource'),
            form_data.get('recommendationLikelihood'),
            form_data.get('raffle'),
            form_data.get('comments')
        )

        cursor.execute(insert_query, values)
        connection.commit()
        cursor.close()
        connection.close()

        return "✅ Survey data inserted into MySQL RDS!"
    
    except Exception as e:
        print("❌ Error:", str(e))
        return "Internal Server Error", 500

@app.route('/api/surveys', methods=['GET'])
def fetch_surveys():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM surveys")
        data = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(data)
    except Exception as e:
        print("❌ Error fetching surveys:", str(e))
        return jsonify([]), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
