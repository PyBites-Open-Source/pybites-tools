.PHONY: setup
setup:
	python3 -m venv venv && source venv/bin/activate && pip install -r requirements/dev.txt

.PHONY: lint
lint:
	flake8 --exclude venv

.PHONY: typing
typing:
	mypy tools tests

.PHONY: test
test:
	pytest

.PHONY: ci
ci: lint test
