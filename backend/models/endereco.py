from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from .paciente import Paciente

class Endereco(Base):
    __tablename__ = 'enderecos'

    def __init__(self, paciente_id, nome_local, logradouro, numero, complemento, bairro, cidade, estado, cep):
        self.__paciente_id = paciente_id
        self.__nome_local = nome_local
        self.__logradouro = logradouro
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    __endereco_id = Column('endereco_id', Integer, Sequence('endereco_id_seq'), primary_key=True)
    __paciente_id = Column('paciente_id', Integer, ForeignKey('pacientes.paciente_id'))
    __nome_local = Column('nome_local', String(200))
    __logradouro = Column('logradouro', String(200))
    __numero = Column('numero', Integer)
    __complemento = Column('complemento', String(100))
    __bairro = Column('bairro', String(100))
    __cidade = Column('cidade', String(50))
    __estado = Column('estado', String(30))
    __cep = Column('cep', String(10))

    __pacientes = relationship("models.paciente.Paciente", back_populates="enderecos")

    def __repr__(self):
        return f'<Endereco(nome_local={self.__nome_local}, logradouro={self.__logradouro}, numero={self.__numero}, complemento={self.__complemento}, bairro={self.__bairro}, cidade={self.__cidade}, estado={self.__estado}, cep={self.__cep})>'

    def get_endereco_id(self):
        return self.__endereco_id

    def get_paciente_id(self):
        return self.__paciente_id

    def set_paciente_id(self, paciente_id):
        self.__paciente_id = paciente_id

    def get_nome_local(self):
        return self.__nome_local

    def set_nome_local(self, nome_local):
        self.__nome_local = nome_local

    def get_logradouro(self):
        return self.__logradouro

    def set_logradouro(self, logradouro):
        self.__logradouro = logradouro

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def get_complemento(self):
        return self.__complemento

    def set_complemento(self, complemento):
        self.__complemento = complemento

    def get_bairro(self):
        return self.__bairro

    def set_bairro(self, bairro):
        self.__bairro = bairro

    def get_cidade(self):
        return self.__cidade
    
    def set_cidade(self, cidade):
        self.__cidade = cidade

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, estado):
        self.__estado = estado

    def get_cep(self):
        return self.__cep

    def set_cep(self, cep):
        self.__cep = cep

    def get_pacientes(self):
        return self.__pacientes