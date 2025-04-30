from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

# ✅ Health check route
@app.route('/')
def home():
    return "✅ Backend is up and running!"

# ✅ Test API endpoint to verify backend is accessible
@app.route('/ping')
def ping():
    return "pong"

# ✅ Survey form route (GET: render form, POST: save data)
@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print("Received JSON data:", data)
            return jsonify({"message": "Survey data (JSON) received successfully!"}), 200
        else:
            form_data = request.form.to_dict(flat=True)
            print("Received Form Data:", form_data)

            # Save form data to CSV
            file_exists = os.path.isfile('survey_data.csv')
            with open('survey_data.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=form_data.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(form_data)

            return "✅ Survey submitted successfully!"

    return render_template('survey.html')  # GET: render form

# ✅ API route to fetch survey data
@app.route('/api/surveys', methods=['GET'])
def get_surveys():
    surveys = []
    if os.path.exists('survey_data.csv'):
        with open('survey_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                surveys.append(row)
    return jsonify(surveys)

# ✅ Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
