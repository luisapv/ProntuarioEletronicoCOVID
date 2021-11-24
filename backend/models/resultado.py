from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from exame import Exame

class Resultado(Base):
    __tablename__ = 'resultados'

    resultado_id = Column(Integer, Sequence('resultado_id_seq'), primary_key=True)
    exame_id = Column(Integer, ForeignKey("exames.exame_id"))
    titulo = Column(String(50))
    descricao = Column(Text)
    data_de_publicacao = Column(Date)

    exame = relationship("Exame", back_populates="resultados")

    def __repr__(self):
        return f'<Resultado(titulo={self.titulo}, descricao={self.descricao}, data_de_publicacao={self.data_de_publicacao})>'