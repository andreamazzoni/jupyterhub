FROM jupyterhub/jupyterhub:latest

RUN pip install dockerspawner
RUN pip install jupyterhub-firstuseauthenticator
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.0.0/examples/cull-idle/cull_idle_servers.py

COPY jupyterhub_config.py .
COPY images.json .
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["jupyterhub"]
