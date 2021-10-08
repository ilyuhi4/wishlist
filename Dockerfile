#syntax=docker/dockerfile:1

#Используем самый последний образ питона
FROM python:3.9.6-alpine

#Устанавливаем перменную "Вывод без буферизации"
ENV PYTHONUNBUFFERED 1

#Обновляем пакеты внутри контейнера
#RUN apt update

#Устанавливаем зависимости из requirements.txt
RUN pip install django gunicorn

#Устанавливаем клиент CURL
RUN apk add curl

#Создаём директорию для проекта
RUN mkdir /wishlist
RUN mkdir /home/app/web/static

#назначем рабочей директорией
WORKDIR /wishlist

#копируем внутрь контейнера наши исходники

#COPY . /wishlist

#что делаем после запуска контейнера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

