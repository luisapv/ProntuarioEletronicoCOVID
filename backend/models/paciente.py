from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

class Paciente(Base):
    __tablename__ = 'pacientes'

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    __paciente_id = Column('paciente_id', Integer, Sequence('paciente_id_seq'), primary_key=True)
    __nome = Column('nome', String(150))
    __cpf = Column('cpf', Integer)

    __enderecos = relationship("models.endereco.Endereco", back_populates="pacientes")
    __prontuarios = relationship("models.prontuario.Prontuario", back_populates="pacientes")

    def __repr__(self):
        return '<Paciente(nome={self.__nome}, cpf={self.__cpf})>'

    def get_paciente_id(self):
        return self.__paciente_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_enderecos(self):
        return self.__enderecos

    def get_prontuarios(self):
        return self.__prontuarios