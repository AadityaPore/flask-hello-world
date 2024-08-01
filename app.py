import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World from Aaditya Pore in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://aadis_flask_tut_database_user:YLPHFdNb8zFlr06eH31gczKzUQH5dOBG@dpg-cqlh9cjv2p9s73ardl5g-a/aadis_flask_tut_database")
    conn.close()
    return "Database Succesfully Connected!"
