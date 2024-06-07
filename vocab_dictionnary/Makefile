up:
	docker compose up -d --build --wait $(service)
start:
	docker compose up
down: 
	docker compose down --remove-orphans -v
build:
	docker compose build $(service)
logs:
	docker compose logs -f $(service)
migrate:
	docker compose exec web python3 manage.py makemigrations
	docker compose exec web python3 manage.py migrate