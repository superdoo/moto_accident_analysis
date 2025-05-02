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
                    pip install --upgrade pip
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
                withSonarQubeEnv('MySonarQube') {
                    sh '''
                        . venv/bin/activate
                        sonar-scanner -Dsonar.projectKey=moto_accident_analysis \
                                      -Dsonar.sources=. \
                                      -Dsonar.host.url=http://localhost:8080 \
                                      -Dsonar.login=$SONAR_TOKEN
                    '''
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
