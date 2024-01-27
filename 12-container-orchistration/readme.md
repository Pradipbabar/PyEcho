# Containerization with Docker

Docker is a popular platform for containerization, enabling developers to package applications and their dependencies into a standardized unit known as a container.

## Example: Dockerizing a Python Application

1. **Create a Python Application (`app.py`):**

```python
# app.py
print("Hello, Docker!")
```

2. **Create a `Dockerfile`:**

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run app.py when the container launches
CMD ["python", "app.py"]
```

3. **Build the Docker Image:**

```bash
docker build -t my-python-app .
```

4. **Run the Docker Container:**

```bash
docker run my-python-app
```

# Orchestration with Kubernetes

Kubernetes is a container orchestration platform that automates the deployment, scaling, and management of containerized applications.

## Example: Deploying a Dockerized Python Application on Kubernetes

1. **Create a Kubernetes Deployment (`deployment.yaml`):**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-python-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-python-app
  template:
    metadata:
      labels:
        app: my-python-app
    spec:
      containers:
      - name: my-python-app
        image: my-python-app:latest
        ports:
        - containerPort: 80
```

2. **Create a Kubernetes Service (`service.yaml`):**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-python-app
spec:
  selector:
    app: my-python-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

3. **Apply the Deployment and Service:**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

4. **Access the Application:**

```bash
kubectl get services my-python-app
```

Access the application using the external IP of the service.

# Python Script for Kubernetes Deployment

You can use Python scripts along with the `kubernetes` library to automate Kubernetes deployments. Below is a simple example:

```python
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes deployment
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="my-python-app"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "my-python-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "my-python-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="my-python-app",
                        image="my-python-app:latest",
                        ports=[client.V1ContainerPort(container_port=80)],
                    )
                ]
            ),
        ),
    ),
)

# Create a Kubernetes service
service = client.V1Service(
    api_version="v1",
    kind="Service",
    metadata=client.V1ObjectMeta(name="my-python-app"),
    spec=client.V1ServiceSpec(
        selector={"app": "my-python-app"},
        ports=[client.V1ServicePort(port=80, target_port=80)],
        type="LoadBalancer",
    ),
)

# Create Kubernetes API objects
k8s_apps_v1 = client.AppsV1Api()
k8s_core_v1 = client.CoreV1Api()

# Apply the deployment and service
k8s_apps_v1.create_namespaced_deployment(namespace="default", body=deployment)
k8s_core_v1.create_namespaced_service(namespace="default", body=service)
```

This script demonstrates creating a Kubernetes deployment and service using the `kubernetes` Python library. Ensure that you have the `kubernetes` library installed (`pip install kubernetes`).