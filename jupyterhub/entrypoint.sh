#!/bin/bash

useradd -m $ADMIN_USERNAME
echo $ADMIN_USERNAME:$ADMIN_PASSWORD | chpasswd
echo User $ADMIN_USERNAME created.

if [ "$1" = 'jupyterhub' ]; then
    exec jupyterhub "$@"
fi

exec "$@"