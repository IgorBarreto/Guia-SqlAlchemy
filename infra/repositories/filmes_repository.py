from infra.configs.connection import DBConectionHandler
from infra.entities.Filmes import Filmes


class FilmesRepository:
    def select_all(self):
        with DBConectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def insert_one(self, titulo: str, ano: int, genero: str) -> None:
        with DBConectionHandler() as db:
            novo_filme = Filmes(titulo=titulo, ano=ano, genero=genero)
            db.session.add(novo_filme)
            db.session.commit()
            db.session.refresh(novo_filme)
            return novo_filme

    def delete_one(self, titulo):
        with DBConectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update_one(self, titulo: str, ano: str):
        with DBConectionHandler() as db:
            filme = db.session.query(Filmes).filter(Filmes.titulo == titulo)
            filme.update({"ano": ano})
            db.session.commit()
            db.session.refresh(filme)
            return filme
