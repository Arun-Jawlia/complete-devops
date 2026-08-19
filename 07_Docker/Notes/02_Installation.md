# Docker Installation Guide

Before installing Docker, understand one important point:

> **Docker runs differently depending on the operating system.**

For modern development, the most common setup is:

```text
Windows → Docker Desktop → WSL 2 → Linux containers
macOS   → Docker Desktop → Linux VM → Linux containers
Linux   → Docker Engine → Containers
```

---

# 1. Prerequisites Before Installing Docker

## Hardware prerequisites

Docker is lightweight compared with virtual machines, but you should have:

* 64-bit CPU
* At least **4 GB RAM** recommended
* Virtualization support enabled where required
* Sufficient disk space
* Administrator/root access for installation

For comfortable Docker + development work, I recommend:

```text
CPU:     4+ cores
RAM:     8 GB+
Storage: 20+ GB available
```

---

# 2. Operating System Prerequisites

## Windows

For Windows, the recommended setup is:

```text
Windows
   ↓
WSL 2
   ↓
Docker Desktop
   ↓
Linux Containers
```

Modern Docker Desktop uses **WSL 2** as the recommended backend for Linux containers.

You should generally have:

* Windows 10 64-bit, version 22H2 or later, or
* Windows 11 64-bit
* WSL 2
* Virtualization enabled in BIOS/UEFI
* A supported Windows edition for the chosen Docker Desktop configuration

### Check Windows version

Open PowerShell:

```powershell
winver
```

Or:

```powershell
systeminfo
```

---

# 3. macOS Prerequisites

Docker Desktop supports both:

```text
Apple Silicon
    ↓
M1 / M2 / M3 / M4 / newer Apple Silicon

Intel
    ↓
Intel-based Macs
```

You need:

* Supported macOS version
* 64-bit processor
* Sufficient RAM and disk space
* Administrator privileges for installation

### Check your Mac architecture

Open Terminal:

```bash
uname -m
```

You may see:

```text
arm64
```

This means:

> Apple Silicon

Or:

```text
x86_64
```

This means:

> Intel Mac

This matters because Docker Desktop provides different installers for Apple Silicon and Intel Macs.

---

# 4. Linux Prerequisites

Linux is slightly different.

You generally **do not need Docker Desktop**.

Instead:

```text
Linux
   ↓
Docker Engine
   ↓
Containers
```

Docker officially supports several Linux distributions, including commonly used distributions such as:

* Ubuntu
* Debian
* Fedora
* RHEL
* CentOS Stream
* openSUSE

Before installation, update your package manager.

For Ubuntu/Debian:

```bash
sudo apt update
```

Check your OS:

```bash
cat /etc/os-release
```

Check architecture:

```bash
uname -m
```

---

# 5. Installing Docker on Windows

## Step 1 — Enable WSL 2

Open **PowerShell as Administrator**:

```powershell
wsl --install
```

Restart Windows if requested.

Then check:

```powershell
wsl --status
```

You should have WSL 2 available.

You can also check installed distributions:

```powershell
wsl --list --verbose
```

Example:

```text
NAME      STATE      VERSION
Ubuntu    Running    2
```

The important part is:

```text
VERSION
   2
```

---

# 6. Install Docker Desktop on Windows

Download Docker Desktop from the official Docker website:

[Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/?utm_source=chatgpt.com)

Run the installer.

During installation, select the option to use:

```text
WSL 2 instead of Hyper-V
```

if presented and appropriate for your system.

After installation, restart if required.

Open:

```text
Docker Desktop
```

Wait until Docker reports that it is running.

---

# 7. Verify Docker on Windows

Open PowerShell:

```powershell
docker --version
```

Example:

```text
Docker version 29.x.x
```

Then:

```powershell
docker info
```

Finally run the official test container:

```powershell
docker run hello-world
```

If everything is working, Docker will:

```text
Docker CLI
    ↓
Docker Engine
    ↓
Pull hello-world image
    ↓
Create container
    ↓
Run container
    ↓
Print confirmation
```

---

# 8. Installing Docker on macOS

## Step 1 — Check architecture

Open Terminal:

```bash
uname -m
```

### Apple Silicon

If you get:

```text
arm64
```

download the **Apple Silicon** Docker Desktop installer.

### Intel

If you get:

```text
x86_64
```

download the **Intel** installer.

---

# 9. Download Docker Desktop for Mac

Use the official Docker website:

[Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/?utm_source=chatgpt.com)

Download the correct version:

```text
Apple Silicon
        OR
Intel
```

Open the downloaded `.dmg` file.

Then:

```text
Docker.app
     ↓
Applications
```

Launch Docker Desktop.

macOS may ask for permission to install privileged components. Approve the required permissions.

---

# 10. Verify Docker on macOS

Open Terminal:

```bash
docker --version
```

Then:

```bash
docker info
```

And test:

```bash
docker run hello-world
```

If successful, Docker is installed correctly.

---

# 11. Installing Docker on Ubuntu/Linux

For Linux, prefer **Docker Engine** rather than Docker Desktop for a server/development environment.

The recommended installation method is Docker's official repository.

[Docker Engine Installation Documentation](https://docs.docker.com/engine/install/?utm_source=chatgpt.com)

For Ubuntu, the basic process is:

```text
Remove conflicting packages
        ↓
Install prerequisites
        ↓
Add Docker's official GPG key
        ↓
Add Docker repository
        ↓
Install Docker Engine
        ↓
Start Docker
        ↓
Verify installation
```

---

# 12. Ubuntu — Install Docker Engine

First update the package index:

```bash
sudo apt update
```

Install prerequisites:

```bash
sudo apt install ca-certificates curl
```

Create the keyring directory:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
```

Download Docker's GPG key:

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
-o /etc/apt/keyrings/docker.asc
```

Set permissions:

```bash
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add Docker's official repository:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Update package information:

```bash
sudo apt update
```

Install Docker:

```bash
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---

# 13. Start Docker on Linux

Check Docker:

```bash
sudo systemctl status docker
```

If it isn't running:

```bash
sudo systemctl start docker
```

Enable Docker to start automatically:

```bash
sudo systemctl enable docker
```

---

# 14. Test Docker on Linux

Run:

```bash
sudo docker run hello-world
```

You should see Docker's confirmation message.

Check the installed version:

```bash
docker --version
```

Check Docker information:

```bash
sudo docker info
```

---

# 15. Running Docker Without `sudo`

By default, Linux users may need:

```bash
sudo docker ps
```

You can add your user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Then log out and log back in.

Alternatively:

```bash
newgrp docker
```

Now try:

```bash
docker ps
```

instead of:

```bash
sudo docker ps
```

### Important security point

Membership in the `docker` group effectively grants root-level control over the host. Therefore, treat access to the Docker socket/group as privileged access.

---

# 16. Verify Everything

Regardless of operating system, these commands are useful:

### Docker version

```bash
docker --version
```

### Docker information

```bash
docker info
```

### List running containers

```bash
docker ps
```

### List all containers

```bash
docker ps -a
```

### List images

```bash
docker images
```

### Test Docker

```bash
docker run hello-world
```

---

# 17. What Happens When You Run `docker run hello-world`?

This command is extremely important for understanding Docker.

```bash
docker run hello-world
```

Conceptually:

```text
             docker run hello-world
                       │
                       ↓
                 Docker CLI
                       │
                       ↓
                 Docker Engine
                       │
                       ↓
             Is image available?
                  /         \
                No           Yes
                │             │
                ↓             │
          Pull image          │
                │             │
                └──────┬──────┘
                       ↓
                Create container
                       ↓
                  Start container
                       ↓
                  Run application
                       ↓
                  Container exits
```

The `hello-world` container is intentionally short-lived. It prints its message and then exits.

---

# 18. Docker Architecture After Installation

Once Docker is installed, think about the system like this.

### Windows

```text
Windows
   │
   └── Docker Desktop
          │
          └── WSL 2 / Linux environment
                 │
                 └── Docker Engine
                        │
                        ├── Images
                        ├── Containers
                        ├── Networks
                        └── Volumes
```

### macOS

```text
macOS
  │
  └── Docker Desktop
         │
         └── Linux VM
                │
                └── Docker Engine
                       │
                       ├── Images
                       ├── Containers
                       ├── Networks
                       └── Volumes
```

### Linux

```text
Linux
  │
  └── Docker Engine
         │
         ├── Images
         ├── Containers
         ├── Networks
         └── Volumes
```

---

# 19. Docker Desktop vs Docker Engine

This distinction is important for DevOps.

| Docker Desktop                        | Docker Engine                   |
| ------------------------------------- | ------------------------------- |
| Primarily used on Windows/macOS       | Native Linux container runtime  |
| GUI included                          | Primarily CLI/service based     |
| Includes Docker Engine                | Docker Engine itself            |
| Easy for developers                   | Common on Linux servers         |
| Uses a lightweight VM/WSL integration | Uses Linux host kernel directly |

A common professional setup is:

```text
Developer Laptop
      ↓
Docker Desktop
      ↓
Development
```

while production might use:

```text
Linux Server
      ↓
Docker Engine
      ↓
Containers
```

---

# 20. Installation Mental Model

Keep this hierarchy in your notes:

```text
                    Docker
                      │
          ┌───────────┴───────────┐
          │                       │
     Docker Desktop          Docker Engine
          │                       │
     ┌────┴────┐                  │
     │         │                  │
  Windows    macOS              Linux
     │         │                  │
     ↓         ↓                  ↓
   WSL 2    Linux VM        Native Linux
     │         │                  │
     └─────────┴──────────┬───────┘
                          ↓
                    Docker Engine
                          ↓
                  ┌───────┼────────┐
                  ↓       ↓        ↓
               Images  Containers Networks
```

## Commands you should memorize

```bash
docker --version
docker info
docker ps
docker ps -a
docker images
docker run hello-world
```

The next logical topic is **Docker Architecture**: Docker CLI, Docker Daemon/Engine, containerd, runc, images, containers, registries, and how `docker run` actually flows through these components.
