#!/bin/bash

config_result=`sudo docker-compose logs poc`

echo $config_result

[[ $config_result =~ "Poc Success!" ]] || exit -1