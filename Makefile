build:
	docker compose build

up:
	docker compose up front back

down:
	docker compose down

vite_scaffolder:
	docker compose run --rm vite_scaffolder npm create vite@latest ${i}  

django_scaffolder:
	docker compose run --rm django_scaffolder django-admin startproject core ./back

create_app:
	docker compose run --rm back ./manage.py startapp ${i}