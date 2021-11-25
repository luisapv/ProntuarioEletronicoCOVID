from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relation, relationship
from .medico import Medico

class Forum(Base):
    __tablename__ = 'forums'

    def __init__(self, forum_id, medico_id, titulo, descricao, conclusao, data_de_criacao):
        self.__forum_id = forum_id
        self.__medico_id = medico_id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__conclusao = conclusao
        self.__data_de_criacao = data_de_criacao

    __forum_id = Column('forum_id', Integer, Sequence('forum_id_seq'), primary_key=True)
    __medico_id = Column('medico_id', Integer, ForeignKey("models.medicos.medico_id"))
    __titulo = Column('titulo', String(200))
    __descricao = Column('descricao', Text)
    __conclusao = Column('conclusao', Text)
    __data_de_criacao = Column('data_de_criacao', Date)

    __medicos = relationship("models.medico.Medico", back_populates="forums")
    __mensagens = relationship("models.mensagem.Mensagem", back_populates="forums")

    def __repr__(self):
        return f'<Forum(titulo={self.__titulo}, descricao={self.__descricao}, conclusao={self.__conclusao}, data_de_criacao={self.__data_de_criacao})>'

    def get_forum_id(self):
        return self.__forum_id

    def get_medico_id(self):
        return self.__medico_id

    def set_medico_id(self, medico_id):
        self.__medico_id = medico_id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_conclusao(self):
        return self.__conclusao
    
    def set_conclusao(self, conclusao):
        self.__conclusao = conclusao
    
    def get_data_de_criacao(self):
        return self.__data_de_criacao
        
    def set_data_de_criacao(self, data_de_criacao):
        self.__data_de_criacao = data_de_criacao

    def get_medicos(self):
        return self.__medicos

    def get_mensagens(self):
        return self.__mensagens