```
docker run -d \
-e POSTGRES_USER=admin \
-e POSTGRES_PASSWORD=admin \
-e POSTGRES_DB=myproject \
-p 5432:5432 postgres
```