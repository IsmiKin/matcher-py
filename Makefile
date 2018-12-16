PYTHONPATH=$(CURDIR)

.PHONY: all

all: test


test:
	@echo "To be defined"


clean-test:
	@echo "To be defined"


linting: flake
	@echo "Running linting"


flake:
	flake8 matcher


setup-dev:
	 pyenv virtualenv 3.6.1 matcher-env


install:
	pipenv install


build:
	docker build -t matcher:staging .


clean-build:
	docker rmi matcher*


up-all-force:
	docker-compose down && docker-compose up --force-recreate


up-dev: build
	docker-compose down && docker-compose up --force-recreate


attach-dev:
	docker exec -it matcherpy_matcher_1 bash


clean:
	@echo "To be defined"
