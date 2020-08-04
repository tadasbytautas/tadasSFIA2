#!/bin/bash

source /var/lib/jenkins/.env

if [[ "$(docker stack services SFIA2 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml SFIA2
else
    docker stack ls
fi 

