install:
	@poetry install
	
venv:
	python -m venv .venv
lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
