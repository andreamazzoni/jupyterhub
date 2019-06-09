build:
	docker-compose build
	docker image prune --force

run:
	docker-compose up

clean:
	docker-compose down
	docker-compose rm
	-docker rm -f $$(docker ps -a --format "{{.Names}}" | grep jupyterhub)
	-docker volume rm $$(docker volume ls --format "{{.Name}}" | grep jupyterhub)
