# Guia-SqlAlchemy
## Descrição
### Este projeto foi desenvolvido para aprender como desenvolver um projeto utilizando sqlAlchemy.
Ferramentas utilizadas:
- SqlAlchemy(1.4.42) - Realizar as queries no banco de dados
    https://docs.sqlalchemy.org/en/14/
- Pytest(7.1.3) - Realizar testes unitarios.
    https://docs.pytest.org/en/7.1.x/
- mock-alchemy(0.2.5) - realizar mocks de dados para simular uma busca no banco de dados e testar o repositorio 
    https://mock-alchemy.readthedocs.io/en/latest/user_guide/index.html
- Docker(20.10.20)/Docker-compose(v2.5.0) - Gerar instancias do postgressql e pgAdmin através das images vindas do dockerhub.
    https://docs.docker.com/get-started/overview/
#### Pré-requisitos para a execução do projeto
- docker
- docker-compose
- python 3.10.x

### Execução do projeto
```console
git clone https://github.com/IgorBarreto/Guia-SqlAlchemy.git
```
```console
python -m venv venv && venv\bin\actvate
```
```console
pip install -r requirements.txt
```
```
//cria os containers do postgresql e pgAcimin
docker compose up -d
```

```
alembic upgrade head
```

Para visualizar utilize <http://localhost:5050/> para acessar o pgAdmin

A partir deste momento o projeto está pronto para ser
rodado atavés do comando 
```console
 python3 run.py
```
