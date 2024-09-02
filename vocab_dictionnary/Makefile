up:
	docker compose up -d --build --wait $(service)
start:
	docker compose up --build
down: 
	docker compose down --remove-orphans
build:
	docker compose build $(service)
logs:
	docker compose logs -f $(service)
migrate:
	docker compose run web python3 manage.py migrate
restart:
	docker compose down
	docker compose build
	docker compose up -d