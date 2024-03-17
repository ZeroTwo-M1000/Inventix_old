POETRY = poetry
UVICORN = $(POETRY) run uvicorn
SRC_DIR = src

.PHONY: api-dev setup

api-dev:
	$(POETRY) run black $(SRC_DIR)
	(cd $(SRC_DIR) && $(UVICORN) --reload --host 0.0.0.0 --port 8000 main:app)

setup:
	$(POETRY) shell
	$(POETRY) install

setup-run-dev: setup api-dev
