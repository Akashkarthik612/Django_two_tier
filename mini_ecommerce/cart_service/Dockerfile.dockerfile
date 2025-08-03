#Dockerfile
FROM python:3.11-slim

WORKDIR /app
copy ./app

RUN pip install django

EXPOSE 8002
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
