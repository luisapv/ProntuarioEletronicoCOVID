from config.db import app
from flask import request
from controller import pacienteController

@app.route('/')
def hello_world():
    return 'Teste realizado com suscesso!'

@app.route('/paciente', methods=['GET'])
def paciente_page():
    print('App_ROUTER: paciente_page')
    return "paciente_form.html"

@app.route('/paciente/save', methods=['POST'])
def paciente_novo():
    print('App_ROUTER: paciente_save')

    data = request.form
    print(data)
    return pacienteController.save(data)

@app.route('/paciente/lista', methods=['GET'])
def paciente_lista():
    print('App_ROUTER: paciente_lista')

    return pacienteController.list()