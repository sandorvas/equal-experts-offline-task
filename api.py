# api.py
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/gists')
def get_gists():
    username = request.args.get('username', 'octocat')
    
    url = f'https://api.github.com/users/{username}/gists'
    response = requests.get(url)
    
    if response.status_code == 200:
        gists = response.json()
        return jsonify(gists)
    else:
        return jsonify({'error': 'Failed to fetch gists'}), response.status_code

if __name__ == '__main__':
    # Run the Flask app on port 8080
    app.run(debug=True, host='0.0.0.0', port=8080)

