pipeline {
  agent any

  stages {
    stage('Setup & Run Python') {
      steps {
        sh '''
          python3 -m venv venv
          . venv/bin/activate

          python -m pip install --upgrade pip
          pip install requests

          python testautomation.py
        '''
      }
    }
  }
}
