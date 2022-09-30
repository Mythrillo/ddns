FROM python:3.8.14-apline3.16

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN crontab crontab

CMD ["crond", "-f"]
