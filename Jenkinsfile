pipeline { 
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/vismayasolanki/jenkin.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 program.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}
