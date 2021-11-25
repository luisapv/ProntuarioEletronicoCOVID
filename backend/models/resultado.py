from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from exame import Exame

class Resultado(Base):
    __tablename__ = 'resultados'

    def __init__(self, exame_id, titulo, descricao, data_de_publicacao):
        self.__exame_id = exame_id
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_de_publicacao = data_de_publicacao

    __resultado_id = Column('resultado_id', Integer, Sequence('resultado_id_seq'), primary_key=True)
    __exame_id = Column('exame_id', Integer, ForeignKey("models.exames.exame_id"))
    __titulo = Column('titulo', String(50))
    __descricao = Column('descricao', Text)
    __data_de_publicacao = Column('data_de_publicacao', Date)

    __exames = relationship("models.exame.Exame", back_populates="resultados")

    def __repr__(self):
        return '<Resultado(titulo={self.__titulo}, descricao={self.__descricao}, data_de_publicacao={self.__data_de_publicacao})>'

    def get_resultado_id(self):
        return self.__resultado_id

    def get_exame_id(self):
        return self.__exame_id

    def set_exame_id(self, exame_id):
        self.__exame_id = exame_id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_descricao(self):
        return self.__descricao

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_data_de_publicacao(self):
        return self.__data_de_publicacao

    def set_data_de_publicacao(self, data_de_publicacao):
        self.__data_de_publicacao = data_de_publicacao

    def get_exames(self):
        return self.__exames