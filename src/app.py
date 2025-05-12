from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/get-subscription-status', methods=['GET'])
def get_subscription_status():
    person = request.args.get('person')
    month = request.args.get('month')

    if not person:
        return jsonify({"error": "Missing 'person' parameter"}), 400
    elif not month:
        return jsonify({"error": "Missing 'month' parameter"}), 400

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



@app.route('/get-subscriber-count', methods=['GET'])
def get_subscriber_count():
    try:
        with open("subscription-status.json", 'r') as file:
            data = json.load(file)
        
        count = len(data)
        return jsonify({"subscriber_count": count})
    
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Failed to count subscribers"}), 500



def load_subscribers():
    try:
        with open("subscription-status.json", "r") as file:
            return json.load(file)  # Load the JSON data from the file
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found
    except json.JSONDecodeError:
        return []  # Return an empty list if there's an error decoding the JSON

@app.route('/get-subscriber-list', methods=['GET'])
def get_subscriber_list():
    subscribers = load_subscribers()  # Load the subscriber data
    return jsonify(subscribers)  # Return the list of subscribers as JSON
