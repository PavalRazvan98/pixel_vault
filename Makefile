lint:
	poetry run ruff check
	ruff format --check

test:
	poetry run pytest