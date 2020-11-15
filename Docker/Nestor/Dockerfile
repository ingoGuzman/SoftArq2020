FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27018
ENV SLACK_TOKEN="xoxb-1425337867252-1412495700022-T2yG6Ld4bov575EG98n6ktEQ"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /dc_bot

COPY nestorbot.py nestorbot.py
COPY nestorbot_app.py nestorbot_app.py

CMD ["python","nestorbot_app.py"]