FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg apt-transport-https && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes main" | \
    tee /etc/apt/sources.list.d/kubernetes.list > /dev/null && \
    apt-get update && \
    apt-get install -y kubectl

USER jenkins
