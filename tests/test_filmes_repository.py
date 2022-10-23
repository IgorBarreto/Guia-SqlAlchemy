from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.repositories.filmes_repository import FilmesRepository
from infra.entities.Filmes import Filmes
from unittest import mock


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Filmes),
                        # mock.call.filter(Filmes.genero == "Acao"),
                    ],
                    [Filmes(titulo="meu_titulo", genero="Acao", ano=2000)],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_select():
    repo = FilmesRepository(ConnectionHandlerMock)
    response = repo.select_all()
    print(response)
