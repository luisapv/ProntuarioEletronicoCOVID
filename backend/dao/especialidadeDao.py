from sqlalchemy.sql.expression import false, true
from config.db import engine
from sqlalchemy.orm import Session
from models.especialidade import Especialidade

__session = Session(engine)

def new_especilidade(param_especialidade):
    print('pacienteDAO: new_especilidade')
    __session.add(param_especialidade)
    __session.commit()
#    return find_especialidae(param_especialidade.nome)