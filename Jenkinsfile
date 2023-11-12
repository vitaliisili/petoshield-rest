pipeline {
    agent any
    tools{
        nodejs '20.9.0'
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

//         stage('Checks before env') {
//             steps {
//                 sh 'ls -a'
//             }
//         }

        stage('Create environment') {
            environment {
                DB_NAME=credentials('PET_DB_NAME')
                DB_USER=credentials('PET_DB_USER')
                DB_PASSWORD=credentials('PET_DB_PASSWORD')
                DB_HOST=credentials('PET_DB_HOST')
                DB_PORT=credentials('PET_DB_PORT')
                DJANGO_SECRET_KEY=credentials('PET_DJANGO_SECRET_KEY')
                DJANGO_DEBUG=credentials('PET_DJANGO_DEBUG')
                DATABASE_ENGINE=credentials('PET_DATABASE_ENGINE')
                DJANGO_ALLOWED_HOSTS=credentials('PET_DJANGO_ALLOWED_HOSTS')
                CSRF_TRUSTED_ORIGINS=credentials('PET_CSRF_TRUSTED_ORIGINS')
                TOKEN_EXPIRE=credentials('PET_TOKEN_EXPIRE')
                REFRESH_TOKEN_EXPIRE=credentials('PET_REFRESH_TOKEN_EXPIRE')
                CORS_ALLOWED_ORIGINS=credentials('PET_CORS_ALLOWED_ORIGINS')
                EMAIL_HOST_USER=credentials('PET_EMAIL_HOST_USER')
                EMAIL_HOST_PASSWORD=credentials('PET_EMAIL_HOST_PASSWORD')
                POLICY_BASE_PRICE=credentials('PET_POLICY_BASE_PRICE')
//                 REACT_APP_BACKEND_URL=credentials('PET_REACT_APP_BACKEND_URL')
                REACT_APP_BACKEND_URL="https://api.petoshield.com"
            }
            steps {
                sh 'echo DB_NAME=$DB_NAME > .env'
                sh 'echo DB_USER=$DB_USER >> .env'
                sh 'echo DB_PASSWORD=$DB_PASSWORD >> .env'
                sh 'echo DB_HOST=$DB_HOST >> .env'
                sh 'echo DB_PORT=$DB_PORT >> .env'
                sh 'echo DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY >> .env'
                sh 'echo DJANGO_DEBUG=$DJANGO_DEBUG >> .env'
                sh 'echo DATABASE_ENGINE=$DATABASE_ENGINE >> .env'
                sh 'echo DJANGO_ALLOWED_HOSTS=$DJANGO_ALLOWED_HOSTS >> .env'
                sh 'echo CSRF_TRUSTED_ORIGINS=$CSRF_TRUSTED_ORIGINS >> .env'
                sh 'echo TOKEN_EXPIRE=$TOKEN_EXPIRE >> .env'
                sh 'echo REFRESH_TOKEN_EXPIRE=$REFRESH_TOKEN_EXPIRE >> .env'
                sh 'echo CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS >> .env'
                sh 'echo EMAIL_HOST_USER=$EMAIL_HOST_USER >> .env'
                sh 'echo EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD >> .env'
                sh 'echo POLICY_BASE_PRICE=$POLICY_BASE_PRICE >> .env'
                sh 'echo REACT_APP_BACKEND_URL=$REACT_APP_BACKEND_URL > petoshield_ui/.env'
            }
        }

        stage('Checks after env') {
            steps {
                sh 'ls -a'
                sh 'cat .env'
                sh 'ls -a petoshield_api'
                sh 'ls -a petoshield_ui'
            }
        }
//         stage('Build FrontEnd') {
//             steps {
//                 sh 'cd petoshield_ui && npm install'
//                 sh 'cd petoshield_ui && npm run build'
//             }
//         }

        stage("Clear Front End Folder") {
            steps {
                sh 'rm -R /var/www/petoshield.com'
            }
        }

        stage('Deploy Front End Application') {
            steps {
                sh 'mkdir /var/www/petoshield.com'
                sh 'cp -r petoshield_ui/build/. /var/www/petoshield.com'
            }
        }

        stage('Deploy Back End Application') {
            steps {
                sh 'sudo docker compose -f docker-compose.yml up -d --build'
                sh 'sudo docker cp petoshield-api:/static /var/www/petoshield-data/static'
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
    }
}