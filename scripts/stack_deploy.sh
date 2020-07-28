#!/bin/bash

if [[ "$(docker stack ls 2> /dev/null)" == "" ]]; then
    docker stack deploy --compose-file docker-compose.yml SFIA2
fi 