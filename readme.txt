                equal-experts-offline-task

                      Description:

This solution includes a Dockerfile, Python code, and a requirements.txt file.

+--------------------------------------------------------------------+
+---                      Dockerfile                              ---+
+--------------------------------------------------------------------+
FROM python:3.9-slim

WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "api.py"]

+--------------------------------------------------------------------+

requirements.in:

flask
requests
werkzeug
pytest

+--------------------------------------------------------------------+

$ pip-compile requirements.in
  It created the following requirements.txt:

attrs==23.2.0
blinker==1.7.0
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
flask==3.0.3
idna==3.7
iniconfig==2.0.0
itsdangerous==2.2.0
jinja2==3.1.3
markupsafe==2.1.5
packaging==24.0
pluggy==1.5.0
py==1.11.0
pytest==6.2.5
requests==2.31.0
toml==0.10.2
urllib3==2.2.1
werkzeug==3.0.2

+--------------------------------------------------------------------+
+---                Python Code  (api.py)                         ---+
+--------------------------------------------------------------------+

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

+--------------------------------------------------------------------+
+---                Python Code  (test_api.py)                    ---+
+--------------------------------------------------------------------+
import requests

def test_get_gists():
    response = requests.get('http://localhost:8080/gists')
    assert response.status_code == 200
    gists = response.json()
    assert isinstance(gists, list)

+--------------------------------------------------------------------+
+---                      How to use it                           ---+
+--------------------------------------------------------------------+
1. Set Up Virtual Environment (Optional but Recommended)

$ python3 -m venv venv
$ source venv/bin/activate

2. Clone the Repository

$ git clone https://github.com/sandorvas/equal-experts-offline-task.git 
$ cd equal-experts-offline-task

3. Install Dependencies

$ pip install -r requirements.txt

4. Build Docker Image

$ docker build -t ee-task-image .

5. Create Docker Container

$ docker run -d -p 8080:8080 --name ee-task-container ee-task-image

6. Run Tests with pytest

$ pytest

7. Check Docker Logs

$ docker logs ee-task-container

8. Access the Application

Open a web browser and navigate to http://localhost:8080/gists to access the application.

