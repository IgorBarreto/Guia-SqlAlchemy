from infra.repositories.atores_repository import AtoresRepository
from infra.repositories.filmes_repository import FilmesRepository


def teste_filmes_repository():
    filmes_repository = FilmesRepository()
    f = filmes_repository.insert_one("testando", 2022, "Ação")
    print(f)
    print()
    data = filmes_repository.select_all()
    print(data)
    filmes_repository.delete_one("testando")
    print()
    data = filmes_repository.select_all()
    print(data)


def teste_filmes_repository_relacionamento():
    repo = FilmesRepository()
    response = repo.select_all()
    filme = response[0]
    print(filme)
    print()
    print(filme.titulo)
    print(filme.atores)


def teste_atores_repository():
    atores_repository = AtoresRepository()
    response = atores_repository.select_all()
    print(response[0])


if __name__ == "__main__":
    # teste_filmes_repository()
    # teste_atores_repository()
    teste_filmes_repository_relacionamento()
