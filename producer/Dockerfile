# dockerfile for the django-based back-end application

FROM python:3.8.5

# logging setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade python package manager
RUN pip install --upgrade pip

# set pwd
WORKDIR /code

# install required packages for the application
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy core project folder to code dir
COPY . .

# define entrypoint to run after the container deployment
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]