import docker
from docker.errors import APIError

client = docker.from_env()

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={'5000/tcp': 5050},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True,
    )
    print(f"Container started WITH profile: {container.short_id}")
except APIError as e:
    print(f"Could not start container with apparmor=my-apparmor-profile: {e.explanation}")
    print("Falling back to unconfined to show the baseline (what the profile WOULD block).")
    container = client.containers.run(
        "flask-apparmor",
        ports={'5000/tcp': 5050},
        security_opt=["apparmor=unconfined"],
        detach=True,
    )
    print(f"Container started UNCONFINED: {container.short_id}")

exit_code, output = container.exec_run("cat /etc/passwd")
first_line = output.decode().splitlines()[0] if output else ""
print(f"Attempt to read /etc/passwd: Exit Code {exit_code}, Output (first line): {first_line}")

exit_code, output = container.exec_run("/bin/bash -c 'echo bash-ran'")
print(f"Attempt to execute /bin/bash: Exit Code {exit_code}, Output: {output.decode().strip()}")

container.stop()
container.remove()
print("Container stopped")
