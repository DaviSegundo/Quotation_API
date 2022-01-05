FROM python:latest
LABEL Davi Segundo
EXPOSE 8000
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
ENTRYPOINT python src/manage.py runserver 0.0.0.0:8000