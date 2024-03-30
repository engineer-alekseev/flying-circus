all: install wait_for_it run

wait_for_it: 
	chmod +x ./wait-for-it.sh 
	./wait-for-it.sh -t 120 booking_service:8000
	# ./wait-for-it.sh -t 129 redus_service:6379

install:
	pip install -r requirements.txt

run:
	celery -A celery_app worker --beat --loglevel=info