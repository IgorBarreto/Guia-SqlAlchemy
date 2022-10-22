from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# configurando a engine com sting de conexão
engine = create_engine("postgresql://postgres:postgres@localhost:5432/cinema")

# criando a base declarativa e a sessão
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = "filmes"
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Filem(titulo:{self.titulo}, ano:{self.ano})"


## SQL

# delete
session.query(Filmes).filter(Filmes.titulo == "Teste1").delete()
session.commit()
# insert
novo_filme = Filmes(titulo="Teste1", ano=1950, genero="Animação")
session.add(novo_filme)
session.commit()

# Update
session.query(Filmes).filter(Filmes.titulo == "teste").update({"titulo": "Meu teste"})
# Select
data = session.query(Filmes).all()

print(data)


session.close()
