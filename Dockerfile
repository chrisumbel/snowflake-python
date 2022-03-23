FROM python:3.10-bullseye

RUN apt-get update -y
RUN apt-get install -y libssl-dev libopenlibm-dev
RUN pip install --upgrade snowflake-connector-python

RUN mkdir /snowflake
WORKDIR /snowflake

ADD validate.py .

ENTRYPOINT [ "/bin/bash" ]