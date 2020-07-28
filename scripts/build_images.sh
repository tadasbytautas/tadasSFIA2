#!/bin/bash

#Build service_1 image if it does not exist localy
if [[ "$(docker images -q tbytautas/service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t tbytautas/service_1 ./Service_1
fi 

#Build service_2 image if it does not exist localy
if [[ "$(docker images -q tbytautas/service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t tbytautas/service_2 ./Service_2
fi 

#Build service_3 image if it does not exist localy
if [[ "$(docker images -q tbytautas/service_3:latest 2> /dev/null)" == "" ]]; then
    docker build -t tbytautas/service_3 ./Service_3
fi 

#Build service_4 image if it does not exist localy
if [[ "$(docker images -q tbytautas/service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t tbytautas/service_4 ./Service_4
fi 