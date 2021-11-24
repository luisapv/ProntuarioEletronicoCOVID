from config.db import Base
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from prontuario import Prontuario

class Exame(Base):
    __tablename__ = 'exames'

    exame_id = Column(Integer, Sequence('exame_id_seq'), primary_key=True)
    prontuario_id = Column(Integer, ForeignKey("prontuarios.prontuario_id"))
    nome = Column(String(60))
    data_de_realizacao = Column(Date)

    prontuario = relationship("Prontuario", back_populates="exames")
    resultados = relationship("Resultado", back_populates="exames")

    def __repr__(self):
        return f'<Exame(nome={self.nome}, data_de_realizacao={self.data_de_realizacao})>'