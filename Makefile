install:
	@poetry install
	
venv:
	python3 -m venv .venv
lint:
	poetry run flake8 brain_games

.PHONY: install test lint selfcheck check build
