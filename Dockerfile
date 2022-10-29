FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN pip install --upgrade pip

WORKDIR /app

RUN adduser --disabled-password --gecos "" supply_tracker_usr
RUN mkdir /app/logs

COPY ./requirements.txt .
RUN pip install -r requirements.txt && pip install uwsgi

COPY . .

COPY infra/uwsgi.ini .
COPY infra/entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["uwsgi", "--ini", "uwsgi.ini"]
