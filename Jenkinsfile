pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "student-survey-app:latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using Dockerfile in 'jenkins' folder
                    sh "docker build -t ${DOCKER_IMAGE} -f jenkins/Dockerfile ."
                }
            }
        }
    }
}
