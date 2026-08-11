# Web Framework & Flask — DevOps Perspective

For a DevOps engineer, you don't need to become a full-time backend developer, but you **must understand how an application works before you deploy, monitor, secure, and scale it**.

---

# 1. What is a Web Framework?

A **web framework** is a collection of tools, libraries, and rules that helps developers build web applications and APIs without implementing everything from scratch.

Without a framework:

```text
Request
   ↓
Manually handle HTTP
   ↓
Parse URL
   ↓
Validate data
   ↓
Connect Database
   ↓
Write Response
```

With a framework:

```text
Client
   ↓
Web Framework
   ↓
Route
   ↓
Business Logic
   ↓
Database
   ↓
Response
```

### Examples of Python Web Frameworks

* Django
* Flask
* FastAPI
* Bottle
* CherryPy
* web2py

---

# 2. Types of Web Frameworks

There are several ways to classify frameworks.

### Full-Stack Framework

Provides almost everything required to build a complete web application.

Example:

```text
Django
```

Usually includes:

* Routing
* Database ORM
* Authentication
* Templates
* Forms
* Admin panel

---

### Microframework

Provides only the core functionality and allows developers to add components as required.

Examples:

```text
Flask
Bottle
```

Flask gives you the basic web functionality, while you choose additional libraries according to your requirements.

---

### API Framework

Focused mainly on building APIs.

Example:

```text
FastAPI
```

---

# 3. What is a Web Server?

A **web server** is software or a machine that receives HTTP requests and returns responses.

Basic flow:

```text
Browser / Client
       │
       │ HTTP Request
       ▼
   Web Server
       │
       ▼
 Application
       │
       ▼
 HTTP Response
       │
       ▼
    Client
```

Popular web servers:

* Nginx
* Apache HTTP Server
* Microsoft IIS

For example:

```text
User
 ↓
Nginx
 ↓
Flask Application
 ↓
MongoDB
```

### Important distinction

**Web server ≠ Web framework**

Nginx is a web server.

Flask is a web framework.

They solve different problems.

---

# 4. Django

**Django** is a Python full-stack web framework.

It follows the principle:

> Batteries included.

It provides many features out of the box.

```text
Django
├── Routing
├── ORM
├── Authentication
├── Admin
├── Forms
├── Templates
└── Security
```

Commonly used for:

* Large web applications
* Enterprise applications
* Content management systems
* APIs

---

# 5. web2py

**web2py** is a Python web framework designed to simplify web application development.

It provides features such as:

* Routing
* Database abstraction
* Templates
* Security
* Authentication

It is less commonly encountered in modern DevOps work than Flask or Django.

---

# 6. Flask

**Flask** is a lightweight Python web framework.

It is called a **microframework** because it provides the core functionality without forcing a large application structure.

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

app.run()
```

Flow:

```text
Client
   ↓
HTTP Request
   ↓
Flask
   ↓
Route "/"
   ↓
home()
   ↓
HTTP Response
```

We'll cover Flask in detail below.

---

# 7. Bottle

**Bottle** is another lightweight Python web framework.

It is very small and can be useful for:

* Small applications
* APIs
* Prototypes
* Embedded applications

---

# 8. CherryPy

**CherryPy** is a lightweight Python web framework that allows developers to build web applications using Python objects and classes.

It can also operate as its own HTTP server.

---

# 9. Why Does a DevOps Engineer Need to Know This?

This is the important part.

A DevOps engineer works with applications throughout their lifecycle.

You need to understand what is running **inside the server/container** you're deploying.

For example:

```text
Developer
    ↓
Python + Flask Application
    ↓
Git
    ↓
Docker
    ↓
CI/CD
    ↓
AWS
    ↓
Kubernetes
    ↓
Monitoring
```

If you don't understand Flask, it becomes harder to understand:

* What process should run?
* Which port does the application use?
* What endpoint should be tested?
* What environment variables are required?
* Why is the container failing?
* Why is the health check failing?
* Where are application logs?
* How should Nginx route traffic?
* How should Kubernetes expose the application?

You don't necessarily need to build complex Flask applications, but you should be able to **run, configure, containerize, deploy, troubleshoot, and monitor one**.

---

# 10. What is REST API?

**REST** stands for **Representational State Transfer**.

A REST API allows different applications to communicate over HTTP.

For example:

```text
Frontend
   │
   │ GET /users
   ▼
Flask REST API
   │
   ▼
Database
```

The API returns data, usually in JSON format.

Example:

```json
{
  "id": 101,
  "name": "Arun",
  "role": "DevOps Engineer"
}
```

---

# 11. What is JSON?

**JSON = JavaScript Object Notation**

It is a lightweight data format commonly used for communication between clients and APIs.

Example:

```json
{
  "name": "Arun",
  "age": 25,
  "skills": ["Python", "Docker", "AWS"]
}
```

REST APIs commonly use:

```text
Request
   ↓
JSON
   ↓
API
   ↓
JSON
   ↓
Response
```

---

# 12. Understanding a URL

Consider:

```text
https://api.example.com:443/users/101?active=true
```

Break it down:

```text
https://api.example.com:443/users/101?active=true
  │          │          │      │       │
Protocol   Hostname    Port   Route   Query
```

---

## Protocol

```text
https
```

Defines how communication happens between client and server.

Common protocols:

```text
HTTP
HTTPS
```

---

## Hostname

```text
api.example.com
```

Identifies the server/service being accessed.

It can resolve to an IP address through DNS.

---

## Port

```text
443
```

Identifies the network port where the service is listening.

Common ports:

```text
HTTP  → 80
HTTPS → 443
SSH   → 22
```

Port can be omitted from the URL when the default port for the protocol is being used.

---

## Route / Path

```text
/users/101
```

Identifies the resource being requested.

Examples:

```text
/users
/products
/orders/123
```

---

## Query Parameters

```text
?active=true
```

Additional data sent with the request.

Multiple parameters:

```text
/products?category=mobile&page=2
```

---

# 13. HTTP vs HTTPS

## HTTP

**HTTP = HyperText Transfer Protocol**

It transfers data between clients and servers.

```text
Client
  │
  │ HTTP
  ▼
Server
```

HTTP does not provide encryption by itself.

---

## HTTPS

**HTTPS = HTTP Secure**

HTTPS uses **TLS encryption** to protect data in transit.

```text
Client
  │
  │ HTTPS + TLS
  ▼
Server
```

HTTPS provides:

* Encryption
* Authentication of the server
* Integrity protection

For production applications, HTTPS is normally expected.

---

# 14. HTTP Methods

HTTP methods tell the server what operation the client wants to perform.

| Method    | Purpose                             | Example          |
| --------- | ----------------------------------- | ---------------- |
| `GET`     | Read data                           | Get users        |
| `POST`    | Create data                         | Create user      |
| `PUT`     | Replace/update data                 | Update user      |
| `PATCH`   | Partially update data               | Update user name |
| `DELETE`  | Delete data                         | Delete user      |
| `HEAD`    | Get headers without response body   | Check resource   |
| `OPTIONS` | Get supported communication options | CORS/preflight   |

---

## GET

Retrieve data.

```http
GET /users
```

Response:

```json
[
  {
    "id": 1,
    "name": "Arun"
  }
]
```

---

## POST

Create a new resource.

```http
POST /users
```

Request body:

```json
{
  "name": "Arun",
  "role": "DevOps"
}
```

---

## PUT

Replace an existing resource.

```http
PUT /users/1
```

---

## PATCH

Partially update a resource.

```http
PATCH /users/1
```

```json
{
  "role": "Cloud Engineer"
}
```

---

## DELETE

Delete a resource.

```http
DELETE /users/1
```

---

# 15. What Happens When You Access an API?

Suppose you call:

```text
https://api.example.com/users/101
```

The actual flow is approximately:

```text
User / Application
        │
        ▼
      DNS
        │
        ▼
   IP Address
        │
        ▼
 Load Balancer / Nginx
        │
        ▼
 Flask Application
        │
        ▼
      Route
        │
        ▼
 Business Logic
        │
        ▼
    Database
        │
        ▼
    JSON Response
        │
        ▼
      Client
```

This is directly relevant to DevOps because you will eventually need to deploy and troubleshoot each layer.

---

# 16. What is Flask?

**Flask is a lightweight Python web framework used to build web applications and REST APIs.**

It is based on:

* **Werkzeug** → WSGI utilities and HTTP functionality
* **Jinja** → Template engine

A minimal Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello DevOps"

if __name__ == "__main__":
    app.run()
```

Run it:

```bash
python app.py
```

By default, Flask's development server usually listens on:

```text
http://127.0.0.1:5000
```

---

# Flask Request Flow

```text
Client
  │
  │ HTTP Request
  ▼
Flask
  │
  ▼
Route
  │
  ▼
Python Function
  │
  ▼
Database / Business Logic
  │
  ▼
Response
  │
  ▼
Client
```

Example:

```python
@app.route("/users", methods=["GET"])
def get_users():
    return {
        "users": ["Arun", "Rahul"]
    }
```

Request:

```http
GET /users
```

Response:

```json
{
  "users": ["Arun", "Rahul"]
}
```

---

# Flask from a DevOps Perspective

As a DevOps engineer, focus on understanding this lifecycle:

```text
Flask Application
       ↓
requirements.txt
       ↓
Python Environment
       ↓
Gunicorn
       ↓
Docker
       ↓
Nginx / Load Balancer
       ↓
AWS / Kubernetes
       ↓
Monitoring & Logs
```

For example, a production setup might look like:

```text
                    Internet
                       │
                       ▼
                  Load Balancer
                       │
                       ▼
                     Nginx
                       │
                       ▼
                   Gunicorn
                       │
                       ▼
                Flask Application
                       │
                       ▼
                    MongoDB
```

**Key DevOps takeaway:** You don't need deep Flask application-development expertise, but you should understand enough Flask to **run the application, expose APIs, configure environment variables, create a Docker image, deploy it, expose its port, configure health checks, inspect logs, and troubleshoot failures.**
