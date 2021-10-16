FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && apt-get -y install software-properties-common 
RUN apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main'
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]
