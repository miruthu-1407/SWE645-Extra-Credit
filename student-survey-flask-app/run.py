from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        if request.is_json:
            # If JSON data is sent (Postman or API)
            data = request.get_json()
            print("Received JSON data:", data)
            return jsonify({"message": "Survey data (JSON) received successfully!"}), 200
        else:
            # If form data is sent (From survey.html)
            form_data = request.form.to_dict(flat=True)
            print("Received Form Data:", form_data)

            # Save form data into a CSV file
            file_exists = os.path.isfile('survey_data.csv')
            with open('survey_data.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=form_data.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(form_data)

            return "Survey form submitted successfully!"

    # For GET request, just render the survey form
    return render_template('survey.html')

@app.route('/surveys', methods=['GET'])
def get_surveys():
    surveys = []
    if os.path.exists('survey_data.csv'):
        with open('survey_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                surveys.append(row)
    return jsonify(surveys)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

