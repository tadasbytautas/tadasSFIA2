#!/bin/bash

#image update for most up to date version
docker service update --image tbytautas/service_1:latest --force SFIA2_service_1
docker service update --image tbytautas/service_2:latest --force SFIA2_service_2
docker service update --image tbytautas/service_3:latest --force SFIA2_service_3
docker service update --image tbytautas/service_4:latest --force SFIA2_service_4

#Removes local images with note tags/names 
docker system prune -f
# docker rmi $(docker images -f "dangling=true" -q) -f

