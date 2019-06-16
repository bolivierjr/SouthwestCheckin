all: init test lint

init:
	pip install -r requirements.txt

test:
	pytest -v --cov=api/ --cov=services/ --cov=tasks/

lint:
	pycodestyle */*.py --show-source --ignore=E501

.PHONY: all
