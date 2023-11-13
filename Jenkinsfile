pipeline {
    agent any
    tools{
        nodejs 'node'
    }
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Copy Environment For Django API') {
            environment {
                API_ENV = credentials('API_PRODUCTION_ENV')
            }

            steps {
            sh 'cp $API_ENV petoshield_api/.env'
            }
        }

        stage('Deploy Back End Application') {
            steps {
                sh 'sudo docker compose -f docker-compose.yml --env-file=petoshield_api/.env up -d --build'
//                 sh 'sudo docker cp petoshield-api:/api/static /var/www/petoshield-data/static'
            }
        }

        stage('Clear Stopped Containers') {
            steps {
                sh 'sudo docker container prune -f'
            }
        }

        stage('Clear Unused Images') {
            steps {
                sh 'sudo docker rmi $(sudo docker images -f "dangling=true" -q) &>/dev/null'
            }
        }

        // DEPLOY REACT APPLICATION
        stage('Copy Environment For React Application') {
            environment {
                UI_ENV = credentials('UI_PRODUCTION_ENV')
            }

            steps {
                sh 'cp $UI_ENV petoshield_ui/.env'
            }
        }

        stage('Install React Application') {
            steps {
                sh 'cd petoshield_ui && npm install'
            }
        }

        stage('Build React Application') {
            steps {
                sh 'cd petoshield_ui && npm run build'
            }
        }

        stage("Clean Front End Folder") {
            steps {
               sh 'rm -rf /var/www/petoshield.com'
            }
        }

        stage('Deploy Front End Application') {
            steps {
                sh 'mkdir -p /var/www/petoshield.com'
                sh 'cp -r petoshield_ui/build/. /var/www/petoshield.com'
            }
        }
    }
}