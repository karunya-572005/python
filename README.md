# End-to-End Python CI/CD Pipeline with Jenkins and GitHub Integration

This project implements a Jenkins CI/CD pipeline for a Python application. It includes steps for building, testing, linting, packaging, publishing to GitHub Releases, and deploying with manual approval.

---

## 📁 Project Structure

```bash
   project/
   ├── app/
   │   └── main.py
   ├── tests/
   │   └── test_main.py
   ├── requirements.txt
   ├── Dockerfile
   ├── Jenkinsfile
   └── README.md
  ```
----

## 🔧 Jenkins Pipeline Stages

<img width="838" alt="image" src="https://github.com/user-attachments/assets/296fca8e-9071-4449-8378-d0bcb9d6133d" />

Pipeline URL: [Jenkins](https://mink-welcome-pheasant.ngrok-free.app/job/First_Project/)

### 1. **Checkout**
- Clones the main branch from the GitHub repository.

### 2. **Build**
- Sets up a Python virtual environment.
- Installs dependencies from `requirements.txt`.

### 3. **Test**
- Runs unit tests using `pytest`.
- Generates a code coverage report in HTML format.

### 4. **Scan**
- Performs code linting using `pylint` on the `app` and `tests` directories.

### 5. **Package**
- Packages the app, tests, and required files into a ZIP archive.
- Archives the artifact (`dist/app.zip`) in Jenkins.

### 6. **Publish**
- Creates a new release on GitHub.
- Uploads the ZIP package as a release asset.

### 7. **DEVDeploy**
- Requires manual approval via Jenkins input step.
- Downloads the latest release from GitHub.
- Extracts and runs the application after setting up a new virtual environment.

---

## 🛠️ Prerequisites and Setup

### Required Tools

1. [Git](https://git-scm.com/)
2. [GitHub Account](https://github.com/)
3. [Docker Desktop](https://www.docker.com/products/docker-desktop)
4. [ngrok](https://ngrok.com/)
5. [VsCode](https://code.visualstudio.com/download)

### Setup Instructions

1. **Clone this Repository**
   ```bash
      git clone https://github.com/SugumarSrinivasan/Python.git
      cd Python
   ```

2. **Build the Docker Image**
   ```bash
      docker build -t python-jenkins-app .
   ```
   
3. **Create a Docker Volume**
   ```bash
      docker volume create jenkins_data
   ```
   
4. **Run the Docker Container with Volume Attached**
   ```bash
      docker run -d \
      --name jenkins-python \
      -p 8080:8080 -p 50000:50000 \
      -v jenkins_data:/var/jenkins_home \
      python-jenkins-app
   ```
   
5. **Install and Configure ngrok**
- Download ngrok from [https://ngrok.com/download](https://ngrok.com/download)
- Unzip and move the `ngrok` binary to a folder in your PATH (e.g. `/usr/local/bin`)
- Authenticate with your token:
  ```bash
     ngrok config add-authtoken <your_auth_token>
  ```
  
6. **Start ngrok**
   ```bash
      ngrok http --url=<replace-static-url-here> 8080
   ```

7. **Setup Jenkins**
   - Access Jenkins at http://localhost:8080
   - Install required plugins:
     - Git Plugin
     - Pipeline Plugin
     - HTML Publisher
     - Credentials Binding Plugin
       
8. **Setup a Multibranch Pipeline**
   - Point it to your GitHub repo.
   - Jenkins will auto-discover the Jenkinsfile.

9. **Configure GitHub Webhook**
    - Navigate to your GitHub repository → Settings → Webhooks.
    - Add a new webhook pointing to:
      ```bash
         https://<your-ngrok-url>/github-webhook/
      ```
      
10. **Create and Add GitHub Personal Access Token**
    - Generate a token from GitHub (with repo and workflow scopes).
    - Add it to Jenkins Credentials:

      This project requires two credentials to be configured in Jenkins for seamless GitHub integration and pipeline execution.

      1. github_public
         - Type: `Username with password`
         - Purpose: Used for authenticating Git operations like cloning and fetching the repository.
         - Steps to Create:
           1. Navigate to Jenkins → Manage Jenkins → Credentials.
           2. Choose a domain (or use (global)).
           3. Click Add Credentials.
           4. Choose Kind: Username with password.
           5. Fill in:
              - Username: Your GitHub username
              - Password: A GitHub Personal Access Token (PAT) — not your GitHub password
           6. Set the ID to: github_public
           7. Click OK
      2. GITHUB_TOKEN
         - Type: `Secret text`
         - Purpose:
           - Used in the `Publish` stage to create a GitHub release and upload artifacts.
           - Used in the `DEVDeploy` stage to download artifacts from the GitHub release.
         - Steps to Create:
           1. Navigate to Jenkins → Manage Jenkins → Credentials.
           2. Choose a domain (or use (global)).
           3. Click Add Credentials.
           4. Choose Kind: `Secret text`
           5. Secret: A GitHub Personal Access Token (PAT) with the following scopes:
              - repo
              - workflow
              - write:packages(optional but useful for package upload)
           6. Set the ID to: `GITHUB_TOKEN`
           7. Click OK

| **Credential ID** | **Type**            | **Used In Stage**      | **Purpose**                               |
| ----------------- | ------------------- | ---------------------- | ----------------------------------------- |
| `github_public`   | Username + Password | `Checkout`             | Clone the GitHub repository               |
| `GITHUB_TOKEN`    | Secret Text         | `Publish`, `DEVDeploy` | Upload and download GitHub release assets |


11. **Enable Jenkins Build Trigger**
    - Ensure the webhook is firing correctly.
    - Jenkins will now trigger builds on every push to the main branch.
   
## 🚀 Deployment

Once the build and release are successful:
1. Jenkins will prompt for deployment approval.
2. Upon approval, the latest release artifact will be downloaded and run in the `DEV` environment.

## 📊 Code Coverage

Code coverage reports are generated in the `project/htmlcov` directory and published to Jenkins as an HTML report.

## 🧹 Post Build

Regardless of build result:
- Code coverage reports are archived.
- Workspace is cleaned up.

## Reference
- [Git and GitHub](https://learn.microsoft.com/en-us/training/paths/github-foundations/)
- [Jenkins](https://www.jenkins.io/doc/tutorials/)
- [Docker](https://docs.docker.com/get-started/)
- [Python Tutorial](https://www.w3schools.com/python/)

## YouTube
- [Git and GitHub Tutorial in Tamil](https://www.youtube.com/watch?v=VIBWdLLq9kQ)
- [What is Docker?](https://www.youtube.com/watch?v=jPdIRX6q4jA&list=PLy7NrYWoggjzfAHlUusx2wuDwfCrmJYcs)
- [Python Tutorial for Beginners](https://www.youtube.com/watch?v=t8pPdKYpowI&list=PLy7NrYWoggjxiwNyXNEM8gt1d5Kd2Uh-x)
- [Run Jenkins in Docker Container](https://www.youtube.com/watch?v=pMO26j2OUME)

## ✍️ Author

Sugumar Srinivasan
