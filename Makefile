install:
	poetry install
	
lint:
	poetry run flake8 task_manager

test:
	./manage.py test

test-coverage:
	poetry run coverage run --omit '.venv/*' --source '.' manage.py test

test-report: test-coverage
	poetry run coverage report

test-report-xml:
	poetry run coverage xml

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
