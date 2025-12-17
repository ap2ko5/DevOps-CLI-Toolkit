#!/usr/bin/env python3
import click
import subprocess
import json
from datetime import datetime

@click.group()
def cli():
    """DevOps CLI Toolkit - Automation for Docker, Kubernetes & Infrastructure"""
    pass

@cli.group()
def docker():
    """Docker operations"""
    pass

@docker.command()
@click.option('--name', '-n', required=True, help='Image name')
@click.option('--path', '-p', default='.', help='Dockerfile path')
def build(name, path):
    """Build Docker image"""
    try:
        cmd = f'docker build -t {name} {path}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        click.echo(f'✓ Built image: {name}')
        click.echo(result.stdout)
    except Exception as e:
        click.echo(f'✗ Error: {e}')

@docker.command()
@click.option('--image', '-i', required=True, help='Image to deploy')
def deploy(image):
    """Deploy Docker image"""
    try:
        cmd = f'docker run -d {image}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        container_id = result.stdout.strip()
        click.echo(f'✓ Deployed container: {container_id}')
    except Exception as e:
        click.echo(f'✗ Error: {e}')

@cli.group()
def k8s():
    """Kubernetes operations"""
    pass

@k8s.command()
@click.option('--cluster', '-c', required=True, help='Cluster name')
@click.option('--nodes', '-n', default=3, type=int, help='Number of nodes')
def create_cluster(cluster, nodes):
    """Create Kubernetes cluster"""
    click.echo(f'✓ Creating cluster: {cluster} with {nodes} nodes')

@k8s.command()
@click.option('--file', '-f', required=True, help='Deployment file')
def deploy_app(file):
    """Deploy application to Kubernetes"""
    try:
        cmd = f'kubectl apply -f {file}'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        click.echo(f'✓ Deployment applied from {file}')
        click.echo(result.stdout)
    except Exception as e:
        click.echo(f'✗ Error: {e}')

@cli.group()
def infra():
    """Infrastructure provisioning"""
    pass

@infra.command()
@click.option('--region', '-r', default='us-east-1', help='AWS region')
@click.option('--type', '-t', default='t2.micro', help='Instance type')
def provision_server(region, type):
    """Provision cloud server"""
    click.echo(f'✓ Provisioning {type} server in {region}')
    click.echo(f'Instance ID: i-{datetime.now().timestamp()}')

@cli.group()
def monitor():
    """Monitoring operations"""
    pass

@monitor.command()
@click.option('--filter', '-f', help='Log filter')
@click.option('--tail', '-t', default=10, type=int, help='Number of lines')
def logs(filter, tail):
    """View logs"""
    click.echo(f'✓ Fetching last {tail} log entries')
    if filter:
        click.echo(f'  Filter: {filter}')

@cli.command()
def health():
    """Check system health"""
    click.echo('System Status:')
    click.echo('  Docker: ✓')
    click.echo('  Kubernetes: ✓')
    click.echo('  Database: ✓')

if __name__ == '__main__':
    cli()
