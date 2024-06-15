import json
import uuid

from flask import *
from psycopg import *
from db.Database import DatabaseConnect

app = Flask(__name__)


@app.route('/registry', methods=["POST"])
def registry():
    try:
        raw_data = request.data
        data = json.loads(raw_data)
        db = DatabaseConnect()
        conn = db.conn()
        cursor = conn.cursor()
        cursor.execute(f"insert into cameras (uuid, ip) values ({uuid.uuid4()},{data['ip']})")
        cursor.fetchall()
        return Response('{"registry":"success"}', 201)
    except Exception as e:
        try:
            db = DatabaseConnect()
            conn = db.conn()
            cursor = conn.cursor()
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS cameras (CREATE TABLE IF NOT EXISTS cameras(uuid varchar(255),ip_external varchar(255), name varchar(255)))")
            cursor.fetchall()
            return Response('{"registry":"error"}', 500)
        except Exception as err:
            return Response('{"registry":"error"}', 500)


@app.route('/remove/<id>', methods=["DELETE"])
def remove_cam():
    try:

        return Response('{"remove":"error"}', 200)
    except Exception as e:
        return Response('{"remove":"error"}', 500)


@app.route('/get/all')
def get_all():
    try:
        db = DatabaseConnect()
        conn = db.conn()
        cursor = conn.cursor()
        cursor.execute("select * from cameras")
        data = cursor.fetchall()
        raw_data = []
        for elem in data:
            raw_data.append(elem)
        return raw_data
    except Exception as e:
        return Response('[]', 500)


app.run("0.0.0.0", port=8080)
