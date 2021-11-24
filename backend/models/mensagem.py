from config.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from forum import Forum

class Mensagem(Base):
    __tablename__ = 'mensagens'

    mensagem_id = Column(Integer, Sequence('mensagem_id_seq'), primary_key=True)
    forum_id = Column(Integer, ForeignKey("forums.forum_id"))
    data = Column(Date)
    mensagem = Column(Text)

    def __repr__(self):
        return f'<Mensagem(data={self.data}, mensagem={self.mensagem})>'