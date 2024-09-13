lint:
	poetry run ruff check
	poetry run ruff format


test:
	poetry run pytest