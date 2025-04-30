from flask import Flask, render_template, request, jsonify
import pymysql
import os

app = Flask(__name__)

# MySQL DB config (Update with your real values)
db_config = {
    'host': 'database-3.cpmwkabzwidn.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'YOUR_PASSWORD',  # Replace with your actual password
    'database': 'surveydb'
}

# Health check
@app.route('/')
def home():
    return "✅ Backend is up and running!"

# Survey submission and rendering
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=True)
        print("Received Form Data:", form_data)

        try:
            conn = pymysql.connect(**db_config)
            cursor = conn.cursor()

            sql = """
                INSERT INTO surveys 
                (firstName, lastName, streetAddress, city, state, zip, telephoneNumber, email, dateOfSurvey, campusLikes, interestSource, recommendationLikelihood, raffle, comments)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                form_data.get("firstName"),
                form_data.get("lastName"),
                form_data.get("streetAddress"),
                form_data.get("city"),
                form_data.get("state"),
                form_data.get("zip"),
                form_data.get("telephoneNumber"),
                form_data.get("email"),
                form_data.get("dateOfSurvey"),
                ','.join(request.form.getlist("campusLikes")),
                form_data.get("interestSource"),
                form_data.get("recommendationLikelihood"),
                form_data.get("raffle"),
                form_data.get("comments"),
            )

            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()

            return "✅ Survey data submitted to RDS!"

        except Exception as e:
            return f"❌ Error saving to database: {str(e)}"

    return render_template('survey.html')

# View surveys (API)
@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM surveys")
        surveys = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(surveys)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
