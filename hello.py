from flask import Flask
from flask import request
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'iotdb.cesdfiypdndn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'jaynalgenez21K'
app.config['MYSQL_DB'] = 'IOT_TEST'

mysql = MySQL(app)

@app.route('/api/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        return 'Data recived'
    else:
        cur = mysql.connection.cursor()
        #cur.execute('''SELECT user, host FROM mysql.user''')
        cur.execute('''SELECT * FROM IOT_TEST.DUMMY''')
        sel = cur.fetchall()
        cur.close()
        return str(sel)
