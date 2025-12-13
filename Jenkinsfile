pipeline {
    agent { label 'builder' }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/veselov317-ux/System-Programming-OS.git'
            }
        }

        stage('Install DEB') {
    steps {
        sh 'dpkg -i ./script-1.0-1.el8.noarch.deb || apt-get install -f -y'
    }
}

        stage('Run Script') {
            steps {
                sh '/usr/bin/task1.sh'
            }
        }
    }
}
