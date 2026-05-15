pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Razib-Hossain21/python-cicd-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-cicd-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop 7cbac930d0c1 || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name python-app python-cicd-app'
            }
        }
    }
}
