FROM python:3.6

WORKDIR /

RUN pip install --no-cache --upgrade pip pipenv

COPY ./Pipfile* /
RUN pipenv install --system --deploy

COPY /. /

CMD [ "python", "./matcher/main.py" ]
