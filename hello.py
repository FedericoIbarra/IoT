from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask import jsonify
from datetime import date

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
            cur.execute('INSERT INTO IOT_TEST.DUMMY (data) \
                VALUES ("'+str(data)+'")')
            mysql.connection.commit()

    cur.close()
    return '100'


@app.route('/api/data/all', methods=['GET'])
def api():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM IOT_TEST.data''')
    sel = cur.fetchall()
    #sel = '{"data": 100}'
    cur.close()
    return jsonify(sel)

@app.route('/api/data/current', methods=['GET'])
def current():
    cur = mysql.connection.cursor()
    cur.execute('''\
        SELECT ph, temperature, times\
        FROM IOT_TEST.data\
        ORDER BY times\
        LIMIT 1;''')

    sel = cur.fetchall()
    #sel = '{"data": 100}'
    cur.close()
    return jsonify(sel)

@app.route('/api/data/week', methods=['GET'])
def week():
    cur = mysql.connection.cursor()
    cur.execute('''\
        SELECT idHw, AVG(ph )as pH, AVG(temperature) as Temperature, day, month, year, times\
        FROM IOT_TEST.data\
        GROUP BY day, month, year\
        ORDER BY times\
        LIMIT 5;''')
    sel = cur.fetchall()
    #sel = '{"data": 100}'
    cur.close()
    return jsonify(sel)

@app.route('/', methods=['GET'])
def stvue():
    return app.send_static_file('index.html')

#Login
@app.route('/api/login', methods=['POST'])
def login():

    data = str(request.get_data())
    data = data[2:len(data)-1]
    print("\n\nData: " + data)
    content = data.split(',')

    cur = mysql.connection.cursor()
    cur.execute('SELECT username FROM IOT_TEST.USERS u\
        WHERE u.username = "'+content[0]+'" and u.pass = "'+content[1]+'";')

    sel = cur.fetchone()
    mysql.connection.commit()
    cur.close()

    if(sel):
        result = str(sel[0])
    else:
        result= "Wrong data"

    print(result + "\n")
    return result



#LogUp
@app.route('/api/logup', methods=['POST'])
def logup():

    data = str(request.get_data())
    data = data[2:len(data)-1]
    print("\n\nData: " + data)
    content = data.split(',')

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO IOT_TEST.USERS (username, pass, email, plant) \
    VALUES (\
     	"'+str(content[0])+'",\
    	"'+str(content[1])+'",\
    	"'+str(content[2])+'",\
    	"'+str(content[3])+'"\
    );')

    mysql.connection.commit()
    cur.close()

    return "200"
