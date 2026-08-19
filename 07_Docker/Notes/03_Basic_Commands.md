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

---
# `Notes 2`
# Main Docker Commands

These commands form the basic Docker workflow:

```text
Docker Registry
      │
      │ docker pull
      ↓
Docker Image
      │
      │ docker run
      ↓
Docker Container
      │
      ├── docker ps
      ├── docker stop
      └── docker start
```

We'll use **Nginx** as the example because it makes container and port concepts easy to understand.

---

# 1. `docker pull`

## What is `docker pull`?

`docker pull` downloads a **Docker image from a container registry** to your local machine.

Syntax:

```bash
docker pull IMAGE_NAME
```

Example:

```bash
docker pull nginx
```

Docker looks for the image in the default registry, usually **Docker Hub**.

Conceptually:

```text
Docker Hub
    │
    │ docker pull nginx
    ↓
Your Computer
    │
    └── nginx image
```

Check downloaded images:

```bash
docker images
```

You may see:

```text
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    abc123...      ...           ...
```

### Image tag

You can specify a particular version:

```bash
docker pull nginx:1.27
```

If you don't specify a tag:

```bash
docker pull nginx
```

Docker uses:

```text
nginx:latest
```

So:

```text
nginx
   ↓
nginx:latest
```

### Important

`docker pull` **only downloads the image**.

It does **not** start a container.

```bash
docker pull nginx
```

means:

> "Download the nginx image."

It does not mean:

> "Run nginx."

---

# 2. `docker run`

## What is `docker run`?

`docker run` creates a **new container from an image and starts it**.

Syntax:

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
     │
     │ docker run
     ↓
New Container
     │
     ↓
Running Nginx
```

### What actually happens?

When you run:

```bash
docker run nginx
```

Docker roughly performs:

```text
1. Check whether nginx image exists locally
             ↓
2. If not, pull the image
             ↓
3. Create a container
             ↓
4. Configure the container
             ↓
5. Start the container
```

Therefore:

```bash
docker run nginx
```

can effectively perform a pull automatically if the image isn't already present.

---

# 3. `docker run` vs `docker pull`

This distinction is important.

### `docker pull`

```bash
docker pull nginx
```

Only downloads:

```text
Registry → Local Image
```

### `docker run`

```bash
docker run nginx
```

Creates and starts:

```text
Image → Container → Running Application
```

---

# 4. Running a Container in Background

By default:

```bash
docker run nginx
```

runs the container attached to your terminal.

For server applications, you usually want **detached mode**:

```bash
docker run -d nginx
```

`-d` means:

> **Detached mode**

Now your terminal is immediately available again.

Check the container:

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE   STATUS          PORTS
a1b2c3d4       nginx   Up 10 seconds
```

---

# 5. Give the Container a Name

Instead of allowing Docker to generate a random container name:

```bash
docker run -d nginx
```

you can specify one:

```bash
docker run -d --name my-nginx nginx
```

Now:

```bash
docker ps
```

might show:

```text
CONTAINER ID   IMAGE   STATUS        NAMES
a1b2c3d4       nginx   Up 10 sec     my-nginx
```

This makes container management much easier.

---

# 6. `docker ps`

## What is `docker ps`?

`docker ps` displays **currently running containers**.

```bash
docker ps
```

Example:

```text
CONTAINER ID   IMAGE   COMMAND                  STATUS         PORTS   NAMES
a12bc34def56   nginx   "/docker-entrypoint…"   Up 2 minutes           my-nginx
```

Important columns:

| Column       | Meaning                               |
| ------------ | ------------------------------------- |
| CONTAINER ID | Unique container identifier           |
| IMAGE        | Image used to create container        |
| COMMAND      | Main command running inside container |
| STATUS       | Current container state               |
| PORTS        | Port mappings                         |
| NAMES        | Container name                        |

---

# 7. `docker ps -a`

By default:

```bash
docker ps
```

shows **only running containers**.

To see:

* Running containers
* Stopped containers
* Exited containers

use:

```bash
docker ps -a
```

Example:

```text
CONTAINER ID   IMAGE   STATUS                     NAMES
a123           nginx   Up 5 minutes               my-nginx
b456           nginx   Exited (0) 2 hours ago     old-nginx
c789           redis   Exited (0) 1 day ago       redis-test
```

Remember:

```text
docker ps
    ↓
Running containers only

docker ps -a
    ↓
All containers
```

---

# 8. `docker stop`

## What is `docker stop`?

`docker stop` gracefully stops a **running container**.

Syntax:

```bash
docker stop CONTAINER
```

Example:

```bash
docker stop my-nginx
```

Or using the container ID:

```bash
docker stop a12bc34def56
```

Conceptually:

```text
Running Container
       │
       │ docker stop
       ↓
Stopped Container
```

### Important

`docker stop` does **not delete the container**.

After:

```bash
docker stop my-nginx
```

the container still exists.

Check:

```bash
docker ps -a
```

You'll see something like:

```text
my-nginx   Exited (0)
```

---

# 9. `docker start`

## What is `docker start`?

`docker start` starts an **existing stopped container**.

Example:

```bash
docker start my-nginx
```

Conceptually:

```text
Stopped Container
       │
       │ docker start
       ↓
Running Container
```

### Important distinction

`docker start` does **not create a new container**.

It starts an existing one.

---

# 10. `docker run` vs `docker start`

This is one of the most important interview questions.

### `docker run`

Creates a **new container**.

```bash
docker run -d --name my-nginx nginx
```

```text
Image
  ↓
NEW Container
  ↓
Running
```

### `docker start`

Starts an **existing container**.

```bash
docker start my-nginx
```

```text
Existing Container
       ↓
    Running
```

Therefore:

```text
docker run
    ↓
CREATE + START

docker start
    ↓
START existing container
```

---

# 11. Container Lifecycle

You can visualize the commands like this:

```text
                 Docker Image
                      │
                      │ docker run
                      ↓
              ┌───────────────┐
              │   Container   │
              │    Running    │
              └───────┬───────┘
                      │
                docker stop
                      ↓
              ┌───────────────┐
              │   Container   │
              │    Stopped    │
              └───────┬───────┘
                      │
                docker start
                      ↓
              ┌───────────────┐
              │   Container   │
              │    Running    │
              └───────────────┘
```

---

# 12. Port Mapping

This is one of the most important Docker concepts.

Suppose Nginx is running inside a container.

Nginx listens on:

```text
Container Port: 80
```

But your browser is outside the container.

You need a way to access:

```text
Your Computer → Container
```

That's where **port mapping** comes in.

---

# 13. The `-p` Option

Docker uses:

```bash
-p HOST_PORT:CONTAINER_PORT
```

Example:

```bash
docker run -d -p 8080:80 nginx
```

This means:

```text
Host Port       Container Port
    8080   →        80
```

So:

```text
Browser
   │
   │ http://localhost:8080
   ↓
Host Machine
   │
   │ Port 8080
   ↓
Docker
   │
   │ Port 80
   ↓
Nginx Container
   │
   │ Port 80
   ↓
Nginx
```

Open:

```text
http://localhost:8080
```

You should get the Nginx welcome page.

---

# 14. Why Do We Need Port Mapping?

Containers have their own network namespace.

Suppose Nginx listens on:

```text
Container
    ↓
Port 80
```

That does not automatically mean you can access it using:

```text
localhost:80
```

on your host machine.

You explicitly publish the port:

```bash
docker run -d -p 8080:80 nginx
```

Now:

```text
Host                 Container

8080  ─────────────→ 80
```

---

# 15. Host Port vs Container Port

This is frequently confusing.

In:

```bash
docker run -d -p 8080:80 nginx
```

the order is:

```text
-p HOST_PORT:CONTAINER_PORT
```

Therefore:

```text
8080 = Host port
80   = Container port
```

### Memory trick

Read it from left to right:

```text
-p

MY COMPUTER : CONTAINER
     ↓           ↓
   8080    :     80
```

---

# 16. Change the Host Port

The container's application may listen on port 80.

You can expose it through any available host port.

For example:

```bash
docker run -d -p 3000:80 nginx
```

Now:

```text
localhost:3000
       ↓
Container:80
```

Or:

```bash
docker run -d -p 8080:80 nginx
```

```text
localhost:8080
       ↓
Container:80
```

Or:

```bash
docker run -d -p 5000:80 nginx
```

```text
localhost:5000
       ↓
Container:80
```

The Nginx container still listens on:

```text
80
```

Only the host-side published port changes.

---

# 17. Multiple Containers

This becomes useful when running multiple services.

Suppose:

```text
Frontend Container
    Container Port: 3000

Backend Container
    Container Port: 5000

Nginx Container
    Container Port: 80
```

You could map them:

```text
Host               Container
────────────────────────────────
localhost:3000  →  Frontend:3000
localhost:5000  →  Backend:5000
localhost:8080  →  Nginx:80
```

Commands:

```bash
docker run -d -p 3000:3000 frontend
```

```bash
docker run -d -p 5000:5000 backend
```

```bash
docker run -d -p 8080:80 nginx
```

---

# 18. Complete Practical Example

Let's build the entire flow.

### Step 1 — Download Nginx

```bash
docker pull nginx
```

### Step 2 — Check image

```bash
docker images
```

### Step 3 — Create and run container

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```

Now:

```text
Docker Image
    │
    │ docker run
    ↓
my-nginx Container
    │
    │ Port 80
    ↓
Nginx
```

### Step 4 — Check container

```bash
docker ps
```

### Step 5 — Open browser

```text
http://localhost:8080
```

### Step 6 — Stop container

```bash
docker stop my-nginx
```

### Step 7 — Verify

```bash
docker ps
```

It won't appear because it is stopped.

But:

```bash
docker ps -a
```

will show it.

### Step 8 — Start it again

```bash
docker start my-nginx
```

### Step 9 — Check

```bash
docker ps
```

### Step 10 — Open browser again

```text
http://localhost:8080
```

Nginx is running again.

---

# 19. Important Command Cheat Sheet

| Command                       | Purpose                           |
| ----------------------------- | --------------------------------- |
| `docker pull nginx`           | Download image                    |
| `docker images`               | List images                       |
| `docker run nginx`            | Create + start container          |
| `docker run -d nginx`         | Run in background                 |
| `docker run --name app nginx` | Give container a name             |
| `docker run -p 8080:80 nginx` | Map host port 8080 → container 80 |
| `docker ps`                   | Show running containers           |
| `docker ps -a`                | Show all containers               |
| `docker stop app`             | Stop container                    |
| `docker start app`            | Start existing container          |

---

# 20. The Most Important Mental Model

Memorize this:

```text
                 REGISTRY
                    │
              docker pull
                    ↓
                 IMAGE
                    │
              docker run
                    ↓
               CONTAINER
                    │
          ┌─────────┴─────────┐
          │                   │
     docker stop         docker ps
          │
          ↓
       STOPPED
          │
      docker start
          │
          ↓
       RUNNING
```

And for networking:

```text
Browser
   │
   │ localhost:8080
   ↓
HOST PORT 8080
   │
   │ -p 8080:80
   ↓
CONTAINER PORT 80
   │
   ↓
Nginx
```

### Three distinctions you should be able to explain in an interview

**`docker pull`**

> Downloads an image from a registry.

**`docker run`**

> Creates a new container from an image and starts it.

**`docker start`**

> Starts an existing stopped container.

And:

> **Port mapping connects a port on the host machine to a port exposed/listened to by an application inside the container.**
