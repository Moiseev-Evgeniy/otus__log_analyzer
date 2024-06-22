run:
	python -m log_analyzer

run_tests:
	pytest .

run_tests_detail:
	pytest tests -s -vvv --setup-show tests

install_deps:
	poetry install

lint:
	ruff check

lint-fix:
	ruff check --fix

lint-format:
	ruff format

lint-isort:
	ruff check --select I

lint-isort-fix:
	ruff check --select I --fix