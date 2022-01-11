# dockerfile for the django-based back-end application

FROM python:3.8.10

# logging setup
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
WORKDIR /code
COPY . /code
RUN pip install -r requirements/prod.txt


# define entrypoint to run after the container deployment
CMD ["python3","main.py"]