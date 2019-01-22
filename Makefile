PYTHONPATH=$(CURDIR)

.PHONY: all

all: test


test:
	coverage run --source=matcher/,matcher/score,matcher/data --omit=*/test* -m pytest --strict
	coverage report -m


test-simple:
	pytest matcher


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
	docker-compose build


clean-build:
	docker rm $(docker ps -aq -f status=exited)
	docker rmi matcher*


up-all-force: build
	docker-compose down
	docker-compose up --force-recreate


up-dev: build
	docker-compose down
	docker-compose up --force-recreate


attach-dev:
	docker exec -it matcherpy_matcher_1 bash


clean:
	@echo "To be defined"
