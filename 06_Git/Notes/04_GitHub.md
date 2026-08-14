What is Github
What is SSH and How to Generate them on Window, Mac or Linux 
Connection Github to Git
Origin 
Creating a New Repository on Github
Connection Remote Respository to Local Repository
Pushing local changes to remote repository 
other git providers 
adding multiple remotes# GitHub & Remote Repositories

## 1. What is GitHub?

### Definition

**GitHub is a cloud-based platform for hosting Git repositories and collaborating on software projects.**

Git manages version history locally, while GitHub provides a **remote repository** where your Git repository can be stored and shared.

### Git vs GitHub

```text
Git
│
├── Version Control System
├── Runs on your computer
├── Tracks changes
├── Creates commits
└── Manages branches

GitHub
│
├── Hosts Git repositories
├── Remote collaboration
├── Pull Requests
├── Issues
├── Code Reviews
└── CI/CD with GitHub Actions
```

### Typical workflow

```text
Local Project
     │
     ▼
    Git
     │
     │ git push
     ▼
   GitHub
     │
     │ git pull
     ▼
Other Developers
```

---

# 2. What is SSH?

### Definition

**SSH (Secure Shell)** is a cryptographic network protocol used to securely communicate with remote systems.

With GitHub, SSH allows your computer to authenticate with GitHub **without entering your GitHub username and password for every Git operation**.

Instead of:

```text
Username + Password
```

you use:

```text
SSH Key Pair
   │
   ├── Private Key → Your Computer
   │
   └── Public Key → GitHub
```

### SSH Key Pair

When you generate SSH keys, two files are created:

| Key         | Location        | Purpose                        |
| ----------- | --------------- | ------------------------------ |
| Private key | Your computer   | Must remain secret             |
| Public key  | Added to GitHub | Used to identify your computer |

**Never share your private key.**

---

# 3. Generate SSH Keys on Windows

Open **Git Bash** or PowerShell.

Check whether you already have SSH keys:

```bash
ls ~/.ssh
```

If you see something like:

```text
id_ed25519
id_ed25519.pub
```

you may already have an SSH key.

### Generate a new key

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

When prompted:

```text
Enter file in which to save the key:
```

Press **Enter** to use the default location.

You can optionally enter a passphrase for additional security.

The keys will normally be created under:

```text
~/.ssh/
```

with:

```text
id_ed25519
id_ed25519.pub
```

---

# 4. Generate SSH Keys on macOS

Open Terminal.

Check for existing keys:

```bash
ls -al ~/.ssh
```

Generate:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Press **Enter** to accept the default file location.

Your keys will typically be:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

---

# 5. Generate SSH Keys on Linux

Open your terminal.

Check:

```bash
ls -al ~/.ssh
```

Generate:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Press **Enter** for the default location.

The generated files are typically:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

The process is essentially the same on:

```text
Windows → Git Bash
macOS   → Terminal
Linux   → Terminal
```

---

# 6. Understanding the Generated Files

After generating the key:

```text
~/.ssh/
├── id_ed25519
└── id_ed25519.pub
```

### Private key

```text
id_ed25519
```

Keep this on your computer.

**Do not upload or share it.**

### Public key

```text
id_ed25519.pub
```

This is the key you provide to GitHub.

Display it:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the complete output.

It will look approximately like:

```text
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... your-email@example.com
```

---

# 7. Add SSH Key to GitHub

In GitHub:

```text
GitHub
  ↓
Settings
  ↓
SSH and GPG keys
  ↓
New SSH key
```

Give the key a recognizable title, such as:

```text
My Windows Laptop
```

Paste the contents of:

```text
id_ed25519.pub
```

into the key field.

Save it.

---

# 8. Test the GitHub SSH Connection

Run:

```bash
ssh -T git@github.com
```

The first time, you may be asked whether you trust the GitHub host.

Enter:

```text
yes
```

If authentication is successful, GitHub will respond with a message indicating that you've successfully authenticated.

This confirms:

```text
Your Computer
     │
     │ SSH
     ▼
  GitHub
```

---

# 9. Connecting Git to GitHub

There are two common protocols for connecting a local repository to GitHub:

### HTTPS

```text
https://github.com/username/repository.git
```

### SSH

```text
git@github.com:username/repository.git
```

For SSH:

```text
Local Git
    │
    │ SSH
    ▼
GitHub
```

Once SSH is configured, you can use Git commands such as:

```bash
git push
git pull
```

without repeatedly providing GitHub credentials.

---

# 10. What is `origin`?

### Definition

**`origin` is the default conventional name given to a remote repository.**

It is **not a Git command** and it is **not a special remote built into Git**.

It's simply a name.

For example:

```bash
git remote add origin git@github.com:username/my-project.git
```

Here:

```text
origin
   ↓
Name of the remote
```

and:

```text
git@github.com:username/my-project.git
   ↓
Remote repository URL
```

You can technically name the remote something else:

```bash
git remote add github git@github.com:username/my-project.git
```

But `origin` is the standard convention.

---

# 11. Creating a New Repository on GitHub

Go to:

[GitHub](https://github.com/?utm_source=chatgpt.com)

After signing in:

```text
GitHub
  ↓
New Repository
```

Provide:

```text
Repository name:
my-project
```

Choose visibility:

```text
Public
```

or:

```text
Private
```

Then create the repository.

You will have a remote repository:

```text
GitHub
└── my-project
```

---

# 12. Connecting Remote Repository to Local Repository

Suppose you already have:

```text
my-project/
├── README.md
└── app.py
```

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit"
```

Now connect the local repository to GitHub:

```bash
git remote add origin git@github.com:username/my-project.git
```

Check the remote:

```bash
git remote -v
```

Example:

```text
origin  git@github.com:username/my-project.git (fetch)
origin  git@github.com:username/my-project.git (push)
```

Your local repository is now connected to GitHub.

---

# 13. Pushing Local Changes to GitHub

### Definition

**`git push` sends local commits to a remote repository.**

First, check your branch:

```bash
git branch
```

Suppose your branch is:

```text
* main
```

Set the upstream remote:

```bash
git push -u origin main
```

Here:

```text
git push
    │
    ├── origin → remote name
    │
    └── main → branch name
```

After the first push, future pushes can usually be:

```bash
git push
```

### Complete workflow

```bash
git add .
git commit -m "Add new feature"
git push
```

The flow becomes:

```text
Working Directory
       │
    git add
       ▼
Staging Area
       │
  git commit
       ▼
Local Repository
       │
    git push
       ▼
GitHub Repository
```

---

# 14. Making Another Change and Pushing It

Modify your project:

```bash
echo "New feature" >> README.md
```

Check:

```bash
git status
```

Stage:

```bash
git add README.md
```

Commit:

```bash
git commit -m "Add new feature information"
```

Push:

```bash
git push
```

Now GitHub contains the new commit.

---

# 15. Other Git Providers

Git is not limited to GitHub.

Several platforms can host Git repositories.

| Provider        | Description                                          |
| --------------- | ---------------------------------------------------- |
| **GitHub**      | Popular Git hosting and collaboration platform       |
| **GitLab**      | Git hosting with strong DevOps/CI/CD capabilities    |
| **Bitbucket**   | Git hosting commonly used with Atlassian tools       |
| **Azure Repos** | Git repository hosting within Microsoft Azure DevOps |
| **Gitea**       | Lightweight, self-hosted Git platform                |

The Git commands remain largely the same.

For example:

```bash
git clone <repository-url>
git add .
git commit -m "message"
git push
```

The main difference is usually the **remote URL and platform-specific features**.

---

# 16. Adding Multiple Remotes

### Definition

A Git repository can have **multiple remote repositories**.

For example:

```text
                    ┌── GitHub
                    │
Local Repository ───┤
                    │
                    └── GitLab
```

You might use this when you want to maintain the same project on multiple Git hosting platforms.

---

## Add GitHub Remote

```bash
git remote add github git@github.com:username/my-project.git
```

## Add GitLab Remote

```bash
git remote add gitlab git@gitlab.com:username/my-project.git
```

Check:

```bash
git remote -v
```

Output:

```text
github  git@github.com:username/my-project.git (fetch)
github  git@github.com:username/my-project.git (push)

gitlab  git@gitlab.com:username/my-project.git (fetch)
gitlab  git@gitlab.com:username/my-project.git (push)
```

Now you have:

```text
Local Repository
       │
       ├──── github ────→ GitHub
       │
       └──── gitlab ────→ GitLab
```

---

# 17. Pushing to Multiple Remotes

Push to GitHub:

```bash
git push github main
```

Push to GitLab:

```bash
git push gitlab main
```

You can also push the same branch to both repositories separately:

```bash
git push github main
git push gitlab main
```

---

# 18. Useful Remote Commands

### Show remotes

```bash
git remote
```

### Show remote URLs

```bash
git remote -v
```

### Add remote

```bash
git remote add origin <URL>
```

### Remove remote

```bash
git remote remove origin
```

### Change remote URL

```bash
git remote set-url origin <NEW_URL>
```

### Inspect a remote

```bash
git remote show origin
```

---

# Complete GitHub Workflow

```text
                GitHub
                  ▲
                  │
               git push
                  │
                  │
Local Repository ─┤
      ▲           │
      │           │
  git commit      │
      ▲           │
      │           │
 Staging Area      │
      ▲           │
      │           │
   git add         │
      ▲           │
      │           │
Working Directory
```

### Commands

```bash
# Create project
mkdir my-project
cd my-project

# Initialize Git
git init

# Create file
touch README.md

# Add data
echo "# My Project" > README.md

# Stage
git add README.md

# Commit
git commit -m "Initial commit"

# Connect GitHub repository
git remote add origin git@github.com:username/my-project.git

# Verify remote
git remote -v

# Push
git push -u origin main
```

### Core concepts to remember

```text
Git
 ↓
Local Version Control

GitHub
 ↓
Remote Repository Hosting

SSH
 ↓
Secure Authentication

origin
 ↓
Name of a Remote

git remote add
 ↓
Connect Local Repository → Remote Repository

git push
 ↓
Local Commits → Remote Repository
```
