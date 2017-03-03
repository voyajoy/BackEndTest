FROM python:3.5.2
RUN apt-get update && apt-get -y install rsyslog mc
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE gitradar.settings

RUN mkdir /django-app
ADD /django-app /django-app
WORKDIR /django-app

RUN pip install -r requirements.txt
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py test

ADD /django-app/cronjob /etc/cron.d/
RUN chmod +x /django-app/cron.sh
RUN chmod 0644 /etc/cron.d/cronjob
RUN touch /var/log/cron.log
RUN service cron reload

CMD python /django-app/manage.py syncdata
CMD python manage.py runserver 0.0.0.0:8080