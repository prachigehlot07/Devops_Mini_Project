import docker

client = docker.from_env()

def deploy_app(image_name, version):
    print(f"Building image {image_name}:{version}...")
    # 1. Build the image 
    image, build_logs = client.images.build(path="./src", tag=f"{image_name}:{version}")
    
    # 2. Run the container 
    print(f"Starting container...")
    container = client.containers.run(
        image.id, 
        detach=True, 
        ports={'8080/tcp': 8080},
        name=f"web_app_{version}"
    )
    print(f"Deployment successful: {container.id}")

deploy_app("my-python-app", "v1")