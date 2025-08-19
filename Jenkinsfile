pipeline {
    agent any
    stages {
        // Stage 1: Checkout Code
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/simple-app.git'
            }
        }
        
        // Stage 2: Build (Install Dependencies)
        stage('Build') {
            steps {
                // For Python
                sh 'pip install -r requirements.txt'
                
                // For Node.js
                // sh 'npm install'
            }
        }
        
        // Stage 3: Run Tests (Example)
        stage('Test') {
            steps {
                // For Python (if using pytest)
                sh 'pytest'
                
                // For Node.js (if using Jest/Mocha)
                // sh 'npm test'
            }
        }
        
        // Stage 4: Deploy (Example: Docker or SSH)
        stage('Deploy') {
            steps {
                // Example: Run the app (Python)
                sh 'python app.py &'
                
                // For Docker:
                // sh 'docker build -t myapp .'
                // sh 'docker run -d -p 5000:5000 myapp'
            }
        }
    }
}
