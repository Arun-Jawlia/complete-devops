# Docker Fundamentals

Let’s build the concepts in the correct order:

**Application → Container → Container Image → Container Registry → Docker**

---

# 1. What is Docker?

**Docker is a platform used to build, package, distribute, and run applications inside containers.**

The key idea is:

> **Docker packages an application together with everything it needs to run, so it can run consistently across different environments.**

For example, suppose you build a Python application.

Your application may require:

```text
Python 3.12
Flask
NumPy
Pandas
Environment variables
System libraries
Your application code
```

Without Docker, you might have:

```text
Developer Machine
    ↓
Python 3.12
    ↓
Dependencies
    ↓
Application
```

But another developer might have:

```text
Developer Machine
    ↓
Python 3.10
    ↓
Different dependencies
    ↓
Application
```

Then you get the famous problem:

> **"It works on my machine!"**

Docker addresses this by packaging the application and its environment into a **container image**.

```text
              Docker Image
                   │
        ┌──────────┴──────────┐
        │                     │
   Application             Dependencies
        │                     │
        └──────────┬──────────┘
                   ↓
              Container
                   ↓
             Running App
```

---

# 2. What is a Container?

A **container is an isolated runtime environment in which an application runs.**

A container contains the things your application needs to execute, such as:

* Application code
* Libraries
* Dependencies
* Configuration
* Runtime environment

But there is an important distinction:

### Container ≠ Image

Think of it like this:

```text
Docker Image
     ↓
   Template
     ↓
Docker Container
     ↓
 Running instance
```

For example:

```text
Python Flask Image
        ↓
        ├── Container 1
        ├── Container 2
        └── Container 3
```

One image can be used to create multiple containers.

### Simple analogy

Think of an **image as a class** in programming.

```python
class Car:
    pass
```

And a **container as an object/instance**:

```python
car1 = Car()
car2 = Car()
car3 = Car()
```

Similarly:

```text
Image
  ↓
  ├── Container 1
  ├── Container 2
  └── Container 3
```

---

# 3. What Problem Does a Container Solve?

Before containers, deploying applications could look like this:

```text
Developer
   ↓
Application
   ↓
Copy application to server
   ↓
Install Python
   ↓
Install libraries
   ↓
Configure environment
   ↓
Configure OS dependencies
   ↓
Run application
```

This creates many potential problems.

### Problem 1: Environment differences

Developer:

```text
Python 3.12
```

Production:

```text
Python 3.10
```

Application may behave differently.

---

### Problem 2: Dependency conflicts

Application A requires:

```text
Django 4
```

Application B requires:

```text
Django 5
```

Installing both directly on the same machine can become problematic.

Containers isolate them:

```text
Server
│
├── Container A
│     └── Django 4
│
└── Container B
      └── Django 5
```

---

### Problem 3: Difficult deployment

Without containers, deployment often involves manually configuring:

```text
OS
Python
Node
Java
Libraries
Environment variables
System packages
Configuration
```

With Docker:

```text
Docker Image
     ↓
     Run
     ↓
Container
     ↓
Application
```

The environment becomes much more reproducible.

---

### Problem 4: "Works on my machine"

Docker gives developers a much more consistent environment.

```text
Developer Machine
       │
       ↓
   Docker Image
       │
       ↓
     Docker
       │
       ↓
   Container
       │
       ↓
   Application
```

The same image can be deployed to:

```text
Development
      ↓
Testing
      ↓
Staging
      ↓
Production
```

---

# 4. What is a Container Image?

This is an important Docker concept.

A **Docker image is an immutable package/template containing the filesystem, application, dependencies, and metadata required to create a container.**

For example:

```text
Python Flask Application Image
│
├── Python
├── Flask
├── Dependencies
├── Application Code
├── Configuration
└── Startup Command
```

The image itself isn't the running application.

When you execute:

```bash
docker run my-flask-app
```

Docker creates a container from the image.

```text
my-flask-app:latest
        │
        │ docker run
        ↓
   Container
        │
        ↓
 Flask Application
```

---

# 5. Where Do Containers Live?

This question needs a precise answer.

Containers **run on a machine that has a container runtime**, such as Docker Engine.

For example:

```text
Your Laptop
│
└── Docker Engine
      │
      ├── Container 1
      ├── Container 2
      └── Container 3
```

They can run on:

* Your laptop
* Development server
* Virtual machine
* Cloud VM
* Kubernetes nodes
* CI/CD runners
* Cloud container services

For example:

```text
AWS EC2
   │
   └── Docker Engine
          │
          ├── Backend Container
          ├── Frontend Container
          └── Redis Container
```

So:

> **Containers live/run on container hosts.**

---

# 6. Where Do Container Images Live?

This is where **Container Registries** come in.

A **container registry is a storage and distribution system for container images.**

Examples include:

* Docker Hub
* GitHub Container Registry
* Amazon Elastic Container Registry (ECR)
* Google Artifact Registry
* Azure Container Registry (ACR)
* GitLab Container Registry

The basic workflow is:

```text
Developer
    │
    │ docker build
    ↓
Docker Image
    │
    │ docker push
    ↓
Container Registry
    │
    │ docker pull
    ↓
Production Server
    │
    │ docker run
    ↓
Container
```

---

# 7. Docker Hub Example

Suppose you build a Python application.

You create an image:

```bash
docker build -t myapp .
```

Now you have:

```text
myapp
```

You push it to Docker Hub:

```bash
docker push username/myapp:latest
```

Now the image is stored in the registry:

```text
Docker Hub
   │
   └── username/myapp:latest
```

A production server can download it:

```bash
docker pull username/myapp:latest
```

Then run it:

```bash
docker run username/myapp:latest
```

The complete flow:

```text
             BUILD
Developer ─────────────→ Docker Image
                              │
                              │ PUSH
                              ↓
                       Container Registry
                              │
                              │ PULL
                              ↓
                         Server
                              │
                              │ RUN
                              ↓
                         Container
                              │
                              ↓
                        Application
```

---

# 8. Container vs Container Registry

These are often confused.

| Concept           | Purpose                                    |
| ----------------- | ------------------------------------------ |
| **Container**     | Runs the application                       |
| **Image**         | Template/package used to create containers |
| **Registry**      | Stores and distributes images              |
| **Docker Engine** | Builds and runs containers                 |
| **Dockerfile**    | Instructions for building an image         |

Think:

```text
Dockerfile
    ↓
 docker build
    ↓
Image
    ↓
 docker push
    ↓
Registry
    ↓
 docker pull
    ↓
Image
    ↓
 docker run
    ↓
Container
    ↓
Application
```

---

# 9. Dockerfile

A **Dockerfile** contains instructions for creating a Docker image.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Then:

```bash
docker build -t myapp .
```

Docker reads the Dockerfile and creates:

```text
Dockerfile
    ↓
Docker Build
    ↓
myapp Image
```

---

# 10. Containerization

The process of packaging an application into a container image and running it as a container is called **containerization**.

Traditional deployment:

```text
Application
     ↓
Install dependencies
     ↓
Configure server
     ↓
Configure environment
     ↓
Run application
```

Containerized deployment:

```text
Application
     ↓
Dockerfile
     ↓
Docker Image
     ↓
Container
     ↓
Running Application
```

---

# 11. Containers vs Virtual Machines

This is one of the most important Docker concepts.

### Virtual Machine

```text
Physical Server
│
├── Host OS
│
├── VM 1
│    ├── Guest OS
│    └── Application
│
└── VM 2
     ├── Guest OS
     └── Application
```

Each VM generally contains its own complete guest operating system.

### Containers

```text
Physical Server
│
├── Host OS
│
└── Docker Engine
      │
      ├── Container 1
      ├── Container 2
      └── Container 3
```

Containers share the host kernel, which generally makes them much lighter and faster to start than full VMs.

---

# 12. Why Containers Became Important in DevOps

Containers fit naturally into the DevOps lifecycle:

```text
Develop
   ↓
Build
   ↓
Test
   ↓
Package
   ↓
Deploy
   ↓
Monitor
```

Docker provides a consistent artifact:

```text
             Docker Image
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
    Testing    Staging   Production
        │         │         │
        ↓         ↓         ↓
    Container  Container  Container
```

This helps reduce environment inconsistencies between development and production.

---

# 13. The Big Picture

Remember this architecture:

```text
                    Dockerfile
                        │
                        │ docker build
                        ↓
                 ┌──────────────┐
                 │ Docker Image  │
                 └──────┬───────┘
                        │
                        │ docker push
                        ↓
              ┌─────────────────────┐
              │ Container Registry  │
              │                     │
              │ Docker Hub / ECR    │
              │ GHCR / ACR / GAR    │
              └──────────┬──────────┘
                         │
                         │ docker pull
                         ↓
                   Server / VM
                         │
                    Docker Engine
                         │
                         │ docker run
                         ↓
                  ┌──────────────┐
                  │  Container   │
                  │              │
                  │ Application  │
                  └──────────────┘
```

## The 5 concepts to remember

**1. Docker**
A platform/tooling ecosystem for building, packaging, distributing, and running containers.

**2. Dockerfile**
Instructions for building an image.

**3. Image**
Immutable package/template containing what is needed to create a container.

**4. Container**
A running, isolated instance created from an image.

**5. Container Registry**
A place where container images are stored and distributed.

### One-line mental model

> **Dockerfile → Image → Registry → Pull → Container → Application**

This flow is the foundation for understanding the next Docker topics: **Docker architecture, Docker Engine, Docker CLI, Dockerfile instructions, images/layers, volumes, networks, Docker Compose, and Dockerizing a real application.**
