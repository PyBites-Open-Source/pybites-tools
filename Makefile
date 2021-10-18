.PHONY: setup
setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements/dev.txt

.PHONY: lint
lint:
	flake8 --exclude venv

.PHONY: typing
typing:
	mypy pybites_tools tests

.PHONY: test
test:
	pytest

.PHONY: coverage
cov:
	pytest --cov=pybites_tools --cov-report term-missing

.PHONY: ci
ci: lint test
