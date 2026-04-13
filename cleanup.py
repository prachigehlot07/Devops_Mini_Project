import docker

client = docker.from_env()

def cleanup_old_containers(prefix="web_app_"):
    containers = client.containers.list(all=True)
    for c in containers:
        if c.name.startswith(prefix) and c.status != "running":
            print(f"Removing old container: {c.name}")
            c.remove()

def prune_images():
    print("Cleaning up dangling images...")
    client.images.prune()

cleanup_old_containers()
prune_images()