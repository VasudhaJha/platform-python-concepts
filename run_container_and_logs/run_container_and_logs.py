import argparse
import subprocess

def run_container(image: str, name:str=None, debug: bool = False) -> str:
    command = ["docker", "run", "-d", "--rm"]

    if name:
        command.extend(["--name", name])
        
    command.append(image)
    print(f"Starting container from image: {image}")

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        container_id = result.stdout.strip()
        print(f"Container '{name}' started with ID: {container_id}")
        return container_id
    except subprocess.CalledProcessError as e:
        print("Failed to start container.")
        if debug:
            print("Docker error:", e.stderr.strip())
        raise RuntimeError(f"Container startup failed for image '{image}'")
    
def get_container_logs(container_id: str, debug: bool = False):
    command = ["docker", "logs", container_id]
    print(f"Fetching logs for container: {container_id}")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("--- container logs ---")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to retrieve logs.")
        if debug:
            print("Docker error:", e.stderr.strip())
        raise RuntimeError("Error getting logs for container with id {container_id}")

def main():
    parser = argparse.ArgumentParser(description="Run a container and prints its logs")
    parser.add_argument("--debug", action="store_true", help="Enable debug output")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # run subcommand
    run_parser = subparsers.add_parser("run", help="Run a Docker container")
    run_parser.add_argument("image", type=str, help="Docker image to run")
    run_parser.add_argument("--name", type=str, help="Container name", default="my-container")

    # log subcommand
    log_parser = subparsers.add_parser("log", help="Get container logs")
    log_parser.add_argument("containerID", type=str, help="Container ID")
    
    args = parser.parse_args()

    #--------logic for each sub command--------------
    try:
        if args.command == "run":
            container_id = run_container(args.image, args.name, args.debug)
            get_container_logs(container_id, args.debug)

        elif args.command == "log":
            get_container_logs(args.containerID)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()