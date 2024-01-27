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
