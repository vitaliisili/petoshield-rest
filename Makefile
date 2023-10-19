runserver:
	python petoshield_api/manage.py runserver

install:
	pip install -r requirements.txt

makemigrations:
	python petoshield_api/manage.py makemigrations

migrate:
	python petoshield_api/manage.py migrate

createsuperuser:
	python petoshield_api/manage.py createsuperuser

startapp:
	cd petoshield_api/apps && django-admin startapp $(app)

flake:
	cd petoshield_api && flake8

test:
	python -m pytest petoshield_api -v

install-web:
	cd petoshield_ui && npm install

start-web:
	cd petoshield_ui && npm start
