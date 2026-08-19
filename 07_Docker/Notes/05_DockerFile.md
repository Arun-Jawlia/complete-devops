# Dockerfile — Building Our Own Docker Image

So far, you have used existing images:

```bash
docker pull nginx
docker run nginx
```

But in real projects, you usually have **your own application**.

For example:

```text
my-python-app
my-node-app
my-flask-api
my-fastapi-api
my-react-app
```

You need to package your application into your own Docker image.

The process is:

```text
Application
     ↓
Dockerfile
     ↓
docker build
     ↓
Docker Image
     ↓
docker run
     ↓
Container
     ↓
Application
```

---

# 1. What is a Dockerfile?

A **Dockerfile is a text file containing instructions that Docker uses to build a Docker image.**

It tells Docker things like:

* Which base image to use
* Where the application should live
* Which dependencies to install
* Which files to copy
* Which ports the application uses
* Which command should run when the container starts

Think of it as a **recipe for creating a Docker image**.

### Analogy

```text
Recipe
  ↓
Ingredients
  ↓
Cooking instructions
  ↓
Food
```

Docker:

```text
Dockerfile
  ↓
Base image + Application + Dependencies
  ↓
docker build
  ↓
Docker Image
```

---

# 2. Dockerfile vs Docker Image vs Container

These three concepts must be clear.

```text
Dockerfile
    │
    │ docker build
    ↓
Docker Image
    │
    │ docker run
    ↓
Docker Container
```

### Dockerfile

Instructions:

```text
"Install Python"
"Copy my code"
"Install dependencies"
"Run app.py"
```

### Image

The packaged result:

```text
Python
Flask
Dependencies
Application
Configuration
```

### Container

The running instance:

```text
Running Flask Application
```

---

# 3. Why Do We Need Dockerfile?

Suppose you have a Python application:

```text
my-app/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

Your application requires:

```text
Python 3.12
Flask
Requests
```

Without Docker, another developer would need to manually do:

```bash
python install
pip install flask
pip install requests
```

With Dockerfile, we define everything once:

```text
Dockerfile
    ↓
docker build
    ↓
Image
    ↓
Anyone can run it
```

This gives us a **reproducible build**.

---

# 4. Creating Our First Dockerfile

Let's create a simple Python application.

## Project structure

```text
docker-python-app/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

---

# 5. Create `app.py`

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Docker!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

There is one important line here:

```python
app.run(host="0.0.0.0", port=5000)
```

Why `0.0.0.0`?

Because the Flask server needs to listen on the container's network interface so it can be reached through Docker's port publishing.

---

# 6. Create `requirements.txt`

```text
Flask
```

You could specify a version:

```text
Flask==3.1.2
```

Pinning versions is generally preferable for reproducible builds.

---

# 7. Create the Dockerfile

Create a file named exactly:

```text
Dockerfile
```

No extension.

Correct:

```text
Dockerfile
```

Not:

```text
Dockerfile.txt
```

Now add:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

Now let's understand every instruction.

---

# 8. `FROM`

```dockerfile
FROM python:3.12
```

`FROM` specifies the **base image**.

We're saying:

> Start my image with Python 3.12.

Docker will get:

```text
python:3.12
```

from the configured registry if it isn't already available locally.

Conceptually:

```text
Python 3.12 Image
       ↓
Our Docker Image
```

You can also use:

```dockerfile
FROM node:22
```

for Node.js.

Or:

```dockerfile
FROM ubuntu:24.04
```

for Ubuntu.

Or:

```dockerfile
FROM nginx:latest
```

for Nginx.

### `FROM` is usually the first instruction

```dockerfile
FROM python:3.12
```

---

# 9. `WORKDIR`

```dockerfile
WORKDIR /app
```

This sets the working directory inside the image/container.

Think:

```text
Container
└── /app
```

After this instruction, subsequent commands operate relative to:

```text
/app
```

For example:

```dockerfile
COPY . .
```

means:

```text
Current directory → /app
```

You don't generally need:

```dockerfile
RUN cd /app
```

because `WORKDIR` handles this.

---

# 10. `COPY`

```dockerfile
COPY requirements.txt .
```

This copies a file from your **build context** into the image.

Our local project:

```text
docker-python-app/
│
├── requirements.txt
├── app.py
└── Dockerfile
```

After:

```dockerfile
COPY requirements.txt .
```

inside the image:

```text
/app/
└── requirements.txt
```

Then:

```dockerfile
COPY . .
```

copies the application files into `/app`.

Result:

```text
/app/
│
├── app.py
├── requirements.txt
└── ...
```

---

# 11. `RUN`

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

`RUN` executes a command **during image building**.

Here Docker executes:

```bash
pip install --no-cache-dir -r requirements.txt
```

So Flask gets installed into the image.

Important distinction:

```text
RUN
 ↓
Build time
```

while:

```text
CMD
 ↓
Container startup
```

---

# 12. `EXPOSE`

```dockerfile
EXPOSE 5000
```

This documents that the application is intended to listen on port `5000`.

It does **not** publish the port to your host machine.

This is a very common misunderstanding.

This:

```dockerfile
EXPOSE 5000
```

does **not** mean you can automatically access:

```text
localhost:5000
```

You still need:

```bash
docker run -p 5000:5000 ...
```

---

# 13. `CMD`

```dockerfile
CMD ["python", "app.py"]
```

`CMD` specifies the default command that runs when a container is started from the image.

So:

```text
docker run my-python-app
           ↓
CMD
           ↓
python app.py
           ↓
Flask starts
```

---

# 14. Complete Dockerfile

Our complete Dockerfile:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

The flow is:

```text
FROM
 ↓
Python 3.12

WORKDIR
 ↓
/app

COPY requirements.txt
 ↓
requirements.txt

RUN pip install
 ↓
Flask installed

COPY . .
 ↓
Application copied

EXPOSE 5000
 ↓
Document application port

CMD
 ↓
python app.py
```

---

# 15. Build the Docker Image

Now we have:

```text
docker-python-app/
│
├── app.py
├── requirements.txt
└── Dockerfile
```

Open your terminal in this directory.

Run:

```bash
docker build -t my-python-app .
```

This is one of the most important Docker commands.

---

# 16. Understand `docker build`

The command:

```bash
docker build -t my-python-app .
```

has three important parts.

### `docker build`

Tell Docker:

> Build an image.

### `-t my-python-app`

`-t` means **tag**.

We're naming the image:

```text
my-python-app
```

### `.`

The dot means:

> Use the current directory as the build context.

Therefore:

```text
docker build -t my-python-app .
             │       │
             │       └── Build context
             │
             └── Image name
```

---

# 17. What Happens During `docker build`?

When you execute:

```bash
docker build -t my-python-app .
```

Docker reads:

```text
Dockerfile
```

and processes the instructions.

Conceptually:

```text
Dockerfile
    │
    ↓
FROM python:3.12
    │
    ↓
WORKDIR /app
    │
    ↓
COPY requirements.txt .
    │
    ↓
RUN pip install ...
    │
    ↓
COPY . .
    │
    ↓
EXPOSE 5000
    │
    ↓
CMD ...
    │
    ↓
Docker Image
```

---

# 18. Check Your Image

After building:

```bash
docker images
```

You should see something similar to:

```text
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
my-python-app    latest    abc123def456   10 seconds ago   1xxMB
```

You can also use:

```bash
docker image ls
```

---

# 19. Run Your Own Image

Now that we've created:

```text
my-python-app
```

run it:

```bash
docker run -d --name my-python-container -p 5000:5000 my-python-app
```

Break it down:

```text
docker run
    ↓
Create + start container

-d
    ↓
Detached/background mode

--name my-python-container
    ↓
Container name

-p 5000:5000
    ↓
Host port → Container port

my-python-app
    ↓
Image
```

---

# 20. Access the Application

Open:

```text
http://localhost:5000
```

Request flow:

```text
Browser
   │
   │ localhost:5000
   ↓
Host Machine
   │
   │ Port 5000
   ↓
Docker
   │
   │ Port 5000
   ↓
Container
   │
   ↓
Flask
   │
   ↓
app.py
```

You should see:

```text
Hello from Docker!
```

---

# 21. Check the Running Container

Run:

```bash
docker ps
```

You should see:

```text
CONTAINER ID   IMAGE           STATUS        PORTS
abc123         my-python-app   Up 1 minute   0.0.0.0:5000->5000/tcp
```

The important part:

```text
0.0.0.0:5000->5000/tcp
```

means:

```text
Host:5000
     ↓
Container:5000
```

---

# 22. View Container Logs

If the application doesn't work:

```bash
docker logs my-python-container
```

This is extremely useful for debugging.

You might see:

```text
 * Running on http://0.0.0.0:5000
```

---

# 23. Stop the Container

```bash
docker stop my-python-container
```

Check:

```bash
docker ps
```

It won't appear because it has stopped.

But:

```bash
docker ps -a
```

will show it.

---

# 24. Start It Again

Because the container already exists:

```bash
docker start my-python-container
```

You don't need to build the image again.

You don't need:

```bash
docker run my-python-app
```

because that would create a **new container**.

Remember:

```text
Image
  │
  ├── docker run → Container 1
  │
  ├── docker run → Container 2
  │
  └── docker run → Container 3
```

---

# 25. Dockerfile Build vs Container Run

This distinction is fundamental.

### Build

```bash
docker build -t my-python-app .
```

Creates:

```text
Dockerfile
    ↓
Image
```

### Run

```bash
docker run my-python-app
```

Creates:

```text
Image
    ↓
Container
```

So:

```text
                 Dockerfile
                     │
                docker build
                     ↓
                   Image
                     │
                 docker run
                     ↓
                 Container
                     │
                     ↓
                Running App
```

---

# 26. Why `COPY requirements.txt` Before `COPY . .`?

You may wonder why we didn't simply write:

```dockerfile
COPY . .
RUN pip install -r requirements.txt
```

Instead, we used:

```dockerfile
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
```

This is related to **Docker layer caching**.

Docker builds images in layers.

Conceptually:

```text
Layer 1 → FROM python:3.12
Layer 2 → WORKDIR /app
Layer 3 → COPY requirements.txt
Layer 4 → RUN pip install
Layer 5 → COPY application
```

If you change only:

```text
app.py
```

Docker can often reuse the earlier dependency-installation layers.

Therefore it doesn't need to reinstall all Python dependencies every time.

This can make builds significantly faster.

---

# 27. `.dockerignore`

You should normally create:

```text
.dockerignore
```

For our Python application:

```text
__pycache__
*.pyc
.venv
venv
.git
.env
.pytest_cache
```

Why?

Because:

```bash
COPY . .
```

would otherwise potentially copy unnecessary files into the build context/image.

For example, you generally don't want:

```text
.git/
.venv/
__pycache__/
.env
```

inside your image.

**Especially important:** don't accidentally copy secrets such as `.env` files containing credentials.

---

# 28. Final Project Structure

A clean version:

```text
docker-python-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

### Dockerfile

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### Build

```bash
docker build -t my-python-app .
```

### Check image

```bash
docker images
```

### Run

```bash
docker run -d \
  --name my-python-container \
  -p 5000:5000 \
  my-python-app
```

### Check container

```bash
docker ps
```

### Logs

```bash
docker logs my-python-container
```

### Stop

```bash
docker stop my-python-container
```

### Start

```bash
docker start my-python-container
```

---

# 29. Dockerfile Instructions You Should Learn First

| Instruction  | Purpose                                                                         |
| ------------ | ------------------------------------------------------------------------------- |
| `FROM`       | Select base image                                                               |
| `WORKDIR`    | Set working directory                                                           |
| `COPY`       | Copy files into image                                                           |
| `ADD`        | Copy/add files; has extra archive/URL semantics, so `COPY` is usually preferred |
| `RUN`        | Execute command during image build                                              |
| `EXPOSE`     | Document intended container port                                                |
| `CMD`        | Default command when container starts                                           |
| `ENTRYPOINT` | Define the container's primary executable                                       |
| `ENV`        | Set environment variables                                                       |
| `ARG`        | Define build-time variables                                                     |
| `USER`       | Set the user for subsequent commands/runtime                                    |
| `VOLUME`     | Declare a mount point                                                           |

For now, focus heavily on:

```text
FROM
WORKDIR
COPY
RUN
EXPOSE
CMD
```

---

# 30. The Complete Docker Workflow

You now have the foundation of how a real application gets containerized:

```text
                 YOUR APPLICATION
                       │
                       ↓
                  Dockerfile
                       │
                       ↓
                docker build
                       │
                       ↓
                  Docker Image
                       │
             ┌─────────┴─────────┐
             │                   │
        docker run          docker push
             │                   │
             ↓                   ↓
        Container          Container Registry
             │                   │
             ↓                   │
       Running App               │
                                 │
                         docker pull
                                 ↓
                              Server
                                 │
                            docker run
                                 ↓
                            Container
```

### The key distinction to remember

> **Dockerfile is the recipe. Image is the packaged result. Container is the running instance.**

And the two commands that connect them are:

```bash
docker build
```

**Dockerfile → Image**

and:

```bash
docker run
```

**Image → Container**
