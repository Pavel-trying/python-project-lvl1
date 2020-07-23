install:
	@poetry install

lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
