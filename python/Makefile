default: test

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: fix
fix:
	isort .
	black .

.PHONY: test
test: fix
	python -m pytest