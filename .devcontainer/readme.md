# Dev Container Guide

This directory contains a pre-configured VS Code Dev Container. 
Provided is an isolated Debian environment with toolchains for C++, CMake, Latex, Python3, and Typst.

## Requirements

1. **Docker**
- Linux: Install for your distro, add user to Docker group, then run the Docker daemon
- macOS: Docker Desktop or OrbStack
- Windows: Docker Desktop
2. **VS Code**
3. **Dev Container VS Code Extension** (`ms-vscode-remote.remote-containers`)

## Environment Setup

1. Open the project root in VS Code
2. Press `ctrl + shift + p` / `cmd + shft + p`, type *Dev Containers: Reopen in Container*, press `enter`

## Testing the Environment

Open a terminal `ctrl + ~` and run:
```sh
g++ --version
pdflatex --version
typst --version
python --version
```
the versions should print if all was set up correctly.

## Making Changes

You can update and add to the container as needed. Inform the team of the changes made and follow these steps:

1. Press `ctrl + shift + p` / `cmd + shift + p`
2. Type `Dev Containers: Rebuild Container` and hit `enter`

The changes will then be applied to the Docker image. If you need a package or development tool just for yourself, you can always use `pip` or `apt`.

## Stopping and Deleting the Container

The container runs entirely inside of Docker's storage directory, and does not alter the host systems libraries or binaries. You can delete the container either by:

1. Going to the Remote Explorer sidebar tab in VS Code, or
2. Via the terminal

```sh
docker rm -f $(docker ps -aq --filter name=MusicMaster2027)
docker image prune -a
```