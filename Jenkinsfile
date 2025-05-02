pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonarqubetoken')
        PATH = "/opt/sonar-scanner/bin:$PATH"
    }

    stages {


        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Clone Repo') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/superdoo/moto_accident_analysis.git', 
                    credentialsId: 'new_github_creds'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Analysis') {
            steps {
                sh '''#!/bin/bash
                source venv/bin/activate
                python3 analysis.py
                '''
            }
        }

        stage('Death Analysis') {
            steps {
                sh '''#!/bin/bash
                source venv/bin/activate
                python3 death_analysis.py
                '''
            }
        }


        // stage('SonarQube Analysis') {
        //     steps {
        //         script {
        //             withSonarQubeEnv('MySonarQube') {
        //                 sh '''#!/bin/bash
        //                 export PATH="/opt/sonar-scanner/bin:$PATH"
        //                 source venv/bin/activate
        //                 sonar-scanner -Dsonar.login=$SONAR_TOKEN
        //                 '''
        //             }
        //         }
        //     }
        // }
    }
}
