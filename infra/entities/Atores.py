from infra.configs.base import Base

from sqlalchemy import Column, String, Integer, ForeignKey


class Atores(Base):

    __tablename__ = "atores"
    id = Column(Integer, primary_key=True)
    nome = Column(String, primary_key=True)
    titulo_filme = Column(String, ForeignKey("filmes.fitulo"))

    def __repr__(self) -> str:
        return f"Atores [nome={self.nome}, filme={self.titulo_filme}]"
