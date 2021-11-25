from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from .forum import Forum

class Mensagem(Base):
    __tablename__ = 'mensagens'

    def __init__(self, mensagem_id, forum_id, data, mensagem):
        self.__mensagem_id = mensagem_id
        self.__forum_id = forum_id
        self.__data = data
        self.__mensagem = mensagem

    __mensagem_id = Column('mensagem_id', Integer, Sequence('mensagem_id_seq'), primary_key=True)
    __forum_id = Column('forum_id', Integer, ForeignKey("models.forums.forum_id"))
    __data = Column('data', Date)
    __mensagem = Column('mensagem', Text)

    def __repr__(self):
        return f'<Mensagem(data={self.__data}, mensagem={self.__mensagem})>'

    def get_mensagem_id(self):
        return self.__mensagem_id
    
    def get_forum_id(self):
        return self.__forum_id

    def set_forum_id(self, forum_id):
        self.__forum_id = forum_id
    
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_mensagem(self):
        return self.__mensagem

    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem