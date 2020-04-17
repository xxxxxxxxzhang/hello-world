#!/bin/bash

IF_DELETE_INSTALL_FILE=1
INSTALL_FILE="/usr/share/nginx/html/install.php"

if [ ${IF_DELETE_INSTALL_FILE} == 1 ];
then
    sudo docker exec -it efa3688efdd3 /bin/sh -c 'rm '${INSTALL_FILE}
    echo "Delete finished!"

fi