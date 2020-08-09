#!/bin/bash

#Build service_1 image if it does not exist localy
if [[ "$(docker node ls 2> /dev/null)" == "" ]]; then
    docker swarm init    
else
    docker node ls
fi 