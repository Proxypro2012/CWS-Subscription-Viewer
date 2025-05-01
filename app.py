from flask import Flask
import requests
import json


app = Flask(__name__)

app.route('/get-subscription-status', methods=['GET'])
def get_subscription_status():
  data = request.get_json()
  person = data.get('person')

  with open("subscription-status.json", 'r') as file:
    status = json.load(file)

  for user in status:
      if user["name"].lower() == person.lower():  # case-insensitive match
          print(f"Found: Name={user['name']}, Status={user['status']},")
          return jsonify({
                "name": user["name"],
                "status": user["status"],
                "expires": user["expires"]
            })

          break
  else:
      print("User not found.")
