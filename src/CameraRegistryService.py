from flask import *
from psycopg import *

app = Flask(__name__)


@app.route('/registry', methods=["POST"])
def registry():
    try:

        return Response('{"registry":"success"}', 201)
    except Exception as e:
        return Response('{"registry":"error"}', 500)


@app.route('/remove/<id>', methods=["DELETE"])
def remove_cam():
    try:

        return Response('{"remove":"error"}', 200)
    except Exception as e:
        return Response('{"remove":"error"}', 500)
app.run("0.0.0.0", port=8080)