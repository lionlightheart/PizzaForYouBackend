FROM python:3.11.9

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --ignore-pipfile

COPY . .

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
