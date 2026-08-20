# Docker Images — Complete Notes: Basic to Advanced

Docker **Image** is one of the most important concepts in Docker. If you understand images properly, containers, Dockerfiles, registries, Docker Compose, and production deployments become much easier to understand.

---

# 1. What is a Docker Image?

A **Docker Image** is a **read-only, immutable template** used to create Docker containers.

Think of it like a **blueprint**.

```text
Docker Image
     │
     │ docker run
     ▼
Docker Container
```

For example, suppose you want to run a Python application.

Your application needs:

```text
Python
Flask
Application Code
Dependencies
Configuration
```

You can package all of these into a Docker Image.

Then anyone with Docker can create a container from that image.

```text
Python Image
     +
Application Code
     +
Dependencies
     ↓
Docker Image
     ↓
Docker Container
```

---

# 2. Image vs Container

This distinction is critical.

| Docker Image              | Docker Container                 |
| ------------------------- | -------------------------------- |
| Blueprint/template        | Running instance                 |
| Read-only                 | Has a writable layer             |
| Used to create containers | Created from an image            |
| Immutable                 | Has runtime state                |
| Stored locally/registry   | Runs on Docker Engine            |
| Example: `nginx:latest`   | Example: running Nginx container |

Analogy:

```text
Class       → Object
Image       → Container
Blueprint   → Building
Recipe      → Prepared Food
```

One image can create many containers:

```text
             Docker Image
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
 Container 1  Container 2  Container 3
```

---

# 3. Where Do Docker Images Live?

Images can exist in several places.

### 1. Local machine

```bash
docker images
```

Images are stored by the Docker Engine on your machine.

### 2. Docker Hub

Public registry:

```text
Docker Hub
    ↓
docker pull nginx
```

### 3. Private registries

Examples:

* AWS ECR
* Google Artifact Registry
* Azure Container Registry
* GitHub Container Registry
* Harbor

General architecture:

```text
Developer Machine
       │
       │ docker push
       ▼
Container Registry
       │
       │ docker pull
       ▼
Production Server
```

---

# 4. What Does a Docker Image Contain?

An image can contain:

```text
Base Operating System files
        +
Runtime
        +
Libraries
        +
Dependencies
        +
Application Code
        +
Configuration
```

For example:

```text
Python Application Image

Ubuntu/Debian files
       ↓
Python
       ↓
pip packages
       ↓
Flask
       ↓
Application
```

Important:

A Docker image **does not contain a complete virtual machine**.

It generally contains the filesystem/user-space components needed by the application while sharing the host kernel.

---

# 5. Docker Image Layers

Docker images are **layered**.

For example:

```text
Application Code
       ↓
Python Dependencies
       ↓
Python Runtime
       ↓
Base Image
```

Each Dockerfile instruction can create a filesystem layer.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Conceptually:

```text
Layer 4 → COPY application
Layer 3 → RUN pip install
Layer 2 → WORKDIR
Layer 1 → FROM python
```

Layers provide:

* caching
* reuse
* faster builds
* efficient storage
* easier distribution

---

# 6. What is an Image Tag?

An image usually has:

```text
repository:tag
```

Example:

```bash
nginx:latest
```

Here:

```text
nginx  → repository
latest → tag
```

Another example:

```bash
python:3.12
```

```text
python → repository
3.12   → tag
```

You can also use:

```bash
python:3.12-slim
```

or:

```bash
node:22-alpine
```

---

# 7. Image Name Structure

A Docker image reference can be more complex:

```text
registry/namespace/repository:tag
```

Example:

```bash
docker.io/library/nginx:latest
```

Breakdown:

```text
docker.io   → registry
library      → namespace
nginx        → repository
latest       → tag
```

Private registry example:

```bash
123456789.dkr.ecr.ap-south-1.amazonaws.com/myapp:v1
```

---

# 8. Basic Image Commands

## List Images

```bash
docker images
```

or:

```bash
docker image ls
```

Example:

```text
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    abc123         2 days ago    192MB
python       3.12      def456         4 days ago    1.02GB
```

---

# 9. List All Images

By default, dangling/intermediate images may not be shown.

Use:

```bash
docker images -a
```

Equivalent:

```bash
docker image ls -a
```

---

# 10. Pull an Image

Download an image from a registry.

```bash
docker pull nginx
```

Specific tag:

```bash
docker pull nginx:1.27
```

Python:

```bash
docker pull python:3.12
```

Ubuntu:

```bash
docker pull ubuntu:24.04
```

---

# 11. Pull From a Specific Registry

```bash
docker pull docker.io/library/nginx:latest
```

Private registry:

```bash
docker pull myregistry.com/myteam/myapp:v1
```

---

# 12. Run an Image

You can create a container from an image using:

```bash
docker run nginx
```

Docker essentially does:

```text
Image
  ↓
Create container
  ↓
Start container
```

---

# 13. Run Image in Background

```bash
docker run -d nginx
```

`-d` means:

```text
detached mode
```

The container runs in the background.

---

# 14. Run With a Custom Container Name

```bash
docker run --name my-nginx nginx
```

Then:

```bash
docker ps
```

You might see:

```text
my-nginx
```

---

# 15. Run Image With Port Mapping

Suppose Nginx listens on:

```text
Container port: 80
```

Map it to host port 8080:

```bash
docker run -d -p 8080:80 nginx
```

Meaning:

```text
Host                 Container
8080  ─────────────→ 80
```

Access:

```text
http://localhost:8080
```

---

# 16. Run Specific Image Version

```bash
docker run nginx:1.27
```

Python:

```bash
docker run python:3.12
```

Node:

```bash
docker run node:22
```

Avoid depending blindly on:

```bash
:latest
```

Production systems commonly prefer explicit version tags or immutable digests.

---

# 17. Inspect an Image

One of the most useful commands:

```bash
docker image inspect nginx
```

or:

```bash
docker inspect nginx
```

It provides information such as:

* image ID
* architecture
* OS
* environment variables
* entrypoint
* command
* layers
* configuration
* metadata

---

# 18. Inspect Specific Information

You can use Go templates.

Example:

```bash
docker image inspect nginx --format '{{.Architecture}}'
```

Get OS:

```bash
docker image inspect nginx --format '{{.Os}}'
```

Get entrypoint:

```bash
docker image inspect nginx --format '{{.Config.Entrypoint}}'
```

Get command:

```bash
docker image inspect nginx --format '{{.Config.Cmd}}'
```

---

# 19. Check Image History

Very useful for understanding image layers:

```bash
docker history nginx
```

Example:

```text
IMAGE       CREATED       CREATED BY
abc123      2 days ago    CMD ["nginx"...]
def456      2 days ago    COPY ...
ghi789      2 days ago    RUN ...
```

This helps answer:

> How was this image constructed?

---

# 20. Show Image History Without Truncation

```bash
docker history --no-trunc nginx
```

Useful when the command output is shortened.

---

# 21. Remove an Image

```bash
docker rmi nginx
```

or:

```bash
docker image rm nginx
```

You can use the image ID:

```bash
docker rmi abc123
```

---

# 22. Force Remove an Image

```bash
docker rmi -f nginx
```

Be careful with `-f`.

It should not be your default solution for image cleanup.

---

# 23. Remove Multiple Images

```bash
docker rmi nginx ubuntu python
```

---

# 24. Remove Dangling Images

Dangling images are usually untagged intermediate images.

```bash
docker image prune
```

Docker asks for confirmation.

Use:

```bash
docker image prune -f
```

to skip confirmation.

---

# 25. Remove Unused Images

```bash
docker image prune -a
```

This removes unused images, not only dangling ones.

Be careful:

```bash
docker image prune -a
```

can remove images you may want to reuse later.

---

# 26. Rename/Tag an Image

Docker uses `tag` to create another name/reference for an existing image.

```bash
docker tag nginx my-nginx:v1
```

Now:

```bash
docker images
```

may show:

```text
nginx       latest
my-nginx    v1
```

The tag operation does not necessarily duplicate the underlying image data.

---

# 27. Tag an Image for Docker Hub

Suppose your Docker Hub username is:

```text
myusername
```

Tag:

```bash
docker tag myapp myusername/myapp:v1
```

Now:

```text
myusername/myapp:v1
```

is ready to push.

---

# 28. Login to Docker Registry

For Docker Hub:

```bash
docker login
```

You will authenticate with your registry credentials.

For another registry:

```bash
docker login registry.example.com
```

---

# 29. Push an Image

```bash
docker push myusername/myapp:v1
```

Flow:

```text
Local Image
    │
    │ docker push
    ▼
Docker Hub
```

---

# 30. Pull Your Own Image

On another machine:

```bash
docker pull myusername/myapp:v1
```

Then:

```bash
docker run myusername/myapp:v1
```

---

# 31. Docker Save

`docker save` exports an image to a tar archive.

```bash
docker save nginx -o nginx.tar
```

You now have:

```text
nginx.tar
```

This is useful for transferring Docker images without using a registry.

---

# 32. Docker Load

Load an image from a tar file:

```bash
docker load -i nginx.tar
```

Flow:

```text
Machine A
Docker Image
    ↓
docker save
    ↓
nginx.tar
    ↓
Transfer
    ↓
Machine B
    ↓
docker load
    ↓
Docker Image
```

---

# 33. Docker Export vs Docker Save

These are commonly confused.

### `docker save`

Works with:

```text
IMAGE
```

Example:

```bash
docker save nginx -o nginx.tar
```

Preserves image information and layers.

### `docker export`

Works with:

```text
CONTAINER
```

Example:

```bash
docker export my-container -o container.tar
```

It exports the container filesystem.

Important:

```text
docker save   → Image
docker export → Container
```

---

# 34. Import an Image From a Tar File

You can use:

```bash
docker import container.tar myimage:v1
```

This creates an image from a filesystem archive.

Conceptually:

```text
Container filesystem
       ↓
docker export
       ↓
tar
       ↓
docker import
       ↓
new image
```

---

# 35. Docker Image Digest

Tags can move.

For example:

```text
nginx:latest
```

may point to a different image later.

A digest identifies a specific image content.

Example:

```text
nginx@sha256:abc123...
```

Pulling by digest:

```bash
docker pull nginx@sha256:...
```

This is useful when you need immutable image references.

---

# 36. Image ID vs Digest

### Image ID

Local Docker identifier.

Example:

```text
sha256:abc123...
```

### Digest

Registry content identifier.

Example:

```text
nginx@sha256:abc123...
```

They are related to content identity but are not simply interchangeable concepts.

---

# 37. Check Image Size

```bash
docker images
```

or:

```bash
docker image ls
```

Example:

```text
REPOSITORY   TAG       SIZE
python       3.12      1.02GB
python       3.12-slim 150MB
```

This is important for production.

Smaller image:

```text
↓
Less storage
↓
Faster pull
↓
Faster deployment
↓
Smaller attack surface
```

---

# 38. List Image IDs

```bash
docker images -q
```

Example:

```text
abc123
def456
ghi789
```

Useful for scripting.

---

# 39. List Only Dangling Images

```bash
docker images -f dangling=true
```

or:

```bash
docker image ls --filter dangling=true
```

---

# 40. Filter Images

Example:

```bash
docker images --filter reference="nginx"
```

Another example:

```bash
docker image ls --filter dangling=true
```

---

# 41. Search for Images

Docker Hub search:

```bash
docker search nginx
```

Example:

```bash
docker search python
```

This searches available public images.

For serious production selection, verify the image's publisher, maintenance status, vulnerabilities, provenance, and documentation rather than selecting purely by popularity.

---

# 42. Create Your Own Docker Image

There are two major approaches:

### Approach 1 — Dockerfile

Recommended.

```text
Dockerfile
     ↓
docker build
     ↓
Docker Image
```

### Approach 2 — Commit a Container

```text
Container
   ↓
docker commit
   ↓
Image
```

For reproducible builds, **Dockerfile-based builds are preferred**.

---

# 43. What is a Dockerfile?

A Dockerfile is a text file containing instructions used to build a Docker image.

Example:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Build:

```bash
docker build -t my-python-app:v1 .
```

---

# 44. Docker Build Command

Basic:

```bash
docker build -t myapp .
```

Meaning:

```text
docker build
     │
     ├── -t myapp
     │
     └── . → build context
```

---

# 45. Build With a Specific Tag

```bash
docker build -t myapp:v1 .
```

Another:

```bash
docker build -t myapp:1.0.0 .
```

---

# 46. Build Using a Different Dockerfile

Suppose:

```text
Dockerfile.dev
Dockerfile.prod
```

Build:

```bash
docker build -f Dockerfile.prod -t myapp:prod .
```

---

# 47. Build With Multiple Tags

```bash
docker build \
  -t myapp:v1 \
  -t myapp:latest \
  .
```

One build can produce multiple references to the same image.

---

# 48. Build Without Cache

```bash
docker build --no-cache -t myapp:v1 .
```

Useful when Docker's build cache is causing unexpected behavior.

But don't use it routinely because it makes builds slower.

---

# 49. Pull Latest Base Image During Build

```bash
docker build --pull -t myapp:v1 .
```

This asks Docker to attempt to pull a newer version of the base image.

---

# 50. Build Progress Output

Modern Docker builds use BuildKit.

You can use:

```bash
docker build --progress=plain -t myapp .
```

This provides more detailed build output.

Useful for debugging.

---

# 51. Build From STDIN

Docker can receive a Dockerfile through standard input:

```bash
docker build -t myapp -f - .
```

This is more advanced and useful in automation.

---

# 52. Build Context

When you execute:

```bash
docker build -t myapp .
```

the `.` means:

> Send the current directory as the build context.

For example:

```text
project/
├── Dockerfile
├── app.py
├── requirements.txt
└── .dockerignore
```

Docker can access files within the build context.

---

# 53. `.dockerignore`

Very important for image optimization.

Example:

```text
.git
.gitignore
node_modules
__pycache__
.env
venv
*.log
```

Without `.dockerignore`, unnecessary files can be sent as part of the build context.

---

# 54. Docker Commit

You can create an image from an existing container.

Example:

```bash
docker commit my-container myapp:v1
```

Flow:

```text
Running Container
       ↓
docker commit
       ↓
Docker Image
```

However, this is generally not preferred for production builds because the build process becomes difficult to reproduce.

Prefer:

```text
Dockerfile
    ↓
docker build
    ↓
Image
```

---

# 55. Image Management With Docker Compose

Docker Compose can build images.

Example:

```yaml
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
```

Run:

```bash
docker compose build
```

Build and start:

```bash
docker compose up --build
```

---

# 56. Build Image With Build Arguments

Dockerfile:

```dockerfile
ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION}
```

Build:

```bash
docker build \
  --build-arg PYTHON_VERSION=3.11 \
  -t myapp .
```

`ARG` is primarily a **build-time variable**.

Do not use `ARG` for secrets.

---

# 57. Image Labels

You can add metadata:

```dockerfile
LABEL maintainer="team@example.com"
LABEL version="1.0"
```

Or during build:

```bash
docker build \
  --label version=1.0 \
  -t myapp:v1 .
```

Inspect:

```bash
docker image inspect myapp:v1
```

---

# 58. Image Metadata

Inspect:

```bash
docker image inspect myapp:v1
```

Important fields include:

```text
Id
RepoTags
RepoDigests
Architecture
Os
Config
RootFS
Created
```

This is useful for debugging and automation.

---

# 59. Image Architecture

Docker images can target different CPU architectures.

Common architectures:

```text
amd64
arm64
arm/v7
```

For example:

```text
Mac Apple Silicon → arm64
Most Intel/AMD servers → amd64
```

This becomes important when building images on one architecture and deploying to another.

---

# 60. Multi-Architecture Images

Modern Docker supports multi-platform builds.

Example:

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t myusername/myapp:v1 \
  --push .
```

Now the registry can contain variants for:

```text
linux/amd64
linux/arm64
```

When someone runs:

```bash
docker pull myusername/myapp:v1
```

Docker can select the appropriate platform image.

---

# 61. Docker Buildx

`buildx` provides advanced build functionality.

Check:

```bash
docker buildx version
```

List builders:

```bash
docker buildx ls
```

Create builder:

```bash
docker buildx create --name mybuilder --use
```

Inspect:

```bash
docker buildx inspect
```

Build:

```bash
docker buildx build -t myapp:v1 .
```

---

# 62. Multi-Stage Builds

One of the most important advanced image techniques.

Instead of putting build tools into your production image:

```text
Build environment
      ↓
Compile
      ↓
Production artifact
      ↓
Small runtime image
```

Example:

```dockerfile
FROM node:22 AS builder

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

RUN npm run build


FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
```

Benefits:

* smaller image
* fewer dependencies
* lower attack surface
* faster deployment

---

# 63. Image Cache

Docker caches image build steps.

Example:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

If only application code changes:

```text
FROM        → cached
WORKDIR     → cached
COPY req    → cached
RUN pip     → cached
COPY app    → rebuilt
```

This makes builds significantly faster.

---

# 64. Good Dockerfile Ordering

Bad:

```dockerfile
COPY . .

RUN pip install -r requirements.txt
```

Better:

```dockerfile
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
```

Why?

Because changing source code won't invalidate the dependency installation layer.

---

# 65. Image Security Scanning

Images should be scanned for vulnerabilities.

Docker provides:

```bash
docker scout
```

For example:

```bash
docker scout cves myapp:v1
```

You can also use external scanners such as:

* Trivy
* Grype
* Snyk
* Clair

Typical CI/CD flow:

```text
Source Code
    ↓
Build Image
    ↓
Security Scan
    ↓
Tests
    ↓
Push Registry
    ↓
Deploy
```

---

# 66. Docker Scout

If available in your Docker installation:

```bash
docker scout quickview myapp:v1
```

View vulnerabilities:

```bash
docker scout cves myapp:v1
```

Recommendations:

```bash
docker scout recommendations myapp:v1
```

This helps identify vulnerable dependencies and potential base-image improvements.

---

# 67. Image Provenance

Modern container supply chains increasingly care about:

```text
Who built the image?
What source produced it?
What dependencies were used?
Can we verify its origin?
```

Advanced Docker BuildKit/buildx workflows can generate provenance and SBOM-related attestations.

Example:

```bash
docker buildx build \
  --provenance=true \
  --sbom=true \
  -t myapp:v1 \
  --push .
```

This is particularly relevant for production CI/CD and software supply-chain security.

---

# 68. SBOM

SBOM means:

> **Software Bill of Materials**

It describes components contained in software.

Conceptually:

```text
Docker Image
     ↓
SBOM
     ↓
Python
OpenSSL
glibc
Flask
Requests
...
```

SBOMs help organizations identify:

* vulnerable dependencies
* outdated packages
* licensing concerns
* supply-chain risks

---

# 69. Image Digests in CI/CD

Instead of deploying:

```text
myapp:latest
```

you can deploy a specific immutable digest:

```text
myapp@sha256:abcdef...
```

This provides stronger reproducibility.

Example:

```text
Build
 ↓
Push
 ↓
Digest
 ↓
Deploy exact image
```

This avoids the ambiguity of mutable tags.

---

# 70. Registry Image Lifecycle

A typical professional workflow:

```text
Developer
    │
    ▼
Dockerfile
    │
    ▼
docker build
    │
    ▼
Docker Image
    │
    ├── Test
    ├── Scan
    └── Tag
          │
          ▼
    Container Registry
          │
          ▼
       Production
```

---

# 71. Useful Image Commands — Cheat Sheet

### List images

```bash
docker images
```

```bash
docker image ls
```

### Pull

```bash
docker pull nginx
```

### Build

```bash
docker build -t myapp:v1 .
```

### Run

```bash
docker run myapp:v1
```

### Inspect

```bash
docker image inspect myapp:v1
```

### History

```bash
docker history myapp:v1
```

### Tag

```bash
docker tag myapp:v1 username/myapp:v1
```

### Push

```bash
docker push username/myapp:v1
```

### Remove

```bash
docker rmi myapp:v1
```

### Prune

```bash
docker image prune
```

### Save

```bash
docker save myapp:v1 -o myapp.tar
```

### Load

```bash
docker load -i myapp.tar
```

### Search

```bash
docker search nginx
```

### List IDs

```bash
docker images -q
```

### Image history

```bash
docker history --no-trunc myapp:v1
```

---

# 72. Important Docker Image Command Categories

You can organize image commands into six groups.

### A. Discover

```bash
docker images
docker search
docker image ls
```

### B. Download

```bash
docker pull
```

### C. Build

```bash
docker build
docker buildx build
```

### D. Inspect

```bash
docker image inspect
docker history
```

### E. Distribute

```bash
docker tag
docker login
docker push
docker save
docker load
```

### F. Clean

```bash
docker rmi
docker image prune
```

---

# 73. Complete Image Lifecycle

Understand this flow very well:

```text
                  Dockerfile
                      │
                      ▼
                docker build
                      │
                      ▼
               Docker Image
                      │
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
       inspect      tag         scan
          │           │
          │           ▼
          │       docker push
          │           │
          │           ▼
          │      Registry
          │           │
          │           ▼
          │       docker pull
          │           │
          └───────────┤
                      ▼
                docker run
                      │
                      ▼
                 Container
```

---

# 74. Image vs Container vs Registry

This is a common interview question.

```text
Registry
   │
   │ pull
   ▼
Image
   │
   │ run
   ▼
Container
```

### Registry

Stores and distributes images.

Examples:

```text
Docker Hub
Amazon ECR
GitHub Container Registry
Google Artifact Registry
Azure Container Registry
```

### Image

Immutable package/template used to create containers.

### Container

Running instance of an image.

---

# 75. Most Important Commands to Memorize

For interviews and daily Docker work, prioritize these:

```bash
docker pull
docker images
docker image ls
docker build
docker run
docker image inspect
docker history
docker tag
docker push
docker rmi
docker image prune
docker save
docker load
docker search
docker buildx build
```

And understand these concepts:

```text
Image
Container
Registry
Repository
Tag
Digest
Layer
Dockerfile
Build Context
Build Cache
Multi-stage Build
Multi-platform Build
Image Security
SBOM
Image Provenance
```

---

# 76. Recommended Learning Order

Since you're learning Docker from a DevOps perspective, learn image handling in this sequence:

```text
1. What is Docker Image
       ↓
2. Image vs Container
       ↓
3. Image Layers
       ↓
4. Image Tags
       ↓
5. docker pull
       ↓
6. docker images
       ↓
7. docker run
       ↓
8. docker inspect
       ↓
9. docker history
       ↓
10. Dockerfile
       ↓
11. docker build
       ↓
12. .dockerignore
       ↓
13. Image Tagging
       ↓
14. docker login
       ↓
15. docker push
       ↓
16. Docker Registry
       ↓
17. docker save / load
       ↓
18. Image Cleanup
       ↓
19. Build Cache
       ↓
20. Multi-stage Builds
       ↓
21. Buildx
       ↓
22. Multi-platform Images
       ↓
23. Image Security
       ↓
24. SBOM
       ↓
25. Provenance
       ↓
26. Immutable Digests
       ↓
27. CI/CD Image Pipeline
```

## Interview-Level Mental Model

Remember this one diagram:

```text
                  Dockerfile
                      │
                  docker build
                      │
                      ▼
               ┌──────────────┐
               │ Docker Image │
               └──────────────┘
                 │     │     │
            inspect   tag   scan
                 │     │
                 │     ▼
                 │   push
                 │     │
                 │     ▼
                 │  Registry
                 │     │
                 │    pull
                 │     │
                 ▼     ▼
              Image ────────┐
                             │
                         docker run
                             │
                             ▼
                      ┌────────────┐
                      │ Container  │
                      └────────────┘
```

**Core idea:** A **Dockerfile builds an Image, a Registry stores/distributes the Image, and `docker run` creates a Container from the Image.**
