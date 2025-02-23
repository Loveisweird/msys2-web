FROM python:3.11.0rc2-bullseye

RUN python -m pip install "poetry==1.1.15"

COPY . /app
WORKDIR /app
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev

ENTRYPOINT ["poetry", "run", "gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--access-logfile", "-", "--bind", "0.0.0.0:80", "--timeout", "60", "app:app"]

EXPOSE 80
