FROM python:latest
LABEL Davi Segundo
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
RUN python src/manage.py makemigrations
RUN python src/manage.py migrate
RUN python src/pop_bank.py
ENTRYPOINT python src/manage.py runserver 0.0.0.0:8000