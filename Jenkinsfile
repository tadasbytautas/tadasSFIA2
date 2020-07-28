pipeline {

    agent any

    stages {

        stage('Build') {

            steps {

                sh 'docker build -t tbytautas/service_1 ./Service_1'
		sh 'docker build -t tbytautas/service_2 ./Service_2'
		sh 'docker build -t tbytautas/service_3 ./Service_3'
		sh 'docker build -t tbytautas/service_4 ./Service_4'

            }

        }

    }

}
