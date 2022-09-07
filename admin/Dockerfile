# initializing
FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Installing requirements
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

# App runs in docker-compose