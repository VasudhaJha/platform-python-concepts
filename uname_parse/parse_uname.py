import subprocess
from typing import Dict

def get_system_info() -> Dict:
    try:
        result = subprocess.run(["uname", "-a"], check=True, capture_output=True, text=True)
        output = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Failed to run: {e}")
        
    components = output.split()
    if len(components) < 4:
        raise ValueError("Unexpected uname output format.")

    return {
        "os": components[0],
        "hostname": components[1],
        "kernel_version": components[2],
        "architecture": components[-1]
    }

def main():
    try:
        info = get_system_info()
        print(f"OS: {info['os']}")
        print(f"Hostname: {info['hostname']}")
        print(f"Kernel version: {info['kernel_version']}")
        print(f"Architecture: {info['architecture']}")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

