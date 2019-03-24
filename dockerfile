FROM python:3.6

ENV PYTHONUNBUFFERED 1

### source
COPY . /root/wxbot

WORKDIR /root/wxbot

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-m", "cron_jobs.cron_job"]