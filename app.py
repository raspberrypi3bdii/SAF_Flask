from flask import Flask, g
import sqlite3

app = Flask(__name__)

# Configuracion BBDD
DATABASE = "saf_flask_db.db"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        app.logger.info(f"Conectado a la db {db}")
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        app.logger.info(f"Cerrando la DB {db}")
        db.close()


@app.route('/')
def index():
    cur = get_db().cursor()
    return "Hola Mundo"
