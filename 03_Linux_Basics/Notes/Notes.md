# Introduction to Linux

## What is Linux?

Linux is an **open-source operating system kernel** created by **Linus Torvalds in 1991**.

Technically, Linux is the **kernel**, not the complete operating system. The kernel manages communication between hardware and software.

```text
Applications
     ↓
Linux Distribution
     ↓
Linux Kernel
     ↓
Hardware
```

Examples of Linux distributions:

* Ubuntu
* Debian
* Fedora
* Red Hat Enterprise Linux (RHEL)
* Arch Linux
* Kali Linux

---

## Who Created Linux?

**Linus Torvalds** created the Linux kernel in **1991** while he was a student at the University of Helsinki.

He released it as an open-source project, allowing other developers to use, modify, and contribute to it.

Today, Linux is maintained by a large global community and organizations.

---

# GNU and GPL

## GNU

**GNU** stands for **GNU's Not Unix**.

The GNU project was started by **Richard Stallman in 1983** with the goal of creating a completely free and open-source Unix-like operating system.

GNU provides many important tools used in Linux systems, such as:

* Bash
* GCC
* Core utilities
* GNU tools and libraries

Linux kernel + GNU tools are commonly used together to create a complete operating system environment.

---

## GPL

**GPL** stands for **GNU General Public License**.

It is an open-source software license.

The Linux kernel is released under **GPL version 2 (GPLv2)**.

The GPL allows users to:

* Use the software
* Study the source code
* Modify the software
* Redistribute the software

If modified GPL software is distributed, the corresponding source code must generally be made available under the GPL's terms.

---

# Uses of Linux

Linux is widely used because it is stable, flexible, secure, and highly customizable.

### 1. Servers

Linux powers a large number of web and application servers.

Examples:

* Web servers
* Database servers
* Application servers
* File servers

### 2. Cloud Computing

Most cloud platforms provide Linux-based virtual machines.

Linux is heavily used in:

* AWS
* Azure
* GCP
* Kubernetes environments

### 3. DevOps

Linux is one of the most important operating systems for DevOps engineers.

It is commonly used with:

* Docker
* Kubernetes
* Jenkins
* Terraform
* Ansible
* Git

### 4. Embedded Systems

Linux is used in:

* Routers
* Smart TVs
* IoT devices
* Automotive systems

### 5. Android

Android uses the **Linux kernel** as its kernel layer.

### 6. Cybersecurity

Linux distributions such as Kali Linux provide tools for security testing and penetration testing.

---

# Advantages of Linux

### Open Source

Its source code is publicly available and can be studied and modified.

### Free

Most Linux distributions can be used without purchasing an operating-system license.

### Secure

Linux provides strong permissions, user management, and security mechanisms.

### Stable

Linux systems can run for long periods with minimal downtime.

### Lightweight

Many Linux distributions can run efficiently even on systems with limited resources.

### Customizable

Users can customize the system, desktop environment, services, and configuration.

### Automation Friendly

Linux provides powerful command-line tools and scripting capabilities, making it ideal for DevOps automation.

---

# Disadvantages of Linux

### Learning Curve

The command line and system administration concepts can be difficult for beginners.

### Software Compatibility

Some commercial applications are primarily designed for Windows or macOS.

### Hardware Support

Certain hardware devices may have limited Linux driver support.

### Gaming

Linux gaming has improved significantly, but some games and anti-cheat systems may still have compatibility issues.

### Manual Configuration

Some tasks may require configuration through the terminal instead of a graphical interface.

---

# Linux Commands

Linux is heavily operated through the **Command Line Interface (CLI)**.

## Navigation

```bash
pwd
```

Shows the current directory.

```bash
ls
```

Lists files and directories.

```bash
cd directory
```

Changes the current directory.

```bash
cd ..
```

Moves one directory up.

---

## File and Directory Management

```bash
mkdir project
```

Creates a directory.

```bash
touch file.txt
```

Creates an empty file.

```bash
cp file.txt backup.txt
```

Copies a file.

```bash
mv file.txt documents/
```

Moves a file.

```bash
rm file.txt
```

Deletes a file.

```bash
rm -r directory
```

Deletes a directory and its contents.

---

## Reading Files

```bash
cat file.txt
```

Displays the file contents.

```bash
less file.txt
```

Opens a file for scrolling.

```bash
head file.txt
```

Shows the beginning of a file.

```bash
tail file.txt
```

Shows the end of a file.

---

## System Information

```bash
whoami
```

Shows the current user.

```bash
uname -a
```

Displays system information.

```bash
df -h
```

Shows disk usage.

```bash
free -h
```

Shows memory usage.

```bash
top
```

Displays running processes and resource usage.

---

## Permissions

```bash
chmod
```

Changes file permissions.

```bash
chown
```

Changes file ownership.

Example:

```bash
chmod 755 script.sh
```

---

## Networking

```bash
ip addr
```

Displays network interfaces and IP addresses.

```bash
ping google.com
```

Tests network connectivity.

```bash
curl https://example.com
```

Makes an HTTP request.

```bash
ss -tuln
```

Shows listening network sockets.

---

## Package Management — Ubuntu/Debian

```bash
sudo apt update
```

Updates package information.

```bash
sudo apt install nginx
```

Installs Nginx.

```bash
sudo apt remove nginx
```

Removes Nginx.

---

# Important Linux Concept

A useful way to remember Linux in DevOps:

```text
Linux
 │
 ├── File System
 ├── Users & Groups
 ├── Permissions
 ├── Processes
 ├── Services
 ├── Networking
 ├── Package Management
 ├── Shell
 └── Shell Scripting
```

These concepts form the foundation for later DevOps topics such as **Docker, Kubernetes, AWS, Terraform, Jenkins, and Ansible**.

