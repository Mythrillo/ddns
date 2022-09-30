FROM python:3.8-alpine

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app/

RUN crontab /app/crontab

RUN touch /tmp/out.log

CMD crond && tail -f /tmp/out.log
