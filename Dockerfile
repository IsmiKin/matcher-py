FROM python:3.6

WORKDIR /src

RUN pip install --no-cache --upgrade pip pipenv

COPY ./Pipfile* /src/
RUN pipenv install --system --deploy

RUN mkdir -p tmp_process

COPY /. /src

ENV FIREBASE_CONFIG=creds/.firebase-creds.json

CMD [ "python", "./matcher/main.py" ]
