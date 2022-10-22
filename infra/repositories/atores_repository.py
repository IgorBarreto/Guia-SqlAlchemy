from infra.configs.connection import DBConectionHandler
from infra.entities.Atores import Atores
from infra.entities.Filmes import Filmes


class AtoresRepository:
    def select_all(self):
        with DBConectionHandler() as db:
            atores = (
                db.session.query(Atores, Filmes)
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)
                .with_entities(Atores.nome, Filmes.genero, Filmes.titulo)
                .all()
            )
            return atores

    # def insert_one(self, nome: str, titulo_filme: str) -> None:
    #     with DBConectionHandler() as db:
    #         novo_ator = Atores(nome=nome, titulo_filme=titulo_filme)
    #         db.session.add(novo_ator)
    #         db.session.commit()
    #         db.session.refresh(novo_ator)
    #         return novo_ator

    # def delete_one(self, titulo):
    #     with DBConectionHandler() as db:
    #         db.session.query(Atores).filter(Atores.titulo == titulo).delete()
    #         db.session.commit()

    # def update_one(self, nome: str, titulo_filme: str):
    #     with DBConectionHandler() as db:
    #         ator = db.session.query(Atores).filter(Atores.nome == nome)
    #         ator.update({"titulo_filme": titulo_filme})
    #         db.session.commit()
    #         db.session.refresh(ator)
    #         return ator
