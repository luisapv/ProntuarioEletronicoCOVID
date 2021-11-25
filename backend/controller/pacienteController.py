from logging import log
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import true, false
from flask import jsonify, json, request
from models.paciente import Paciente
from dao import pacienteDao

def save(data) :
    print('pacienteController: paciente_save')

    param_nome, param_cpf = data.get("nome"), data.get("cpf")

#    try :
#        paciente = pacienteDao.find_cpf(param_cpf)
#    except :
#        paciente = None
    
#    if not paciente :
    try :
        paciente = Paciente
        paciente.__nome = param_nome
        paciente.__cpf = param_cpf
        print(paciente.__repr__)
        pacienteDao.new_paciente(paciente)
#            return jsonify(paciente.__repr__)
        return "Cadastrado"
    except Exception as exc:
#            return jsonify({'exception': str(exc)}), 400
        print(exc)
        return "Erro Cadastrar"
#    else :
#        try :
#            paciente.nome = param_nome
#            paciente.cpf = param_cpf
#            pacienteDao.update_paciente(paciente)
#            return jsonify({'Paciente': paciente.__repr__, 'message': 'Paciente successfully created'}), 201
#            return "Editado"
#        except Exception as exc:
#            return jsonify({'exception': str(exc), 'message': 'Paciente not created'}), 400
#            return "Erro Editar"

def list() :
    print('pacienteController: paciente_list')

    return pacienteDao.lista_paciente()