FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

ENV PYTHONUNBUFFERED=1

WORKDIR /app/greeting/

COPY requirements.txt /app/greeting/

RUN pip install -r requirements.txt

COPY . /app/greeting/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]