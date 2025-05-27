# Base Jenkins image
FROM jenkins/jenkins:lts

USER root

# Install system packages including zip and unzip
RUN apt-get update \
 && apt-get install -y python3 python3-pip python3-venv git curl gnupg zip unzip \
 && python3 -m venv /opt/venv \
 && /opt/venv/bin/pip install --upgrade pip \
 && /opt/venv/bin/pip install pytest \
 && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg \
 && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" > /etc/apt/sources.list.d/github-cli.list \
 && apt-get update \
 && apt-get install -y gh \
 && apt-get clean

# Add Python virtual environment to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Switch back to Jenkins user
USER jenkins
