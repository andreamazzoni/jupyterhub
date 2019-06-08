build:
	docker-compose build

run:
	docker-compose up

clean:
	docker-compose down
	docker-compose rm
	docker volume rm jupyterhub-proxy-tmp
