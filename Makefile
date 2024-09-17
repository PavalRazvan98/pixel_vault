lint:
	poetry run ruff check
	poetry run ruff format --check


test:
	poetry run pytest