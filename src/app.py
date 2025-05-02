from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/get-subscription-status', methods=['GET'])
def get_subscription_status():
    person = request.args.get('person')  # GET param ?person=Kabir

    if not person:
        return jsonify({"error": "Missing 'person' parameter"}), 400

    try:
        with open("subscription-status.json", 'r') as file:
            status = json.load(file)

        for user in status:
            if user["name"].lower() == person.lower():  # case-insensitive match
                return jsonify({
                    "name": user["name"],
                    "status": user["status"],
                    "expires": user["expires"]
                })

        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        print("Server error:", e)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def home():
    return "Backend for CWS"
