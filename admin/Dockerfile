# initializing
FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Installing requirements
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

# Running the app
CMD python manage.py runserver 0.0.0.0:8000