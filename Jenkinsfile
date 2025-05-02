pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonarqubetoken')
        PATH = "/opt/sonar-scanner/bin:$PATH"
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/superdoo/moto_accident_analysis.git', 
                    credentialsId: 'new_github_creds'
            }
        }

        stage('Set Up Python Environment') {
    steps {
        sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
        '''
            }
        }


        stage('Run Helmet & Speeding Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 analysis.py
                '''
            }
        }

        stage('Run Vehicle Death Analysis') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 death_analysis.py
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('MySonarQube') {
                        sh '''#!/bin/bash
                        export PATH="/opt/sonar-scanner/bin:$PATH"
                        source venv/bin/activate
                        sonar-scanner -Dsonar.login=$SONAR_TOKEN
                        '''
                    }
                }
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/*.csv', onlyIfSuccessful: true
            }
        }
    }
}
