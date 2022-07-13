install:
	@poetry install
 
lint:
	@poetry run flake8 gendiff
 
selfcheck:
	poetry check
 
check: selfcheck lint
 
build: check
	@poetry build
 
run_test:
	poetry run pytest --cov=gendiff --cov-report xml tests/
 
 
.PHONY: install test lint selfcheck check build