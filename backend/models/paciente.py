from config.db import Base, engine
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship, Session
from .endereco import Endereco
from .prontuario import Prontuario

class Paciente(Base):
    __tablename__ = 'pacientes'

    paciente_id = Column(Integer, Sequence('paciente_id_seq'), primary_key=True)
    nome = Column(String(150))
    cpf = Column(Integer)

    enderecos = relationship("Endereco", back_populates="pacientes")
    prontuarios = relationship("Prontuario", back_populates="pacientes")

    def __repr__(self):
        return f'<Paciente(nome={self.nome}, cpf={self.cpf})>'