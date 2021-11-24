from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Text
from sqlalchemy.orm import relationship
from .medico import Medico

class Especialidade(Base):
    __tablename__ = 'especialidades'

    especialidade_id = Column(Integer, Sequence('especialidade_id_seq'), primary_key=True)
    medico_id = Column(Integer, ForeignKey('medicos.medico_id'))
    nome = Column(String(100))
    descricao = Column(Text)

    medico = relationship('Especialidade', back_populates='medicos')

    def __repr__(self):
        return f'<Especialidade(nome={self.nome}, descricao={self.descricao})>'