from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from .prontuario import Prontuario

class Exame(Base):
    __tablename__ = 'exames'

    def __init__(self, exame_id, prontuario_id, nome, data_de_realizacao):
        self.__exame_id = exame_id
        self.__prontuario_id = prontuario_id
        self.__nome = nome
        self.__data_de_realizacao = data_de_realizacao

    __exame_id = Column('exame_id', Integer, Sequence('exame_id_seq'), primary_key=True)
    __prontuario_id = Column('prontuario_id', Integer, ForeignKey("models.prontuarios.prontuario_id"))
    __nome = Column('nome', String(60))
    __data_de_realizacao = Column('data_de_realizacao', Date)

    __prontuarios = relationship("models.prontuario.Prontuario", back_populates="exames")
    __resultados = relationship("models.resultado.Resultado", back_populates="exames")

    def __repr__(self):
        return f'<Exame(nome={self.__nome}, data_de_realizacao={self.__data_de_realizacao})>'

    def get_exame_id(self):
        return self.__exame_id

    def set_exame_id(self, exame_id):
        self.__exame_id = exame_id

    def get_prontuario_id(self):
        return self.__prontuario_id

    def set_prontuario_id(self, prontuario_id):
        self.__prontuario_id = prontuario_id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_data_de_realizacao(self):
        return self.__data_de_realizacao

    def set_data_de_realizacao(self, data_de_realizacao):
        self.__data_de_realizacao = data_de_realizacao
    
    def get_prontuarios(self):
        return self.__prontuarios

    def get_resultados(self):
        return self.__resultados