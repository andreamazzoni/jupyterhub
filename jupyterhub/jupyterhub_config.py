import os
import json

# User can set their passwords on first login
c.JupyterHub.authenticator_class = 'firstuseauthenticator.FirstUseAuthenticator'

# Users have to exists (created by admin users) before attempt to login
c.FirstUseAuthenticator.create_users = False

## Set of users that will have admin rights on this JupyterHub.
c.Authenticator.admin_users = set([os.environ['ADMIN_USERNAME']])
c.LocalAuthenticator.create_system_users = True
#c.LocalAuthenticator.add_user_cmd = ['adduser', '-q', '–gecos', '""',"&&","echo USERNAME:USERNAME | chpasswd"]

## Docker Spawner
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
#c.JupyterHub.spawner_class = DockerImageChooserSpawner

# The admin must pull these before they can be used.
c.DockerSpawner.image_whitelist = json.load(open("images.json"))

#Envs
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# delete containers when the stop
c.DockerSpawner.remove = True

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '1G'

# Redirect to JupyterLab, instead of the plain Jupyter notebook
c.Spawner.default_url = '/lab'

## Data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
notebook_dir = '/home/jovyan'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.container_name_template = 'jupyterhub-lab-{username}'
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
