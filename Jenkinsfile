pipeline {
    agent any

    stages {
        stage('Run Python script') {
            steps {
                sh '''
                    python3 --version
                    python3 testautomation.py
                '''
            }
        }
    }
}
