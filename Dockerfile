FROM python:3.6

ENV PYTHONPATH=$PYTHONPATH:.

WORKDIR /src

RUN pip install --no-cache --upgrade pip pipenv

COPY ./Pipfile* /src/
RUN pipenv install --system --deploy

COPY /. /src

CMD [ "python", "./matcher/main.py" ]
