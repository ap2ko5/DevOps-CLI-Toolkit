# DevOps-CLI-Toolkit

**Comprehensive CLI toolkit for DevOps automation including Docker management, Kubernetes deployment, log monitoring, and infrastructure provisioning scripts.**

## Overview

DevOps-CLI-Toolkit is a command-line utility that simplifies DevOps operations with automated deployment, container management, monitoring, and infrastructure provisioning capabilities.

## Features

### 1. Container Management
- Docker image management
- Container lifecycle management
- Docker Compose orchestration
- Registry management
- Container health monitoring

### 2. Kubernetes Operations
- Cluster deployment and management
- Pod and deployment management
- Service management
- Ingress configuration
- Resource scaling and monitoring

### 3. Infrastructure Provisioning
- Infrastructure as Code (IaC)
- Server provisioning
- Network configuration
- Load balancer setup
- Database provisioning

### 4. Log Monitoring
- Centralized log aggregation
- Log analysis and filtering
- Alert system
- Performance metrics
- Error tracking

## Tech Stack

- Python 3.8+
- Docker SDK
- Kubernetes Python Client
- Click for CLI framework
- Terraform for IaC
- ELK Stack for logging

## Installation

```bash
git clone https://github.com/ap2ko5/DevOps-CLI-Toolkit.git
cd DevOps-CLI-Toolkit
pip install -r requirements.txt
python setup.py install
```

## Usage

```bash
# Docker operations
dtk docker build -n myapp .
dtk docker deploy myapp:latest

# Kubernetes operations
dtk k8s create-cluster prod --nodes=3
dtk k8s deploy -f deployment.yaml

# Infrastructure provisioning
dtk provision server --region us-east-1 --type t2.medium

# Monitoring
dtk monitor logs --filter error --tail 100
```

## Commands

### Docker Commands
```
build       Build Docker images
run         Run containers
deploy      Deploy to registry
clean       Remove unused images
ps          List running containers
```

### Kubernetes Commands
```
cluster     Manage clusters
deploy      Deploy applications
scale       Scale deployments
monitor     Monitor cluster health
logs        View pod logs
```

### Provisioning Commands
```
server      Provision servers
network     Configure networks
db          Setup databases
lb          Configure load balancers
firewall    Manage firewall rules
```

## Configuration

Create `~/.devops-toolkit/config.yaml`:

```yaml
docker:
  registry: docker.io
  username: your_username

kubernetes:
  context: production
  namespace: default

cloud:
  provider: aws
  region: us-east-1
```

## Performance

- Deployment time: < 5 minutes
- Provisioning: < 10 minutes
- Scaling: < 30 seconds
- Log query response: < 1 second

## Contributing

Contributions welcome! Fork and submit pull requests.

## License

MIT License

---

**Last Updated**: December 2025
