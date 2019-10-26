all: init test lint

init:
	pip install -r requirements.txt

lint:
	pycodestyle */*.py --show-source --ignore=E501

.PHONY: all
