from sqlalchemy.sql.expression import false, true
from config.db import engine
from sqlalchemy.orm import Session
from models.paciente import Paciente

__session = Session(engine)

def new_paciente(param_paciente):
    print('pacienteDAO: new_paciente')
    __session.add(param_paciente)
    __session.commit()
#    return find_cpf(param_paciente.cpf)

def update_paciente(param_paciente) :
    print('pacienteDAO: update_paciente')
#    __session.query(Paciente).filter(Paciente.paciente_id==param_paciente.paciente_id).merge_result()
    __session.merge(param_paciente)
    __session.commit()
    return find_cpf(param_paciente.cpf)

def delete_paciente(param_id) :
    print('pacienteDAO: delete_paciente')
    __session.query(Paciente).filter(Paciente.paciente_id==param_id).delete()
    __session.commit()

def lista_paciente() :
    print('pacienteDAO: lista_paciente')
    return __session.query(Paciente).all()

def find_paciente(param_id) :
    print('pacienteDAO: find_paciente')
    return __session.query(Paciente).filter_by(Paciente.paciente_id==param_id).one()

def find_cpf(param_cpf) :
    print('pacienteDAO: find_cpf')
    return __session.query(Paciente).filter_by(cpf=param_cpf).first()