import docker
from docker.errors import APIError

client = docker.from_env()

print("Building image from Dockerfile...")
client.images.build(path=".", tag="flask-apparmor")

print("Running container with AppArmor profile...")
try:
    container = client.containers.run(
        "flask-apparmor",
        ports={'5000/tcp': 5050},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )
except APIError as e:
    print(f"Container failed to start with AppArmor profile: {e.explanation}")
    raise SystemExit(1)

print(f"Container started: {container.short_id}")

print("Inspecting container to verify AppArmor profile...")
container_info = client.api.inspect_container(container.id)
apparmor_profile = container_info['HostConfig']['SecurityOpt']

print(f"AppArmor profile applied: {apparmor_profile}")

print("Stopping the container...")
container.stop()
container.remove()
