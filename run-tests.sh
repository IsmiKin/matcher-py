#!/bin/sh

coverage run --source=matcher/,matcher/score,matcher/data -m pytest --strict -rw --ignore=venv/ --junitxml=test-reports/pytest/junit.xml

coverage_success=$?

coverage report -m --skip-covered
coverage html -d test-reports/coverage

flake8 matcher tests

flake8_success=$?

exit $coverage_success && $flake8_success
