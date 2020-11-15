FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_T1 xoxb-1425337867252-141249
ENV SLACK_T2 5700022-jVHglEbfTtfhfPVcSQpOsPS9

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /dc_bot

COPY nestorbot.py nestorbot.py
COPY nestorbot_app.py nestorbot_app.py
COPY populate.py populate.py

CMD ["python","nestorbot_app.py"]