pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonarqubetoken')  // 'sonar-token' is the ID you gave to your SonarQube token in Jenkins credentials
    }

    stages {
        stage('Clone Repo') {
            steps {
            git branch: 'main', 
                url: 'https://github.com/superdoo/moto_accident_analysis.git', 
                credentialsId: 'new_github_creds'
    }
}

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Analysis') {
            steps {
                sh '''#!/bin/bash
                        python3 -m venv venv
                        . venv/bin/activate
                    pip install -r requirements.txt 
                    '''
                }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('MySonarQube') { // Ensure 'MySonarQube' matches the name in your Jenkins SonarQube configuration
                        sh "sonar-scanner -Dsonar.login=$SONAR_TOKEN"
                    }
                }
            }
        }
    }
}
