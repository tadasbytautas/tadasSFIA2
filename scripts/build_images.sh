#!/bin/bash

#Build clean version of service_1 image
docker build --no-cache -t tbytautas/service_1:latest ./Service_1
#Pushes new built image to docker hub
docker push tbytautas/service_1

#Build clean version of service_2 image
docker build -t tbytautas/service_2:latest ./Service_2
#Pushes new built image to docker hub
docker push tbytautas/service_2

#Build clean version of service_3 image
docker build -t tbytautas/service_3:latest ./Service_3
#Pushes new built image to docker hub
docker push tbytautas/service_3

#Build clean version of service_4 image
docker build -t tbytautas/service_4:latest ./Service_4
#Pushes new built image to docker hub
docker push tbytautas/service_4

#Build clean version of service_4 image
docker build -t tbytautas/nginxsfia2:latest ./NGINX
#Pushes new built image to docker hub
docker push tbytautas/nginxsfia2

 