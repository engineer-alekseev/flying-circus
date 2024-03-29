```
docker run --name booking_db -d \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=the-answer-is-42 \
-e POSTGRES_DB=booking \
-p 5432:5432 postgres
```