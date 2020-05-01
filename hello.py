from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask import jsonify
from datetime import datetime

import constants as CONSTANTS


app = Flask(__name__, static_folder='front-iot/src/dist/')


app.config['MYSQL_HOST'] = CONSTANTS.DB_HOST
app.config['MYSQL_USER'] = CONSTANTS.DB_USER
app.config['MYSQL_PASSWORD'] = CONSTANTS.DB_PASSWORD
app.config['MYSQL_DB'] = CONSTANTS.DB_NAME

mysql = MySQL(app)

#FRONT END Static files srver
@app.route('/', methods=['GET'])
def stvue():
    return app.send_static_file('index.html')

'''
Hardware and Software connection
'''
@app.route('/api/data', methods=['POST', 'GET'])
def data():
    cur = mysql.connection.cursor()
    date = datetime.now()

    if request.method == 'POST':
        data = str(request.get_data())

        if(data):
            data = data[2:len(data)-3]
            data = data.split(',')
            print(data)

            hw = data[0]
            ph = data[1].split(':')[1]
            temp = data[2].split(':')[1]
            hum = data[3].split(':')[1]
            print(str(ph)  + " - " + str(temp) + " - " + str(hum))

            cur.execute('INSERT INTO IOT_TEST.DATA \
                (idNode, ph, temperature, humidity, day, month, year, times) \
                VALUES ("'+str(hw)+'", \
                '+str(ph)+', \
                '+str(temp)+', \
                '+str(hum)+', \
                '+str(date.day)+', \
                '+str(date.month)+', \
                '+str(date.year)+', \
                "'+str(date)+'")')

            mysql.connection.commit()

    cur.close()
    return '100'

'''
Fetch all data
'''
@app.route('/api/data/all', methods=['POST'])
def api():
    data = str(request.get_data())
    data = data[2:len(data)-1]
    data = data.split(',')
    print("\n\nData: " + str(data))

    cur = mysql.connection.cursor()
    cur.execute(' \
        SELECT n.nodeName, n.plant, d.ph, d.temperature, d.humidity, d.day, d.month, d.year, d.times \
        FROM IOT_TEST.DATA d \
        JOIN IOT_TEST.NODES n ON d.idNode = n.idNode \
        JOIN IOT_TEST.USERS u ON u.idPK = n.idUser \
        WHERE u.username = "'+str(data[0])+'" \
        ORDER BY d.times; \
    ')

    sel = cur.fetchall()
    cur.close()
    return jsonify(sel)

'''
Get current node data based
'''
@app.route('/api/data/current', methods=['POST'])
def current():
    data = str(request.get_data())
    data = data[2:len(data)-1]
    data = data.split(',')
    print("\n\nData: " + str(data))

    cur = mysql.connection.cursor()
    cur.execute('\
        SELECT d.ph, n.phMin, n.phMax, \
               d.temperature, n.tempMin, n.tempMax, \
               d.humidity, n.humMin, n.humMax, \
               n.plant, d.day, d.month, d.year, d.times \
        FROM IOT_TEST.DATA d \
        JOIN IOT_TEST.NODES n ON d.idNode = n.idNode \
        JOIN IOT_TEST.USERS u ON u.idPK = n.idUser \
        WHERE u.username = "'+str(data[0])+'" and n.nodeName = "'+str(data[1])+'" \
        ORDER BY d.times DESC \
        LIMIT 1; \
        ')

    sel = cur.fetchall()
    cur.close()
    print(sel)
    return jsonify(sel)


'''
Weekly average per day
'''
@app.route('/api/data/week', methods=['POST'])
def week():
    data = str(request.get_data())
    data = data[2:len(data)-1]
    data = data.split(',')

    cur = mysql.connection.cursor()
    cur.execute(' \
        SELECT n.nodeName, n.plant, avg(d.ph) as ph, avg(d.temperature) as temp, \
                        avg(d.humidity) as hum, d.day, d.month, d.year, d.times \
        FROM IOT_TEST.DATA d \
        JOIN IOT_TEST.NODES n ON d.idNode = n.idNode \
        JOIN IOT_TEST.USERS u ON u.idPK = n.idUser \
        WHERE u.username = "'+str(data[0])+'" and n.nodeName = "'+str(data[1])+'" \
        GROUP BY d.day, d.month, d.year \
        ORDER BY d.times DESC \
        LIMIT 7; \
        ')
    sel = cur.fetchall()
    cur.close()
    print(sel)
    return jsonify(sel)

'''
Yearly average
'''
@app.route('/api/data/year', methods=['POST'])
def year():
    data = str(request.get_data())
    data = data[2:len(data)-1]
    data = data.split(',')

    cur = mysql.connection.cursor()
    cur.execute(' \
        SELECT avg(d.ph) as ph, avg(d.temperature) \
        as temp, avg(d.humidity) as hum, d.year, d.times \
        FROM IOT_TEST.DATA d \
        JOIN IOT_TEST.NODES n ON d.idNode = n.idNode \
        JOIN IOT_TEST.USERS u ON u.idPK = n.idUser \
        WHERE u.username = "'+str(data[0])+'" and n.nodeName = "'+str(data[1])+'" \
        GROUP BY d.year \
        ORDER BY d.times DESC \
        LIMIT 1; \
        ')
    sel = cur.fetchall()
    print(sel)
    cur.close()
    return jsonify(sel)

'''
Get all nodes by user
'''
@app.route('/api/nodes', methods=['POST'])
def allNodes():
    data = str(request.get_data())
    data = data[2:len(data)-1]
    data = data.split(',')
    print("\n\nData: " + str(data))

    cur = mysql.connection.cursor()
    cur.execute(' \
        SELECT n.nodeName \
        FROM IOT_TEST.NODES n \
        JOIN IOT_TEST.USERS u ON u.idPK = n.idUser \
        WHERE u.username = "'+str(data[0])+'" \
    ')


    sel = cur.fetchall()
    cur.close()
    print(sel)
    return jsonify(sel)

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

#Create new project
@app.route('/api/project', methods=['POST'])
def newProject():

    data = str(request.get_data())
    data = data[2:len(data)-1]
    content = data.split(',')
    print("\n\nData: " + str(content))

    cur = mysql.connection.cursor()
    cur.execute(' \
        SELECT idPK FROM IOT_TEST.USERS u\
        WHERE u.username = "'+content[0]+'"; \
    ')

    usrId = cur.fetchone()

    cur.execute(' \
        INSERT INTO  IOT_TEST.NODES (nodeName, plant, idUser, tempMax, tempMin, phMax, phMin, humMax, humMin) \
          VALUES ( \
            "'+content[1]+'", \
        	"'+content[2]+'", \
            '+str(usrId[0])+', \
            '+content[3]+', \
        	'+content[4]+', \
            '+content[5]+', \
            '+content[6]+', \
            '+content[7]+', \
        	'+content[8]+' \
        ); \
    ')


    mysql.connection.commit()
    cur.close()
    return "200"

#LogUp
@app.route('/api/logup', methods=['POST'])
def logup():

    data = str(request.get_data())
    data = data[2:len(data)-1]
    print("\n\nData: " + data)
    content = data.split(',')

    cur = mysql.connection.cursor()
    cur.execute(' \
        INSERT INTO IOT_TEST.USERS (username, pass, email) \
        VALUES (\
         	"'+str(content[0])+'",\
        	"'+str(content[1])+'",\
        	"'+str(content[2])+'"\
        ); \
    ')

    mysql.connection.commit()
    cur.close()

    return "200"
