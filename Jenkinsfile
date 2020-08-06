pipeline {

    agent any

    stages {

        stage('Building Images') {

            steps {
                
                sh 'chmod +x ./scripts/*.sh'
                // build images and pushes them to dockerhub
                sh './scripts/build_images.sh'

            }

        }

        stage('Initialising Docker Swarm') {

            steps {
                
                sh './scripts/docker_swarm_init.sh'

            }

        }

        stage('Deploying Docker Stack') {

            steps {
                
                sh './scripts/stack_deploy.sh'
                sh './scripts/ansible_execute.sh'

            }

        }

        stage('Updating Stack') {

            steps {
                
                sh './scripts/stack_update.sh'

            }

        }

    }

}
