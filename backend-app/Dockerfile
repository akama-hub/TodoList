# 公式からpython3.10 イメージをpull
FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
RUN mkdir /code/backend-app
WORKDIR /code/backend-app

RUN pip3 install --upgrade pip

ADD requirements.txt /code/backend-app
RUN pip3 install -r requirements.txt
ADD . /code/backend-app/

RUN bash setup.sh