DOCKER_COMPOSE_PROJECT=olive
DOCKER_COMPOSE_FILE_DEV="`pwd`/dev/docker-compose.dev.yml"
DOCKER_COMPOSE_FILE_PROD="`pwd`/dev/docker-compose.prod.yml"
DOCKER_COMPOSE_CMD_DEV=docker compose -p $(DOCKER_COMPOSE_PROJECT) -f $(DOCKER_COMPOSE_FILE_DEV)
DOCKER_COMPOSE_CMD_PROD=docker compose -p $(DOCKER_COMPOSE_PROJECT) -f $(DOCKER_COMPOSE_FILE_PROD)

PYTHON_EXEC=/usr/local/bin/python


run:
	$(DOCKER_COMPOSE_CMD_DEV) up --force-recreate --build -d

api:
	$(DOCKER_COMPOSE_CMD_DEV) up --force-recreate olive-api --build -d

db:
	$(DOCKER_COMPOSE_CMD_DEV) up --force-recreate olive-db --build -d

prod:
	$(DOCKER_COMPOSE_CMD_PROD) up --force-recreate --build -d

makemigrations:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic revision --autogenerate

alembic_init:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic init migrations

migrate:
	$(DOCKER_COMPOSE_CMD_DEV) exec wordle_bot alembic upgrade head

check:
	@pre-commit run --all-files
