from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

user_name = "naveennekkanti"
roll_number = "AP21110010959"
email = "naveen_nekkanti@srmap.edu.in"

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    highest_alphabet = sorted(alphabets, reverse=True)[:1] if alphabets else []
    
    response = {
        "is_success": True,
        "user_id": f"{user_name}_{roll_number}",
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": highest_alphabet
    }
    
    return jsonify(response)

# GET Method to return a hardcoded operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        "operation_code": 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
