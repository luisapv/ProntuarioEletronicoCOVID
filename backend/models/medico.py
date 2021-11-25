from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from .especialidade import Especialidade

class Medico(Base):
    __tablename__ = 'medicos'

    def __init__(self, medico_id, especialidade_id, nome, crm):
        self.__medico_id = medico_id
        self.__especialidade_id = especialidade_id
        self.__nome = nome
        self.__crm = crm

    __medico_id = Column('medico_id', Integer, Sequence('medico_id_seq'), primary_key=True)
    __especialidade_id = Column('especialidade_id', Integer, ForeignKey('models.especialidades.especialidade_id'))
    __nome = Column('nome', String(100))
    __crm = Column('crm', Integer)

    __especialidades = relationship('models.especialidade.Especialidade', back_populates='medicos')
    __prontuarios = relationship("models.prontuario.Prontuario", back_populates="medicos")

    def __repr__(self):
        return f'<Medico(nome={self.__nome}, crm={self.__crm})>'

    def get_medico_id(self):
        return self.__medico_id

    def get_especialidade_id(self):
        return self.__especialidade_id

    def set_especialidade_id(self, especialidade_id):
        self.__especialidade_id = especialidade_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_crm(self):
        return self.__crm

    def set_crm(self, crm):
        self.__crm = crm

    def get_especialidades(self):
        return self.__especialidades
    
    def get_prontuarios(self):
        return self.__prontuarios