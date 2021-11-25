from config.db import Base
from sqlalchemy import Column, Integer, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from medico import Medico
from paciente import Paciente

class Prontuario(Base):
    __tablename__ = 'prontuarios'

    def __init__(self, paciente_id, medico_id, data_de_atendimento):
        self.__paciente_id = paciente_id
        self.__medico_id = medico_id
        self.__data_de_atendimento = data_de_atendimento

    __prontuario_id = Column('prontuario_id', Integer, Sequence('models.prontuario_id_seq'), primary_key=True)
    __paciente_id = Column('paciente_id', Integer, ForeignKey("models.pacientes.paciente_id"))
    __medico_id = Column('medico_id', Integer, ForeignKey("models.medicos.medico_id"))
    __data_de_atendimento = Column('data_de_atendimento', Date)

    __medicos = relationship("models.medico.Medico", back_populates="prontuarios")
    __pacientes = relationship("models.paciente.Pacientes", back_populates="prontuarios")

    def __repr__(self):
        return f'<Prontuarios(data_de_atendimento={self.data_de_atendimento})>'

    def get_prontuario_id(self):
        return self.__prontuario_id

    def get_paciente_id(self):
        return self.__paciente_id

    def set_paciente_id(self, paciente_id):
        self.__paciente_id = paciente_id

    def get_medico_id(self):
        return self.__medico_id

    def set_medico_id(self, medico_id):
        self.__medico_id = medico_id

    def get_data_de_atendimento(self):
        return self.__data_de_atendimento

    def set_data_de_atendimento(self, data_de_atendimento):
        self.data_de_atendimento = data_de_atendimento

    def get_medicos(self):
        return self.__medicos

    def get_pacientes(self):
        return self.__pacientes