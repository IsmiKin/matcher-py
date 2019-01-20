#!/bin/sh

pytest --cov=matcher --cov-report=xml --cache-clear src/matcher/tests

coverage_success=$?

flake8 matcher

flake8_success=$?

exit $coverage_success && $flake8_success
