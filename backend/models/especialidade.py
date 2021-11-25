from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text
from sqlalchemy.orm import relationship
from .medico import Medico

class Especialidade(Base):
    __tablename__ = 'especialidades'

    def __init__(self, medico_id, nome, descricao):
        self.__medico_id = medico_id
        self.__nome = nome
        self.__descricao = descricao

    __especialidade_id = Column('especialidade_id', Integer, Sequence('especialidade_id_seq'), primary_key=True)
    __medico_id = Column('medico_id', Integer, ForeignKey('medicos.medico_id'))
    __nome = Column('nome', String(100))
    __descricao = Column('descricao', Text)

    __medicos = relationship('models.especialidade.Especialidade', back_populates='medicos')

    def __repr__(self):
        return f'<Especialidade(nome={self.__nome}, descricao={self.__descricao})>'

    def get_especialidade_id(self):
        return self.__especialidade_id

    def set_especialidade_id(self, especialidade_id):
        self.__especialidade_id = especialidade_id

    def get_medico_id(self):
        return self.__medico_id

    def set_medico_id(self, medico_id):
        self.__medico_id = medico_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao
    
    def get_medicos(self):
        return self.__medicos