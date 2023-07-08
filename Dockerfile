FROM python:3.8-alpine

ARG run_env=dev
ENV env $run_env

LABEL authors="Равиль"

WORKDIR ./docker/user

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip install -r requirements.txt  # RUN Этап сборки.

COPY . .

CMD pytest -s -v tests/*  #RUN Этап запуска.

#Эту команду мы запускаем чтобы собрать наш контейнер
#docker build --build-arg env=development -t automation-tests .

#Эта команда нужна чтобы запустить наш созданый контейнер
#docker run automation-tests

#Эти 2 команды нам нужны чтобы скопировать данные из контейнера и чтобы сгенерировать из результата репорт
#docker cp $(docker ps -a -q | head -1):/usr/lessons/allureResults .
#allure serve allureResults/