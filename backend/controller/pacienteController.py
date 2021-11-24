from logging import log
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import true
from models.paciente import Paciente
from dao import pacienteDao
from flask import jsonify, json, request

def save(data) :
    print('pacienteController: paciente_save')

    param_nome, param_cpf = data.get("nome"), data.get("cpf")

    try :
        paciente = pacienteDao.find_cpf(param_cpf)
    except :
        paciente = None
    
    if not paciente :
        try :
            paciente = Paciente(nome = param_nome, cpf = param_cpf, enderecos = None)
            print(paciente.__repr__)
            pacienteDao.new_paciente(paciente)
#            return jsonify(paciente.__repr__)
            return "Cadastrado"
        except Exception as exc:
#            return jsonify({'exception': str(exc)}), 400
            print(exc)
            return "Erro"
    else :
        try :
            paciente.nome = param_nome
            paciente.cpf = param_cpf
            pacienteDao.update_paciente(paciente)
            return jsonify({'Paciente': paciente.__repr__, 'message': 'Paciente successfully created'}), 201
        except Exception as exc:
            return jsonify({'exception': str(exc), 'message': 'Paciente not created'}), 400

def list() :
    print('pacienteController: paciente_list')

    return pacienteDao.lista_paciente()