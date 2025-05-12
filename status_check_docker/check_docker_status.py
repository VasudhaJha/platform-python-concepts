import subprocess
import argparse

def check_docker_status(debug=False):
    try:
        subprocess.run(["docker", "info"], check=True, capture_output=True, text=True)
        print("Docker is running.")
    except subprocess.CalledProcessError as e:
        print("Docker is installed but the daemon is not running.")
        if debug:
            print("-----------------")
            print("DETAILS")
            print("-----------------")
            print(e.stderr.strip())

    except FileNotFoundError as e:
        print("Docker is not installed.")

def main():
    parser = argparse.ArgumentParser(description="Check docker installation and daemon status")
    parser.add_argument("--debug", action="store_true", help="Print detailed error output")
    args = parser.parse_args()

    check_docker_status(debug=args.debug)


if __name__ == "__main__":
    main()