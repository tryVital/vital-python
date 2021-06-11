NAME=vital-python
VERSION=$(shell git rev-parse HEAD)

install:
	pip install -r requirements.txt
	pip install -r requirements-test.txt

install-requirements:
	pip install -r requirements.txt

install-test-requirements:
	pip install -r requirements-test.txt

lint:
	flake8 --exclude=.venv,./scripts/*

check-format:
	black --check --diff vital/*
	isort --check-only --diff .

format:
	black .
	isort .

mypy:
	mypy --disallow-incomplete-defs --check-untyped-defs vital

test:
	pytest -vv -c pytest.ini .

run:
	. ./scripts/run.sh

create_test_data:
	PYTHONPATH=. python scripts/test_user.py $(AUTH0_ID)


.PHONY: lint run test install install-requirements install-test-requirements
