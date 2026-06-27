pipeline {
    agent any

    environment {
          CONTAINER_NAME= "my_django_cont"
          IMAGE_NAME=  "django_image"
          PORT= 8000
          EMAIL="mdshaisakhter840@gmail.com"
    }

    stages{
        stage('Clone repo'){
            steps{
                git branch: 'main',
                 url: 'https://github.com/Eagle766/Django_CI_CD.git'
            }
        }

        stage('Build Image'){
            steps{
                sh 'docker build -t $IMAGE_NAME . '
            }
        }

        stage('stop & remove previous container'){
            steps{
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                
                '''
            }
        }

         stage('deployed container or container run'){
            steps{
                sh '''
                docker run -d -p ${PORT}:${PORT} --name $CONTAINER_NAME $IMAGE_NAME
                
                '''
            }
        }

         stage('SEND EMAIL'){
            steps{
                emailext(
                    subject: "Your django app deployed is successfully",
                    body: "Your app is deployed!  http://34.248.132.135:${PORT}/",
                    to: '${EMAIL}'
                    
                )
            }
        }
    }
}