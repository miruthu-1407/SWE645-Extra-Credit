FROM jenkins/jenkins:lts

USER root

# Install Docker CLI
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    apt-transport-https \
    lsb-release \
    docker.io

# Install kubectl
RUN curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | \
    gpg --dearmor -o /usr/share/keyrings/kubernetes-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /" \
    > /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update && apt-get install -y kubectl

# Do NOT switch back to the Jenkins user
# USER jenkins  <-- comment or remove this
