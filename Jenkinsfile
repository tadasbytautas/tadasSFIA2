pipeline {

    agent any

    // stages {

    //     stage('Installing Dependecies') {

    //         steps {

    //             sh 'chmod +x ./scripts/*.sh'
    //             // build images and pushes them to dockerhub
    //             sh './scripts/ansible_execute.sh'

    //         }

    //     }

    stages {

        stage('Builing Images') {

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

            }

        }

        stage('Updating Stack') {

            steps {
                
                sh './scripts/stack_update.sh'

            }

        }

    }

}
