from logging import log
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import true
from models.especialidade import Especialidade
from dao import especialidadeDao
from flask import jsonify, json, request

def save(data) :
    print('especialidadeController: save')

    param_nome, param_descricao = data.get("nome"), data.get("descricao")

#    try :
#        especialidade = especialidadeDao.find_nome(param_nome)
#    except :
    especialidade = None
    
    if not especialidade :
        try :
            paciente = Especialidade(nome = param_nome, descricao = param_descricao)
            print(especialidade.__repr__)
            especialidadeDao.new_paciente(especialidade)
#            return jsonify(especialidade.__repr__)
            return "Cadastrado"
        except Exception as exc:
#            return jsonify({'exception': str(exc)}), 400
            print(exc)
            return "Erro Cadastrar"
    else :
        try :
            especialidade.nome = param_nome
            especialidade.descricao = param_descricao
            especialidadeDao.update_especialidade(especialidade)
#            return jsonify({'Especialidade': especialidade.__repr__, 'message': 'Especialidae successfully created'}), 201
            return "Editado"
        except Exception as exc:
#            return jsonify({'exception': str(exc), 'message': 'Especialidae not created'}), 400
            return "Erro Editar"