DB_DIR := postgres_service
DB_CONTAINER_NAME := postgres_service

all: clean_db up

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs

clean_db:
	-docker stop $(DB_CONTAINER_NAME)
	-docker rm $(DB_CONTAINER_NAME)

.PHONY: nginx
nginx:
	docker-compose restart nginx

.PHONY: fastapi
fastapi:
	docker-compose restart fastapi_1
	docker-compose restart fastapi_2
	docker-compose restart fastapi_3

# copy_proto:
# 	cp proto/auth.proto auth_service/proto/auth.proto
# 	cp proto/auth.proto gateway_service/proto/auth.proto
# 	cp proto/auth.proto booking_service/proto/auth.proto

test:
	cd auth; make test

key:
	openssl req -x509 -newkey rsa:4096 -keyout backend3.local.key -out backend3.local.crt -days 365 -nodes -subj "/CN=backend3.local"

prune:
	docker system prune -a

install:
	cd auth; make install