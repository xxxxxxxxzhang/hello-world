#!/bin/bash
sleep 50
config_result=`sudo docker-compose logs poc`

echo "$config_result"

[[ $config_result =~ "Success Poc!" ]] || exit -1