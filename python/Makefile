.PHONY: install test

default: test

install:
	ip install -r requirements.txt

fix:
	isort .
	black .

test:
	python -m pytest