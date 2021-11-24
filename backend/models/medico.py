from config.db import Base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from .especialidade import Especialidade

class Medico(Base):
    __tablename__ = 'medicos'

    medico_id = Column(Integer, Sequence('medico_id_seq'), primary_key=True)
    especialidade_id = Column(Integer, ForeignKey('especialidades.especialidade_id'))
    nome = Column(String(100))
    crm = Column(Integer)
    senha = Column(String(100))

    especialidade = relationship('Especialidade', back_populates='medicos')
    prontuarios = relationship("Prontuario", back_populates="medicos")

    def __repr__(self):
        return f'<Medico(nome={self.nome}, crm={self.crm})>'