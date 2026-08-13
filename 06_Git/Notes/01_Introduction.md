# Git & GitHub — Introduction

## 1. What is Git?

### Definition

**Git is a distributed version control system (DVCS)** used to track changes in source code and other files.

In simple terms:

> **Git helps developers save, track, compare, and manage different versions of their project.**

Git runs on your **local computer**. You can use Git without an internet connection.

### Example

Suppose you are developing a website:

```text
my-project/
├── index.html
├── style.css
└── script.js
```

You make changes to `script.js`.

Without Git, you might manually create:

```text
script-v1.js
script-v2.js
script-final.js
script-final-new.js
script-final-really-final.js
```

This quickly becomes difficult to manage.

With Git:

```text
Commit 1 → Initial project
Commit 2 → Added login page
Commit 3 → Fixed login bug
Commit 4 → Added authentication
```

You can move between these versions when required.

---

# 2. What is GitHub?

### Definition

**GitHub is a cloud-based platform for hosting Git repositories and collaborating on software projects.**

Git manages your project **locally**.

GitHub allows you to store and collaborate on that Git repository **remotely**.

### Simple Difference

```text
Git
 ↓
Version control
 ↓
Your local computer
```

```text
GitHub
 ↓
Remote repository hosting
 ↓
Internet / Cloud
```

### Example

You create a project on your laptop:

```text
Laptop
   ↓
   Git
   ↓
Local Repository
   ↓
git push
   ↓
GitHub
   ↓
Remote Repository
```

Other developers can then:

```text
GitHub
   ↓
git clone / git pull
   ↓
Their Computer
```

---

# 3. Git vs GitHub

| Git                       | GitHub                                          |
| ------------------------- | ----------------------------------------------- |
| Version control system    | Git hosting/collaboration platform              |
| Runs locally              | Runs primarily as a cloud service               |
| Tracks file changes       | Hosts Git repositories                          |
| Works offline             | Usually requires internet for remote operations |
| Created by Linus Torvalds | A platform built around Git                     |
| Command-line tool         | Web platform + Git services                     |
| `git commit`              | Pull Requests, Issues, Actions, etc.            |

### Important

Git and GitHub are **not the same thing**.

You can use:

```bash
git
```

without GitHub.

But GitHub repositories generally use Git for version control.

---

# 4. Why Do We Use Git?

Git solves several important software-development problems.

## 4.1 Version Control

Git maintains the history of your project.

Example:

```text
v1 → Login page
v2 → Registration page
v3 → Authentication
v4 → Bug fix
v5 → Payment integration
```

You can inspect what changed at each stage.

---

## 4.2 Track Changes

Git tells you:

* Which files changed?
* What lines changed?
* Who made the change?
* When was it changed?
* Why was it committed?

Example:

```bash
git diff
```

This shows changes that haven't been staged.

---

## 4.3 Collaboration

Multiple developers can work on the same project.

For example:

```text
Developer A → Authentication
Developer B → Payment
Developer C → Dashboard
```

Git provides mechanisms to combine their work.

---

## 4.4 Branching

Git allows developers to create separate development branches.

```text
main
 │
 ├── feature/login
 │
 ├── feature/payment
 │
 └── bugfix/navbar
```

For example:

```bash
git branch feature/login
```

Then:

```bash
git switch feature/login
```

The developer can work on the feature without directly modifying `main`.

---

## 4.5 Rollback

Suppose your latest code introduces a serious bug.

Git maintains previous commits, allowing you to inspect or restore earlier versions.

```bash
git log
```

You can see your previous commits.

---

# 5. Why Do We Use GitHub?

GitHub adds collaboration and remote-development capabilities on top of Git.

### Important uses

### 1. Remote Repository

Store your project online.

```text
Local Repository
       ↓
    git push
       ↓
GitHub Repository
```

### 2. Collaboration

Developers can work together using:

* Branches
* Pull Requests
* Code Reviews
* Issues
* Discussions

### 3. Backup

Your repository exists remotely, so your project isn't stored only on your laptop.

### 4. Portfolio

Developers can showcase projects and code to:

* Recruiters
* Hiring managers
* Other developers
* Open-source communities

### 5. CI/CD

GitHub can integrate with CI/CD systems and GitHub Actions.

Example:

```text
Developer
   ↓
git push
   ↓
GitHub
   ↓
CI/CD Pipeline
   ↓
Build
   ↓
Test
   ↓
Deploy
```

---

# 6. Git in the DevOps Lifecycle

Git is one of the fundamental tools in modern DevOps workflows.

A simplified workflow:

```text
Developer
    ↓
Write Code
    ↓
Git
    ↓
Commit
    ↓
GitHub
    ↓
CI/CD
    ↓
Build
    ↓
Test
    ↓
Deploy
    ↓
Production
```

For a DevOps Engineer, understanding Git is essential because CI/CD pipelines are commonly triggered by Git repository events.

For example:

```text
git push
   ↓
GitHub
   ↓
GitHub Actions / Jenkins
   ↓
Build
   ↓
Automated Tests
   ↓
Docker Build
   ↓
Deploy
```

---

# 7. Downloading Git

Git needs to be installed on your computer before you can use commands such as:

```bash
git init
git clone
git add
git commit
git push
```

You can download Git from the official website:

[Git Official Website](https://git-scm.com/?utm_source=chatgpt.com)

---

## Windows

Go to the Git website and download the Windows installer.

After installation, open:

* Git Bash
* Command Prompt
* PowerShell

Then verify the installation:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

The exact version depends on the current Git release.

---

## Linux

On Debian/Ubuntu:

```bash
sudo apt update
sudo apt install git
```

Verify:

```bash
git --version
```

On Fedora:

```bash
sudo dnf install git
```

On Arch:

```bash
sudo pacman -S git
```

---

## macOS

If Homebrew is installed:

```bash
brew install git
```

Then:

```bash
git --version
```

---

# 8. Configure Git

After installing Git, configure your identity.

### Configure username

```bash
git config --global user.name "Your Name"
```

### Configure email

```bash
git config --global user.email "your@email.com"
```

Check configuration:

```bash
git config --global --list
```

Example:

```text
user.name=Your Name
user.email=your@email.com
```

### Why is this required?

Git associates commits with an author.

When you create a commit:

```text
Commit
 ├── Author: Your Name
 ├── Email: your@email.com
 └── Changes
```

---

# 9. Basic Linux Commands

Before learning Git deeply, you should be comfortable with basic Linux/Unix commands.

Git Bash on Windows provides many Unix-style commands.

---

## 9.1 `pwd`

### Definition

`pwd` means **Print Working Directory**.

It shows your current location.

```bash
pwd
```

Example:

```text
/home/user/projects
```

Think:

> **Where am I currently?**

---

# 9.2 `ls`

### Definition

`ls` lists files and directories.

```bash
ls
```

Example:

```text
app.py
README.md
requirements.txt
```

### Useful options

Show detailed information:

```bash
ls -l
```

Show hidden files:

```bash
ls -a
```

Both:

```bash
ls -la
```

---

# 9.3 `cd`

### Definition

`cd` means **Change Directory**.

It is used to move between directories.

```bash
cd folder-name
```

Example:

```bash
cd projects
```

Go back one directory:

```bash
cd ..
```

Go to home directory:

```bash
cd ~
```

---

# 9.4 `mkdir`

### Definition

`mkdir` means **Make Directory**.

Create a directory:

```bash
mkdir my-project
```

Then:

```bash
cd my-project
```

---

# 9.5 `touch`

Creates a new empty file.

```bash
touch README.md
```

Example:

```bash
touch app.py
```

Now:

```bash
ls
```

may show:

```text
app.py
README.md
```

---

# 9.6 `cat`

Displays the contents of a file.

```bash
cat README.md
```

Example:

```text
# My Project
This is my project.
```

---

# 9.7 `echo`

Prints text.

```bash
echo "Hello Git"
```

It can also write text into a file:

```bash
echo "Hello Git" > README.md
```

Be careful: `>` **overwrites** the file.

Use:

```bash
echo "Another line" >> README.md
```

to append.

---

# 9.8 `cp`

`cp` means **copy**.

Copy a file:

```bash
cp file.txt backup.txt
```

Copy a directory recursively:

```bash
cp -r project project-backup
```

---

# 9.9 `mv`

`mv` means **move**.

Move a file:

```bash
mv file.txt documents/
```

It can also rename files:

```bash
mv old-name.txt new-name.txt
```

---

# 9.10 `rm`

`rm` means **remove**.

Delete a file:

```bash
rm file.txt
```

Delete a directory and its contents:

```bash
rm -r my-folder
```

### Important

Be careful with:

```bash
rm -rf
```

It can recursively and forcefully delete files/directories.

---

# 9.11 `clear`

Clears the terminal.

```bash
clear
```

---

# 9.12 `history`

Shows previously executed commands.

```bash
history
```

Example:

```text
1  pwd
2  ls
3  mkdir project
4  cd project
5  git init
```

---

# 9.13 `whoami`

Shows the currently logged-in user.

```bash
whoami
```

Example:

```text
arun
```

---

# 9.14 `man`

Displays the manual/documentation for a command.

```bash
man ls
```

For example:

```bash
man git
```

Press `q` to exit.

---

# 10. Practice: Basic Linux Workflow

Let's create a project using the commands we learned.

### Step 1 — Check location

```bash
pwd
```

### Step 2 — List files

```bash
ls
```

### Step 3 — Create project

```bash
mkdir git-demo
```

### Step 4 — Enter project

```bash
cd git-demo
```

### Step 5 — Create files

```bash
touch README.md app.py
```

### Step 6 — Check files

```bash
ls
```

Output:

```text
README.md
app.py
```

### Step 7 — Add content

```bash
echo "# Git Demo Project" > README.md
```

### Step 8 — Read file

```bash
cat README.md
```

Output:

```text
# Git Demo Project
```

### Step 9 — Check current location

```bash
pwd
```

---

# 11. Git vs Linux Commands

These are different concepts.

### Linux command

```bash
ls
```

Used to interact with the filesystem.

### Git command

```bash
git status
```

Used to interact with a Git repository.

For example:

```text
Linux Commands
│
├── pwd
├── ls
├── cd
├── mkdir
├── touch
├── cp
├── mv
└── rm

Git Commands
│
├── git init
├── git status
├── git add
├── git commit
├── git branch
├── git merge
├── git pull
└── git push
```

---

# 12. Important Git Terminology

Before moving to Git commands, understand these terms:

| Term                  | Meaning                                   |
| --------------------- | ----------------------------------------- |
| **Repository**        | Project tracked by Git                    |
| **Working Directory** | Files currently being edited              |
| **Staging Area**      | Changes selected for the next commit      |
| **Commit**            | Snapshot of project changes               |
| **Branch**            | Independent line of development           |
| **Remote**            | Repository hosted elsewhere               |
| **Origin**            | Common default name for remote repository |
| **Clone**             | Copy a remote repository locally          |
| **Push**              | Send local commits to remote              |
| **Pull**              | Get remote changes and integrate them     |
| **Merge**             | Combine branches                          |

---

# 13. Big Picture

The relationship can be remembered as:

```text
                 DEVELOPMENT
                      │
                      ▼
                ┌───────────┐
                │   Linux   │
                │ Commands  │
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │    Git    │
                │   Local   │
                └─────┬─────┘
                      │
             git push │
                      ▼
                ┌───────────┐
                │  GitHub   │
                │  Remote   │
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │   CI/CD   │
                └─────┬─────┘
                      │
                      ▼
                  Production
```

### The core idea

> **Linux commands help you work with your operating system and filesystem. Git tracks your project changes. GitHub hosts Git repositories and enables collaboration.**

The next logical topic is **Git Repository → `git init` → Working Directory → Staging Area → Commit → Git Log → Git Status**, because this establishes the fundamental Git workflow before branches and GitHub remotes.
