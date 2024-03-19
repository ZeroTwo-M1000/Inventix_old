POETRY_CMD := $(shell which poetry)
YARN_CMD := $(shell which yarn)
UVICORN_CMD := $(POETRY_CMD) run uvicorn
SRC_DIR := src
CLIENT_DIR := client
PRISMA_CMD := $(POETRY_CMD) run prisma

define set_env_variable
	@echo $(1)="'$(2)'" >> $(SRC_DIR)/.env
endef

.PHONY: api-dev client-dev client-build create-env create-media create-logs setup-prisma setup-backend setup-client setup instructions

api-dev:
	@$(POETRY_CMD) run black $(SRC_DIR)
	@(cd $(SRC_DIR) && $(UVICORN_CMD) --reload --host 0.0.0.0 --port 8000 main:app)

client-dev:
	@(cd $(CLIENT_DIR) && $(YARN_CMD) format && $(YARN_CMD) dev)

client-build:
	@(cd $(CLIENT_DIR) && $(YARN_CMD) format && $(YARN_CMD) build)

create-env:
	@mkdir -p $(SRC_DIR)
	@> $(SRC_DIR)/.env
	$(call set_env_variable,DATABASE_URL,postgresql://user:password@localhost:5432/db_name)
	$(call set_env_variable,SECRET_KEY,secret)
	$(call set_env_variable,ALGORITHM,HS256)
	$(call set_env_variable,ACCESS_TOKEN_EXPIRE_MINUTES,30)

create-media:
	@mkdir -p $(SRC_DIR)/media

create-logs:
	@mkdir -p logs

setup-prisma:
	@(cd $(SRC_DIR) && $(PRISMA_CMD) migrate dev --name init)

setup-backend: create-env create-media create-logs
	@$(POETRY_CMD) install --no-root

setup-client:
	@(cd $(CLIENT_DIR) && $(YARN_CMD) && $(YARN_CMD) format && $(YARN_CMD) build)

setup: setup-backend setup-client instructions

instructions:
	@echo "Setup complete. Please update the .env file with your environment variables."
	@echo "Afterwards, run 'make setup-prisma' to set up the database, followed by 'make api-dev' and 'make client-dev' to start the development servers."
