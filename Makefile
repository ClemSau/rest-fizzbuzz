PKG ?= $(subst -,_,$(PRJ))
ENV ?= development
BIN ?= venv/Scripts/python3.7.exe

help:			## Print available actions
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

qa:				## Run the QA checks (isort, black, flake8, mypy)
	@isort --profile black .
	@black .
	@flake8
	@mypy -p $(PKG)

test:           ## Run the tests
    @docker-compose exec backend pytest

run:			## Run the api directly
	@python manage.py runserver

run-compose:    ## Run the api and the postgres database with docker-compose
    @docker-compose up

run-compose-build:      ## Run the api and the postgres database with docker-compose and force build
    @@docker-compose up --build