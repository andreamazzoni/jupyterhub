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

create-self-signed-certificate:
	mkdir -p reverse-proxy/certs
	chmod 755 reverse-proxy
	chmod 750 reverse-proxy/certs
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
		-keyout reverse-proxy/certs/jupyterhub.key -out reverse-proxy/certs/jupyterhub.crt
	chmod 644 reverse-proxy/certs/jupyterhub.crt
	chmod 600 reverse-proxy/certs/jupyterhub.key
