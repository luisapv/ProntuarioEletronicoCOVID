from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from paciente import Paciente

class Endereco(Base):
    __tablename__ = 'enderecos'

    endereco_id = Column(Integer, Sequence('endereco_id_seq'), primary_key=True)
    paciente_id = Column(Integer, ForeignKey('pacientes.paciente_id'))
    nome_local = Column(String(200))
    logradouro = Column(String(200))
    numero = Column(Integer)
    complemento = Column(String(100))
    bairro = Column(String(100))
    cidade = Column(String(50))
    estado = Column(String(30))
    cep = Column(String(10))

    paciente = relationship("Paciente", back_populates="enderecos")

    def __repr__(self):
        return f'<Endereco(nome_local={self.nome_local}, logradouro={self.logradouro}, numero={self.numero}, complemento={self.complemento}, bairro={self.bairro}, cidade={self.cidade}, estado={self.estado}, cep={self.cep})>'