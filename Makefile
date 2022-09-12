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
	django-admin makemessages --ignore="static" --ignore="env" -l ru

locale-compile:
	django-admin compilemessages --ignore="static" --ignore="env" -l ru

migration:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

push:
	poetry export -f requirements.txt --output requirements.txt
	poetry run python manage.py collectstatic
	heroku run python manage.py makemigrations -a task-manager-5289
	heroku run python manage.py migrate -a task-manager-5289
	git push heroku main
	git push
