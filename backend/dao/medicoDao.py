from config.db import engine
from sqlalchemy.orm import Session
from models.medico import Medico

__session = Session(engine)

def cadastra_medico(medico):
    __session.add(medico)
    __session.commit()

def update_medico(param_medico) :
#    __session.query(Medico).filter(Medico.medico_id==param_medico.medico_id).merge_result()
    __session.merge(param_medico)
    __session.commit()

def delete_medico(param_id) :
    __session.query(Medico).filter(Medico.medico_id==param_id).delete()
    __session.commit()

def lista_medico() :
    return __session.query(Medico).all

def find_medico(param_id) :
    return __session.query(Medico).filter_by(medico_id=param_id).first()

def find_cpf(param_crm) :
    return __session.query(Medico).filter_by(crm=param_crm).first()