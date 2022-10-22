from infra.repositories import filmes_repository
from infra.repositories.filmes_repository import FilmesRepository


if __name__ == "__main__":
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
