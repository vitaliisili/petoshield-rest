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

test-cov-detail:
	cd petoshield_api && python -m pytest --cov-report term-missing --cov

shell:
	cd petoshield_api && python -m manage shell

create-env:
	cd petoshield_api && \
	echo 'DB_NAME=test_db_name' > .env && \
	echo 'DB_USER=test_db_user' >> .env && \
	echo 'DB_PASSWORD=test_password' >> .env && \
	echo 'DB_HOST=localhost' >> .env && \
	echo 'DB_PORT=5432' >> .env && \
	echo 'DJANGO_SECRET_KEY="super_secret_key_write_here"' >> .env && \
	echo 'DJANGO_DEBUG=1' >> .env && \
	echo 'DATABASE_ENGINE=postgresql' >> .env && \
	echo 'DJANGO_ALLOWED_HOSTS="127.0.0.1,http://localhost:3000/,localhost"' >> .env && \
	echo 'CSRF_TRUSTED_ORIGINS="http://127.0.0.1,http://localhost:3000/"' >> .env && \
	echo 'CORS_ALLOWED_ORIGINS="http://localhost:3000"' >> .env && \
	echo 'TOKEN_EXPIRE=7' >> .env && \
	echo 'REFRESH_TOKEN_EXPIRE=28' >> .env && \
	echo 'EMAIL_HOST_USER="your_smtp_email@mail.com"' >> .env && \
	echo 'EMAIL_HOST_PASSWORD="password_here"' >> .env && \
	echo 'POLICY_BASE_PRICE=10' >> .env && \
	echo 'STRIPE_SECRET_KEY="Stripe_Secret_key_from_stripe.com"' >> .env && \
	echo 'STRIPE_PUBLIC_KEY="Stripe_public_key_from_stripe.com"' >> .env && \
	echo 'STRIPE_WEBHOOK_SECRET="Stripe_webhook_key_from_stripe.com"' >> .env

create-env-ui:
	cd petoshield_ui && echo 'REACT_APP_BACKEND_URL=http://localhost:8000' > .env

spectacular:
	cd petoshield_api && python -m manage spectacular --file schema.yml
