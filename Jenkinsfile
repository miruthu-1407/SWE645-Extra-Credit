pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ruchitadarur/python-survey-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/miruthu-1407/SWE645-Extra-Credit.git', branch: 'main'
            }
        }

        stage('Install & Test') {
            steps {
                script {
                    docker.image('python:3.11').inside {
                        dir('student-survey-flask-app') {
                            sh 'pip install -r requirements.txt'
                            sh 'pytest'
                        }
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('student-survey-flask-app') {
                    sh "docker build -t $DOCKER_IMAGE ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploy stage (to be implemented or uncommented as needed)'
                // Add deployment logic here if needed
            }
        }
    }
}
