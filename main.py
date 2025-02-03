from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # to enable cors for all routes


@app.route("/", methods=["GET"])
def get_info():
    # response dictionary
    response = {
        "email": "Kgkpt2018@gmail.com",
        # figure out UTC datetime last one wasnt correct
        "current_datetime": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Karadumk/hng-api-task",
    }
    return jsonify(response), 200


if __name__ == "__main__":
    # app.run(debug=True)
    # Set host to "0.0.0.0" so the API is accessible externally if deployed
    app.run(host="0.0.0.0", port=5000, debug=True)
