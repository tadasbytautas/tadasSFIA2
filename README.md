## SFIA 2 Project

## docker prune dont not support swarm!
#
extra marks for get ansible to delete unused images and containers from worker node

# Nickname Generator

## Contents

<ul>
  <li>Project Objective</li>
  <li>Application Overview</li>
  <li>Trello Board</li>
  <li>Database Table</li>
  <li>CI Pipeline</li>
  <li>Application Design</li>
  <li>Deployment</li> 
  <li>Risk Assessment</li>
  <li>Current Issues</li>
  <li>Improvements</li>
</ul>

## Project Objective
The requirements of the project are as follows:
<ul>
<li>An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.</li>
<li>An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.</li>
<li>If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application.</li>
<li>The project must follow the Service-oriented architecture that has been asked for.</li>
<li>The project must be deployed using containerisation and an orchestration tool.</li>
<li>As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.</li>
<li>The project must make use of a reverse proxy to make your application accessible to the user.</li>
</ul>
  
## Application Overview
Application designed to create random nickname witch ustualised 4 different microservices.   

Service 1 - is purely designed for user who using application. User has ability to create new nickname by pressing **Generate Nickname** button and see other nickanames that were generetrated previously.

Service 2 - backend service which generates first part of the nickname. Application choses one random string out of 9 which will be used as part of full nickname.

Service 3 - another backend service which does almost same as Service 2, only difference its genererating second part of the nickname.

Service 4 - Combines output of Service 2 and Service 3. Service 1 sends GET request to Service 4 and represens outcome to the user on the main page.

<br>

![](./images/service.png)


## Trello Board
For tracking project progress Trello board was used. Trello is free tool which I utilised on SFIA1 therefor it made sense to use it again. Picture below was taken at the beginning of the project.

![](./images/trello1.png)

Second picture was taken towards end of SFIA2 project which changed quite a bit.

![](./images/trello2.png)

## Database
One of the application requirements was to make sure data is persistent, for this MySQL virtual machine was used. Simple table nickname_gen was created and utilised for this task. 

![](./images/table.png)

## CI Pipeline  

First Diagriam represnts idea of first implementation of CI pipeline prior project development stage. 

![](./images/CI1.png)

Second diagram is focused more on SFIA2 end cicle of finished product. CI pipeline now has Ansible as configaration management tool and docker swarm as orchestrator.

![](./images/CI2.png)

##  Application Design 

Application is quite simple design wise. Title of application is on the top, recentrly generated nickname visable between title and genreate nickname button and previously genererated nicknames populated below in descending order.

![](./images/appscreen.png)

## Deployment

The deployment of the application is fully automated by uttilising tools such as Jenkins, Ansible and Docker. As soon as code being pushed to github repository Jenkins pull the code and starts building docker images. This process is already preconfigured in a way that user should not be required to do any manual work.

Process of Deployment:
- Jenkins builds docker images of each microservice and pushes them to docker hub account.
- 

![Successful Pipeline](https://imgur.com/F0sE4BR.jpg)


A failed Pipeline Job will be displayed as such: 

![Failed Pipeline](https://imgur.com/SdeAent.jpg)

## Risk Assessment
I also carried out a risk assessment identifying the potential risks for this project and any mitigation in place. 

![Risk Assessment](https://imgur.com/6Ge9Dhe.jpg)

## Current Issues
There are currently a few issues with the deployment of the application. These are as follows:  

<ul>
  <li>Nginx isn't configured with Ansible</li>
  <li>Sometimes there can be some downtime when deploying the second implementation as containers are being switched out.</li>
  <li>Machines run out of space</li>
</ul>

## Future Improvements
For potential future improvements, I could:  

<ul>
  <li>Add error handling to prevent downtime</li>
  <li>Store stats in database so a complete character is there</li>
  <li>Add a feature so users can query the database to pull a character at any time</li>
  <li>Improve aesthetic</li>
</ul>