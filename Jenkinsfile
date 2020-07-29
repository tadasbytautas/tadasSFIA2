pipeline {

    agent any

    stages {

        stage('Build Images') {

            steps {

                sh 'chmod +x ./scripts/*.sh'
                // build images and pushes them to dockerhub
                sh './scripts/build_images.sh'

            }

        }

        stage('Docker Swarm Init') {

            steps {
                
                sh './scripts/docker_swarm_init.sh'

            }

        }

        stage('Deploy Stack') {

            steps {
                
                sh './scripts/stack_deploy.sh'

            }

        }

        stage('Update Stack') {

            steps {
                
                sh './scripts/stack_update.sh'

            }

        }

    }

}
