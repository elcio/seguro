import json
import mysql.connector
from flask import Flask

with open('config.json') as config_file:
    config = json.load(config_file)

mydb = mysql.connector.connect(**config['db'])

app = Flask(__name__)

@app.get('/')
def index():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM pessoa")
    results = [{'id': d[0], 'nome': d[1]} for d in cursor.fetchall()]
    return {"result": results, "status": "success"}
