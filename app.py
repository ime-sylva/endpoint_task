from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

# Define a route that takes two query parameters: name and track
@app.route('/info', methods=['GET'])
def get_info():
    # Get query parameters
    name = request.args.get('name')
    track = request.args.get('track')

    # Get current day of the week and UTC time
    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = datetime.datetime.utcnow()

    # Get GitHub URLs for the file being run and full source code
    file_url = os.getenv('GITHUB_FILE_URL')  # Set this environment variable with the file's GitHub URL
    source_code_url = os.getenv('GITHUB_SOURCE_CODE_URL')  # Set this environment variable with the full source code's GitHub URL

    # Validate UTC time (+/- 2 hours)
    utc_offset = current_utc_time - datetime.datetime.now()
    if abs(utc_offset.total_seconds()) > 2 * 60 * 60:
        return jsonify({"error": "UTC time is not within +/- 2 hours of the current time"}), 400

    # Construct the response JSON
    response = {
        "Slack name": ime_sylva,
        "Current day of the week": current_day,
        "Current UTC time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "Track": track,
        "GitHub URL of the file being run": file_url,
        "GitHub URL of the full source code": source_code_url,
        "Status Code": "Success"
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
