#!/bin/sh

coverage run --source=matcher/,matcher/score,matcher/data -m pytest --strict -rw --ignore=venv/ --cache-clear --junitxml=test-reports/pytest/junit.xml

coverage_success=$?

coverage report -m --skip-covered
coverage html -d test-reports/coverage
coverage xml -o test-reports/coverage.xml

flake8 matcher

flake8_success=$?

exit $coverage_success && $flake8_success
