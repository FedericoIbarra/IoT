from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/api/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        return 'Data recived'
    else:
        return 'Hello, World!'
