# Check if Docker is Installed and Running

## Problem

Write a Python script that uses `subprocess` to check the system’s Docker installation and daemon status.

The script should:

- Print “Docker is running” if `docker info` succeeds
- Print “Docker is installed but not running” if the CLI exists but the daemon isn't responsive
- Print “Docker is not installed” if the `docker` command is missing entirely

---

## Topics Practiced

- `subprocess.run()`
- `check=True` and `capture_output=True`
- Handling `CalledProcessError` vs `FileNotFoundError`
- Graceful CLI-based system diagnostics

---
