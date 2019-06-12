# jupyterhub

This jupyterhub configuration includes:
- Authenticator: FirstUseAuthenticator (https://github.com/jupyterhub/firstuseauthenticator)
- Spawner: DockerSpawner (https://github.com/jupyterhub/dockerspawner)

### FirstUseAuthenticator
This authenticator class allow to create users from the admin console and let them to set their passwords on first login.

If you want user to be able to create themselves on the first login you have to change the flag like this:
```python
c.FirstUseAuthenticator.create_users = True
```
### DockerSpawner
This spawner class allow to create a single-user container for every user. 
The container will be automatically stopped (and removed) after a specified time:
```python
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
```
This spawner also has the possibility to select the image that user want to launch by a selector. You can add (or remove) images simply by edit *jupyterhub/images.json* files. At the moment you can find all the jupyter defaul images describerd here: https://github.com/jupyter/docker-stacks.
### Run
You have to provide:
- Docker
- Docker Compose
- Make

You have to execute:
```bash
$ make create-self-signed-certificate
...
$ docker-compose up
```
