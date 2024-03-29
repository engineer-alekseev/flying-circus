sudo docker run --rm --name my_postgres -p 5431:5432 \
--mount type=bind,source=/home/prod/cursebow,\
target=/docker-entrypoint-initdb.d -e POSTGRES_PASSWORD=postgres postgres



scp -r -p 2022 ./ prod@bytecode.su:
# test