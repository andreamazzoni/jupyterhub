FROM jupyterhub/jupyterhub:1.0

RUN pip install dockerspawner==0.11.1
RUN pip install jupyterhub-firstuseauthenticator
RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.0.0/examples/cull-idle/cull_idle_servers.py

ENV ADMIN_USERNAME admin
ENV ADMIN_PASSWORD admin

COPY jupyterhub_config.py .
COPY images.json .
COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["jupyterhub"]
