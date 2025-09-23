from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    sample_data = {
        'id': 1,
        'name': 'Sample Data',
        'description': 'This is a sample description.'
    }
    return jsonify(sample_data)