all: install wait_for_it run

loop:
	while true; do \
	  echo		;\
	  sleep 1 ;\
	done

wait_for_it: 
	chmod +x ./wait-for-it.sh 
	./wait-for-it.sh -t 120 postgres_service:5432

init_migration:
	-alembic init -t async migrations

migrate:
	alembic revision --autogenerate -m "init"

grpc:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/auth.proto

install:
	pip install -r requirements.txt

run:
	python3 main.py