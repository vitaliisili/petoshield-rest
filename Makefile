runserver:
	python petoshield_api/manage.py runserver

install:
	cd petoshield_api && pip install -r requirements.txt

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

install-web:
	cd petoshield_ui && npm install

start-web:
	cd petoshield_ui && npm start

build-web:
	cd petoshield_ui && npm run build

test:
	cd petoshield_api && python -m pytest

test-class:
	cd petoshield_api && python -m pytest -k $(class)

testprint:
	cd petoshield_api && python -m pytest -s

test-cov:
	cd petoshield_api && python -m pytest --cov