ARG baseImage
FROM ${baseImage}
ENTRYPOINT [ "./run-tests.sh" ]

RUN pipenv install --dev --system --skip-lock
COPY run-tests.sh ./run-tests.sh
COPY tests/. ./tests
