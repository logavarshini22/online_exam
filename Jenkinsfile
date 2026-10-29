pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install Python Dependencies') {
            steps { bat 'py -m pip install -r requirements.txt' }
        }

        stage('Syntax Check') {
            steps { bat 'py -m py_compile app_v1.py app_v2.py app_v3.py questions.py' }
        }

        stage('Build and Push Docker Images') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKERHUB_USERNAME',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    bat 'docker build -f Dockerfile.v1 -t %DOCKERHUB_USERNAME%/online-exam:v1 .'
                    bat 'docker build -f Dockerfile.v2 -t %DOCKERHUB_USERNAME%/online-exam:v2 .'
                    bat 'docker build -f Dockerfile.v3 -t %DOCKERHUB_USERNAME%/online-exam:v3 .'
                    bat 'echo %DOCKERHUB_TOKEN% | docker login -u %DOCKERHUB_USERNAME% --password-stdin'
                    bat 'docker push %DOCKERHUB_USERNAME%/online-exam:v1'
                    bat 'docker push %DOCKERHUB_USERNAME%/online-exam:v2'
                    bat 'docker push %DOCKERHUB_USERNAME%/online-exam:v3'
                    bat 'docker logout'
                }
            }
        }
    }
}
