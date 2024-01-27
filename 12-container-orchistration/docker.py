import docker

def run_docker_container(image_name, command):
    # Create a Docker client
    client = docker.from_env()

    try:
        # Pull the Docker image (if not already present)
        client.images.pull(image_name)

        # Run the Docker container and capture the container object
        container = client.containers.run(image_name, command, detach=True)

        # Get container details
        container.reload()

        # Print container ID
        print(f"Container ID: {container.id}")

        # Print container logs
        print("\nContainer Logs:")
        print(container.logs().decode("utf-8"))

    except docker.errors.ImageNotFound:
        print(f"Error: Docker image '{image_name}' not found.")
    except docker.errors.APIError as e:
        print(f"Error: {e}")
    finally:
        # Stop and remove the container
        if container:
            container.stop()
            container.remove()

if __name__ == "__main__":
    # Specify the Docker image and command to run
    docker_image = "alpine:latest"
    docker_command = ["echo", "Hello from Docker!"]

    # Run the Docker container and perform actions
    run_docker_container(docker_image, docker_command)
