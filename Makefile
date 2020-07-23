install:
	@poetry install

test:
	poetry run pytest brain_games tests

lint:
	poetry run flake8 brain_games

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install test lint selfcheck check build
		
