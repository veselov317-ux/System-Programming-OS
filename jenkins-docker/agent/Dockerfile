FROM jenkins/inbound-agent:latest

USER root

RUN apt-get update && apt-get install -y \
    docker.io \
    rpm \
    dpkg \
    apt-transport-https \
    ca-certificates \
    curl \
    bash

RUN usermod -aG docker jenkins

USER jenkins
