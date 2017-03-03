migrate:
	python manage.py migrate

run: migrate
	python manage.py runserver 0.0.0.0:8000

worker:
	celery -A backend worker -l info

beat:
	celery -A backend beat -l info

test:
	python manage.py test
