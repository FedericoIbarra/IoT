from flask import Flask
from flask import request
from flask_mysqldb import MySQL


app = Flask(__name__, static_folder='front-iot/src/dist/')

app.config['MYSQL_HOST'] = 'iotdb.cesdfiypdndn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'jaynalgenez21K'
app.config['MYSQL_DB'] = 'IOT_TEST'

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
            
    else:
        #cur.execute('''SELECT user, host FROM mysql.user''')
        cur.close()
        return '100'
    

@app.route('/api', methods=['GET'])
def api():
    cur = mysql.connection.cursor()

    if request.method == 'GET':
        cur.execute('''SELECT * FROM IOT_TEST.DUMMY''')
        sel = cur.fetchall()
        return str(sel)

    cur.close()

@app.route('/', methods=['GET'])
def stvue():
    return app.send_static_file('index.html')

