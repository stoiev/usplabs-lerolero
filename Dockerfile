FROM python:3.7.4-alpine3.10

WORKDIR /app

RUN pip install pipenv

COPY views lerolero.py web.py Pipfile Pipfile.lock /app/

RUN pipenv install

EXPOSE 8080

CMD ["pipenv", "run", "python", "web.py"]
