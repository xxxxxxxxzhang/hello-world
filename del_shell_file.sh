#!/bin/bash

IF_DELETE_INSTALL_FILE=1
WEBSHELL_FILE="/usr/share/nginx/html/bl-content/tmp/shell.php"

if [ ${IF_DELETE_INSTALL_FILE} == 1 ];
then
    sudo docker exec -it efa3688efdd3 /bin/sh -c 'rm '${WEBSHELL_FILE}
    echo "Delete finished!"

fi