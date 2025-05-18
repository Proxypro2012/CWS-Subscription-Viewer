from flask import Flask, request, jsonify
import json
from functools import wraps

app = Flask(__name__)

def load_data():
    try:
        # Open the correct file where user data is stored
        with open('subscription-status.json', 'r') as file:
            data = json.load(file)
            return data["organizations"]  # Ensure the structure is correct in your JSON file
    except FileNotFoundError:
        return {"error": "Data file not found"}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON file"}

# Decorator for authentication
def require_login(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.get_json() or {}
        username = auth.get("username")
        password = auth.get("password")

        orgs = load_data()
        matched_org = next((org for org in orgs if org["username"] == username and org["password"] == password), None)

        if not matched_org:
            return jsonify({"error": "Not logged in"}), 401

        return f(matched_org, auth, *args, **kwargs)
    return wrapper

@app.route('/')
def home():
    return "Backend for CWS"

@app.route('/login', methods=['POST'])
def login():
    creds = request.get_json() or {}
    username = creds.get("username")
    password = creds.get("password")

    orgs = load_data()
    org = next((o for o in orgs if o["username"] == username and o["password"] == password), None)

    if org:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

@app.route('/get-subscription-status', methods=['POST'])
@require_login
def get_subscription_status(org, data):
    person = data.get('person')
    year = data.get('year')
    month = data.get('month')

    if not person or not year or not month:
        return jsonify({"error": "Missing one or more of: person, year, month"}), 400

    month = month.strip().capitalize()

    for user in org["users"]:
        if user["name"].lower() == person.lower():
            year_data = user["subscriptions"].get(year)
            if not year_data:
                return jsonify({"error": f"No data for year: {year}"}), 404

            month_data = year_data.get(month)
            if not month_data:
                return jsonify({"error": f"No data for month: {month}"}), 404

            return jsonify({
                "name": user["name"],
                "year": year,
                "month": month,
                "status": month_data["status"],
                "expires": month_data["expires"]
            })
    return jsonify({"error": "User not found"}), 404

@app.route('/get-subscriber-count', methods=['POST'])
@require_login
def get_subscriber_count(org, data):
    return jsonify({"subscriber_count": len(org["users"])})

@app.route('/get-subscriber-list', methods=['POST'])
@require_login
def get_subscriber_list(org, data):
    return jsonify(org["users"])

@app.route('/get-subscriber-years', methods=['POST'])
@require_login
def get_subscriber_year(org, data):
    person = data.get('person')
    if not person:
        return jsonify({"error": "Missing 'person' parameter"}), 400

    for user in org["users"]:
        if user["name"].lower() == person.lower():
            years = list(user.get("subscriptions", {}).keys())
            return jsonify({"person": user["name"], "years": years})

    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
