# Run a Docker Container and Print Logs

## Problem

Write a Python script that:

1. Accepts a Docker image name (e.g. `nginx`)
2. Runs the image in **detached mode** and captures the container ID
3. Waits for 2 seconds to allow the container to initialize
4. Prints the container’s logs using `docker logs <container_id>`

---

## 🧪 Topics Practiced

- `subprocess.run()` with multiple subcommands
- `capture_output=True`, `text=True`, and `.stdout.strip()`
- Error handling with `CalledProcessError`
- Accepting user input with `argparse`

---
