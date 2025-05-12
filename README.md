# Platform Engineering with Python – Concepts & Practice

This repository is my personal knowledge base and practice ground for using Python in Platform Engineering.

I'm documenting everything I'm learning through hands-on examples — from scripting and automation to system process control and error handling — with the goal of building strong engineering habits and preparing for real-world Platform roles.

This repo will:

- Document platform engineering concepts that are often scattered
- Build small, testable scripts as learning tools

---

## Topics Covered

### subprocess/

- Running shell commands securely
- Capturing output, handling failures
- Preventing shell injection
- Example: Running Docker containers with subprocess

### argparse/

- Building clean, maintainable CLIs
- Subcommands, boolean flags, and validation
- Example: Docker wrapper with `run`, `stop`, `build` commands

### error_handling/

- try/except blocks
- Handling `CalledProcessError` in automation scripts
- Using `else`, `finally` effectively

### logging/

- Logging levels (`DEBUG`, `INFO`, `ERROR`)
- Structured logging for CLI tools

### file_ops/

- Reading/writing config files
- Safely handling paths and deletions

---

## How to Use This Repo

- Browse each folder to see a specific concept in action
- Run the example scripts directly (Python 3.8+)
- Use it as a reference when writing your own platform tools

---

## Contributions

This is a personal learning repo, but I'm happy to receive thoughtful suggestions or improvements!
