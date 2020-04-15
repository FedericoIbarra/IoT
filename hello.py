from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask import jsonify

import constants as CONSTANTS


app = Flask(__name__, static_folder='front-iot/src/dist/')


app.config['MYSQL_HOST'] = CONSTANTS.DB_HOST
app.config['MYSQL_USER'] = CONSTANTS.DB_USER
app.config['MYSQL_PASSWORD'] = CONSTANTS.DB_PASSWORD
app.config['MYSQL_DB'] = CONSTANTS.DB_NAME

mysql = MySQL(app)

@app.route('/api/data', methods=['POST', 'GET'])
def data():
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        data = request.stream.read()
        if(data):
            print(data)
            cur.execute('INSERT INTO IOT_TEST.DUMMY (data) VALUES ("'+str(data)+'")')
            mysql.connection.commit()

    cur.close()
    return '100'


@app.route('/api', methods=['GET'])
def api():
    #cur = mysql.connection.cursor()

    if request.method == 'GET':
        #cur.execute('''SELECT * FROM IOT_TEST.DUMMY''')
        #sel = cur.fetchall()
        sel = '{"data": 100}'


    #cur.close()
    return jsonify(str(sel))

@app.route('/', methods=['GET'])
def stvue():
    return app.send_static_file('index.html')

#Login
@app.route('/api/login', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    content = request.get_json()
    print("\ndata: \n"+ str(content) +"\n")

    cur.execute('SELECT username FROM IOT_TEST.USERS u\
        WHERE u.username = "'+content['username']+'" and u.pass = "'+content['password']+'";')

    sel = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return str(sel)



#LogUp
@app.route('/api/logup', methods=['POST'])
def logup():
    cur = mysql.connection.cursor()
    content = request.get_json()
    print("\ndata: \n"+ str(content) +"\n")


    cur.execute('INSERT INTO IOT_TEST.USERS (username, pass, email, plant) VALUES (\
     	"'+str(content['username'])+'",\
    	"'+str(content['password'])+'",\
    	"'+str(content['email'])+'",\
    	"'+str(content['plant'])+'"\
    );')

    mysql.connection.commit()
    cur.close()

    return "200"
