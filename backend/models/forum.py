from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relation, relationship
from medico import Medico

class Forum(Base):
    __tablename__ = 'forums'

    forum_id = Column(Integer, Sequence('forum_id_seq'), primary_key=True)
    medico_id = Column(Integer, ForeignKey("medicos.medico_id"))
    titulo = Column(String(200))
    descricao = Column(Text)
    conclusao = Column(Text)
    data_de_criacao = Column(Date)

    medicos = relationship("Medico", back_populates="forums")
    mensagens = relationship("Mensagem", back_populates="forums")

    def __repr__(self):
        return f'<Forum(titulo={self.titulo}, descricao={self.descricao}, conclusao={self.conclusao}, data_de_criacao={self.data_de_criacao})>'