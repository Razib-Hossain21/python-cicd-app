pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t python-cicd-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop python-app || true'
		sh 'docker rm -f python-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name python-app python-cicd-app'
            }
        }
    }
}
