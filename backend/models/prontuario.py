from config.db import Base
from sqlalchemy import Column, Integer, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from medico import Medico
from paciente import Paciente

class Prontuario(Base):
    __tablename__ = 'prontuarios'

    prontuario_id = Column(Integer, Sequence('prontuario_id_seq'), primary_key=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.paciente_id"))
    medico_id = Column(Integer, ForeignKey("medicos.medico_id"))
    data_de_atendimento = Column(Date)

    medicos = relationship("Medico", back_populates="prontuarios")
    pacientes = relationship("Pacientes", back_populates="prontuarios")

    def __repr__(self):
        return f'<Prontuarios(data_de_atendimento={self.data_de_atendimento})>'