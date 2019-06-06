#!/bin/sh

useradd -m $ADMIN_USERNAME
echo $ADMIN_USERNAME:$ADMIN_PASSWORD | chpasswd

if [ "$1" = 'jupyterhub' ]; then
    exec jupyterhub "$@"
fi

exec "$@"