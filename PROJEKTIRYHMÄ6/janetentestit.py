import random
import mysql.connector
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import json
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def get_db_connection_oma():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="niittykuja4MAR",
        database="flight_game",
        collation='latin1_swedish_ci',
        autocommit=True
    )


@app.route('/hae_nimi/')
def hae_asiakkaan_nimi_oma(person_id):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = f"SELECT nimi FROM person WHERE id = '{person_id}'"
    cursor.execute(query)
    nimi = cursor.fetchone()
    conn.close()

    ans = {
        "nimi":nimi
    }
    json_ans = json.dumps(ans)
    response = Response(response=json_ans, status=200, mimetype="application/json")
    response.headers["Content-Type"] = "charset=utf-8"
    return ans

@app.route('/')
def hae_kysymys_oma(person_id, order_nro):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = f"SELECT question FROM question WHERE person_id = %s AND Order_No = %s"
    cursor.execute(query, (person_id, order_nro))
    kysymys = cursor.fetchone()
    conn.close()

    ans = {
        "kysymys":kysymys
    }
    json_ans = json.dumps(ans)
    response = Response(response=json_ans, status=200, mimetype="application/json")
    response.headers["Content-Type"] = "charset=utf-8"
    return ans







if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)