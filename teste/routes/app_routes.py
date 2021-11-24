from config.db import app
from flask import request

@app.route('/')
def hello_world():
    return 'Teste realizado com suscesso!'