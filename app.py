from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

# Define a route that takes two query parameters: name and track
@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week and UTC time
    current_day = datetime.datetime.now().strftime('%A')
    current_utc_time = datetime.datetime.utcnow()

    # Get GitHub URLs for the file being run and full source code
    file_url = 'https://github.com/ime-sylva/endpoint_task/blob/main/app.py'  # Set this environment variable with the file's GitHub URL
    source_code_url = 'https://github.com/ime-sylva/endpoint_task/tree/main'  # Set this environment variable with the full source code's GitHub URL

    # Validate UTC time (+/- 2 hours)
    utc_offset = current_utc_time - datetime.datetime.now()
    if abs(utc_offset.total_seconds()) > 2 * 60 * 60:
        return jsonify({"error": "UTC time is not within +/- 2 hours of the current time"}), 400

    # Construct the response JSON
    response = {
        "slack_name": name,
        "current_day": current_day,
        "utc_time": current_utc_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": file_url,
        "github_repo_url": source_code_url,
        "status_code": 200
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=1)
