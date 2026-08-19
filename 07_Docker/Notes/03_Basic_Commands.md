# Main Docker Commands

Before learning individual commands, keep this basic Docker flow in mind:

```text
Docker Image
    ↓
docker pull
    ↓
Image stored locally
    ↓
docker run
    ↓
Container created + started
    ↓
docker ps
    ↓
See running container
    ↓
docker stop
    ↓
Container stopped
    ↓
docker start
    ↓
Container started again
```

---

## 1. `docker pull`

### What is it?

`docker pull` downloads a **Docker image** from a container registry to your local machine.

By default, Docker uses **Docker Hub** as the registry.

### Syntax

```bash
docker pull IMAGE_NAME
```

### Example

```bash
docker pull nginx
```

This downloads the `nginx` image.

You can also specify a version/tag:

```bash
docker pull nginx:latest
```

```bash
docker pull nginx:1.27
```

### What happens?

```text
Docker Hub
    │
    │ docker pull nginx
    ↓
Your Computer
    │
    └── nginx image
```

You can check downloaded images using:

```bash
docker images
```

Example:

```text
REPOSITORY   TAG       IMAGE ID       SIZE
nginx        latest    abc123         188MB
```

### Important

`docker pull` **does not create or start a container**.

It only downloads the image.

---

# 2. `docker run`

### What is it?

`docker run` creates a **new container from an image** and starts it.

### Syntax

```bash
docker run IMAGE_NAME
```

Example:

```bash
docker run nginx
```

Conceptually:

```text
nginx Image
     ↓
docker run nginx
     ↓
New Container
     ↓
Container starts
```

### Important distinction

```text
Image      → Template
Container  → Running instance of that template
```

For example:

```bash
docker pull nginx
```

downloads the image.

Then:

```bash
docker run nginx
```

creates a container using that image.

---

## `docker run` automatically pulls the image

You don't always need to manually run `docker pull`.

For example:

```bash
docker run nginx
```

If `nginx` doesn't exist locally, Docker will normally pull it automatically.

So:

```bash
docker pull nginx
docker run nginx
```

and, when the image isn't already local:

```bash
docker run nginx
```

can accomplish both steps.

---

# 3. `docker ps`

### What is it?

`docker ps` shows **currently running containers**.

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE   COMMAND                  STATUS        PORTS
a1b2c3d4       nginx   "/docker-entrypoint..."  Up 2 minutes  80/tcp
```

Important information includes:

| Column       | Meaning                          |
| ------------ | -------------------------------- |
| CONTAINER ID | Unique container identifier      |
| IMAGE        | Image used by container          |
| COMMAND      | Command running inside container |
| STATUS       | Container status                 |
| PORTS        | Port information                 |
| NAMES        | Container name                   |

---

## Show all containers

By default:

```bash
docker ps
```

only shows **running** containers.

To see both running and stopped containers:

```bash
docker ps -a
```

For example:

```text
CONTAINER ID   IMAGE   STATUS
a1b2c3d4       nginx   Up 5 minutes
e5f6g7h8       nginx   Exited
```

This distinction is important:

```bash
docker ps
```

→ Running containers

```bash
docker ps -a
```

→ All containers

---

# 4. `docker stop`

### What is it?

`docker stop` gracefully stops a running container.

### Syntax

```bash
docker stop CONTAINER_ID
```

or:

```bash
docker stop CONTAINER_NAME
```

Example:

```bash
docker stop my-nginx
```

If your container ID is:

```text
a1b2c3d4
```

you can use:

```bash
docker stop a1b2c3d4
```

After stopping:

```bash
docker ps
```

will no longer show that container.

But:

```bash
docker ps -a
```

will still show it.

### Important

`docker stop` **does not delete the container**.

It simply changes:

```text
Running
   ↓
Stopped
```

The container still exists.

---

# 5. `docker start`

### What is it?

`docker start` starts an **existing stopped container**.

### Syntax

```bash
docker start CONTAINER_NAME
```

Example:

```bash
docker start my-nginx
```

or:

```bash
docker start a1b2c3d4
```

Flow:

```text
Running Container
       ↓
 docker stop
       ↓
Stopped Container
       ↓
 docker start
       ↓
Running Container
```

### Very important difference

`docker run` and `docker start` are **not the same**.

### `docker run`

Creates a **new container**.

```bash
docker run nginx
```

### `docker start`

Starts an **existing container**.

```bash
docker start my-nginx
```

Think:

```text
docker run
    ↓
CREATE + START

docker start
    ↓
START EXISTING
```

---

# 6. Port Mapping

This is one of the most important Docker concepts.

Suppose you run an Nginx container:

```bash
docker run nginx
```

Nginx listens on port `80` **inside the container**.

But your browser runs on your host machine.

You need a way to connect:

```text
Your Browser
     ↓
Host Machine
     ↓
Docker Container
     ↓
Nginx :80
```

This is done using **port mapping**.

---

## `-p` option

The syntax is:

```bash
docker run -p HOST_PORT:CONTAINER_PORT IMAGE
```

Example:

```bash
docker run -p 8080:80 nginx
```

This means:

```text
Host Port       Container Port
   8080    →         80
```

So:

```text
Browser
   │
   │ http://localhost:8080
   ↓
Host :8080
   │
   │ Docker port mapping
   ↓
Container :80
   │
   ↓
Nginx
```

Now open:

```text
http://localhost:8080
```

and you should see the Nginx welcome page.

---

# Why do we use different ports?

You don't have to use `8080`.

You could use:

```bash
docker run -p 3000:80 nginx
```

Then:

```text
localhost:3000
       ↓
container:80
```

Or:

```bash
docker run -p 5000:80 nginx
```

Then:

```text
localhost:5000
       ↓
container:80
```

The general pattern is:

```text
-p HOST_PORT:CONTAINER_PORT
```

For example:

```bash
-p 8080:80
```

means:

> "Expose my machine's port 8080 and forward traffic to port 80 inside the container."

---

# A Complete Example

Let's run Nginx properly.

### Step 1: Pull image

```bash
docker pull nginx
```

### Step 2: Run container

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

Here:

| Option            | Meaning                         |
| ----------------- | ------------------------------- |
| `docker run`      | Create and start container      |
| `-d`              | Run in detached/background mode |
| `-p 8080:80`      | Map host 8080 → container 80    |
| `--name my-nginx` | Give container a name           |
| `nginx`           | Image to use                    |

---

### Step 3: Check container

```bash
docker ps
```

You should see something similar to:

```text
CONTAINER ID   IMAGE   STATUS       PORTS
abc123         nginx   Up 10 sec    0.0.0.0:8080->80/tcp
```

The important part is:

```text
8080 -> 80
```

---

### Step 4: Open browser

Go to:

```text
http://localhost:8080
```

Request flow:

```text
Browser
   │
   │ localhost:8080
   ↓
Host Machine
   │
   │ Port 8080
   ↓
Docker
   │
   │ Port mapping
   ↓
Container
   │
   │ Port 80
   ↓
Nginx
```

---

### Step 5: Stop container

```bash
docker stop my-nginx
```

Check:

```bash
docker ps
```

It won't appear because it's stopped.

Check all containers:

```bash
docker ps -a
```

You will see:

```text
my-nginx    Exited
```

---

### Step 6: Start it again

```bash
docker start my-nginx
```

Then:

```bash
docker ps
```

It should be running again.

You can access:

```text
http://localhost:8080
```

again.

---

# Commands You Should Memorize

```bash
# Download image
docker pull nginx

# List images
docker images

# Create and start container
docker run nginx

# Run in background
docker run -d nginx

# Give container a name
docker run -d --name my-nginx nginx

# Port mapping
docker run -d -p 8080:80 --name my-nginx nginx

# Show running containers
docker ps

# Show all containers
docker ps -a

# Stop container
docker stop my-nginx

# Start existing container
docker start my-nginx
```

## The most important mental model

```text
                 DOCKER HUB
                     │
                     │ docker pull
                     ↓
                ┌───────────┐
                │   IMAGE   │
                │   nginx   │
                └─────┬─────┘
                      │
                 docker run
                      ↓
                ┌───────────┐
                │ CONTAINER │
                │   nginx   │
                │    :80    │
                └─────┬─────┘
                      │
                -p 8080:80
                      │
                      ↓
              HOST MACHINE :8080
                      │
                      ↓
                  BROWSER
```

**Key rule:** `pull` gets an **image**, `run` creates a **new container**, `ps` views containers, `stop` stops a container, `start` restarts an existing container, and `-p` connects a **host port to a container port**.
