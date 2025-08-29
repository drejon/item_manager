build:
	docker compose build

up:
	docker compose up --no-attach postgres

down:
	docker compose down

init: build
	rm -rf back/node_modules
	rm -rf front/node_modules
	mkdir back/node_modules
	mkdir front/node_modules
	docker compose run --rm back npm install
	docker compose run --rm front npm install

test_back:
	docker compose run --rm back npm test

vite_scaffolder:
	docker compose run --rm vite_scaffolder npm create vite@latest ${i}