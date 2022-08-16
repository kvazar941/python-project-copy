lint:
	poetry run flake8 page_loader
	poetry run flake8 tests

tests:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader tests/ --cov-report xml

server:
	poetry run python manage.py runserver

locale:
	django-admin makemessages --ignore="static" --ignore="env" -l en

locale-compile:
	django-admin compilemessages --ignore="static" --ignore="env" -l en

migration:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py makemigrations task_manager
	python manage.py migrate task_manager
