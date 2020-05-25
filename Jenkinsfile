pipeline{
    agent any
    triggers {
        pollSCM '* * * * *'
    }
    stages{
        stage('SCM') {
            steps {
                git 'https://gitlab.com/rkotturu/safeway_poc.git'
            }
        }
        stage('Building Image'){
            steps {
                sh 'docker build -t rohit14/safewayimg:$BUILD_NUMBER /var/jenkins_home/workspace/safeway'
            }
        }
        stage('Push to Docker Hub '){
            steps{
                withCredentials([string(credentialsId: 'Azure2', variable: 'DockerHub')]) {
                    // some block
                    sh "docker login -u rohit14 -p ${DockerHub}"
                }
                sh 'docker push rohit14/safewayimg:$BUILD_NUMBER'
            }
        }
        stage('Remove Images'){
            steps{
                sh 'docker rmi rohit14/safewayimg:$BUILD_NUMBER'
            }
        }
    }   
}
