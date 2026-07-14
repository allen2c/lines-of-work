# Development
fmt:
	@isort lines_of_work tests
	@black lines_of_work tests
	@ruff check --fix lines_of_work tests

install:
	poetry install --all-extras --all-groups

update:
	poetry update

# Docs
mkdocs:
	mkdocs serve -a 0.0.0.0:8000

# Tests
pytest:
	python -m pytest
