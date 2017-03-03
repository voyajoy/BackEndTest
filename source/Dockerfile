FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE gitradar.settings
RUN mkdir /django-app
ADD /django-app /django-app
WORKDIR /django-app
RUN pip install -r requirements.txt
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py test
CMD python manage.py runserver 0.0.0.0:8080
