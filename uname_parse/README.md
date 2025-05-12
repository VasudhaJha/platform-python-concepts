# Question 01 – Parse System Info from `uname -a`

## Problem

Write a Python script that runs the `uname -a` command and extracts key system information:

- Operating system (kernel name)
- Hostname
- Kernel version
- Architecture

This simulates how platform engineers might collect environment metadata for logging or diagnostics.

---

## Topics Practiced

- `subprocess.run()`
- `capture_output=True`, `text=True`
- Basic string parsing using `strip` and `split` methods.
- error handling

---
