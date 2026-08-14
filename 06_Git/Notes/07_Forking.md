# Forking

## 1. Working with Existing Projects

When working with an **existing project**, you may not have permission to directly modify its GitHub repository.

For example:

```text
Original Project
GitHub
└── company/project
```

You want to make changes to it, but you are not a collaborator.

Instead of directly modifying the original repository, you can **fork** it.

```text
Original Repository
        │
        │ Fork
        ▼
Your GitHub Repository
```

A fork creates your own copy of the repository under your GitHub account.

---

# 2. Why Fork?

### Definition

**Forking** means creating a personal copy of another user's or organization's repository under your own GitHub account.

A fork is commonly used when contributing to **open-source projects**.

### Example

Suppose there is an open-source project:

```text
github.com/company/project
```

You want to contribute to it.

You don't have direct write access:

```text
Original Repository
       │
       │ ❌ No write access
       ▼
     You
```

So you fork it:

```text
Original Repository
       │
       │ Fork
       ▼
Your Repository
```

Now:

```text
Original Repository
github.com/company/project

        ↓ fork

Your Fork
github.com/your-username/project
```

You can make changes to your fork without affecting the original repository.

---

# 3. Why Do We Fork?

Forking is useful when:

* You don't have write access to the original repository.
* You want to contribute to an open-source project.
* You want your own copy of an existing project.
* You want to experiment without affecting the original project.
* You want to create a Pull Request back to the original project.

### Typical Open-Source Workflow

```text
Original Repository
        │
       Fork
        ↓
Your Fork
        │
      Clone
        ↓
Local Computer
        │
   Make Changes
        ↓
      Commit
        ↓
      Push
        ↓
Your Fork
        │
  Pull Request
        ↓
Original Repository
```

---

# 4. How to Fork a Repository

Suppose you want to contribute to:

```text
github.com/company/project
```

Open the repository on GitHub.

Click:

```text
Fork
```

GitHub asks where you want to create the fork.

Select your account.

GitHub creates:

```text
github.com/your-username/project
```

You now have:

```text
Original Repository
        │
        └──────────┐
                   │
                  Fork
                   │
                   ▼
             Your Repository
```

The original repository is commonly called the **upstream repository**.

Your fork is your **origin repository** when you clone it.

---

# 5. Cloning the Forked Project to Local

After creating the fork, you need to download it to your computer.

Go to **your fork** on GitHub.

Click:

```text
Code
```

Select SSH if you have configured SSH:

```text
git@github.com:your-username/project.git
```

Clone it:

```bash id="ljj7g7"
git clone git@github.com:your-username/project.git
```

Then enter the project:

```bash id="3b7ypj"
cd project
```

Check the repository:

```bash id="31pgwz"
git status
```

---

# 6. What Does `git clone` Do?

`git clone` downloads a remote Git repository to your local computer.

```bash id="a8v8a3"
git clone <repository-url>
```

For example:

```bash id="0ndtqo"
git clone git@github.com:your-username/project.git
```

It creates:

```text id="1sv4ay"
Your Computer
└── project/
    ├── .git/
    ├── README.md
    ├── src/
    └── ...
```

It also automatically configures the cloned repository's remote.

Check:

```bash id="qy8kju"
git remote -v
```

You will typically see:

```text id="vv3h7f"
origin  git@github.com:your-username/project.git (fetch)
origin  git@github.com:your-username/project.git (push)
```

---

# 7. What is `origin` in a Forking Workflow?

After cloning your fork:

```bash id="8w8x4g"
git remote -v
```

You typically get:

```text id="20cl3m"
origin  git@github.com:your-username/project.git
```

Here:

```text id="twl2sy"
origin
  ↓
Your fork on GitHub
```

So:

```text id="44t40s"
Local Repository
       │
       │ origin
       ▼
Your GitHub Fork
```

---

# 8. What is `upstream`?

### Definition

In a fork-based workflow, **`upstream` is the conventional name for the original repository that you forked.**

For example:

```text id="lx4lpx"
Original Repository
github.com/company/project
        │
        │ Fork
        ▼
Your Fork
github.com/your-username/project
```

Your local repository can have:

```text id="jkv2e1"
origin
   ↓
Your Fork

upstream
   ↓
Original Repository
```

### Important

`upstream` is **not a special Git keyword**.

It is simply a commonly used remote name.

Just like `origin`, it is a name that developers agree to use by convention.

---

# 9. Adding `upstream` to Local Repository

After cloning your fork, add the original repository as another remote.

```bash id="u2jks7"
git remote add upstream git@github.com:company/project.git
```

Check:

```bash id="ux7e7g"
git remote -v
```

You should now see:

```text id="8p5mnp"
origin    git@github.com:your-username/project.git (fetch)
origin    git@github.com:your-username/project.git (push)

upstream  git@github.com:company/project.git (fetch)
upstream  git@github.com:company/project.git (push)
```

Your local repository now knows about both repositories.

```text id="kqz2fu"
                    ┌── origin ──→ Your Fork
                    │
Local Repository ───┤
                    │
                    └── upstream → Original Repository
```

---

# 10. Why Do We Need `upstream`?

The original repository can continue receiving new changes.

For example:

```text id="o5k8tm"
Original Repository
A → B → C → D → E
```

Your fork may be behind:

```text id="x7m8s0"
Your Fork
A → B → C
```

Your local repository also has:

```text id="3x6tw9"
A → B → C
```

You can use `upstream` to get the latest changes from the original repository.

Fetch:

```bash id="55nh3e"
git fetch upstream
```

Now Git knows about the latest upstream changes.

You can inspect the branches:

```bash id="8s0h7m"
git branch -a
```

---

# 11. Updating Your Local Main from Upstream

Suppose the original project has new changes.

First switch to your main branch:

```bash id="t0ft4m"
git switch main
```

Fetch the original repository:

```bash id="8u8nkm"
git fetch upstream
```

Merge the upstream main branch:

```bash id="z0wqyi"
git merge upstream/main
```

Now your local `main` contains the latest upstream changes.

Then update your fork:

```bash id="8f9xgr"
git push origin main
```

The flow is:

```text id="whu2tr"
Original Repository
       │
       │ git fetch upstream
       ▼
Local Repository
       │
       │ git merge upstream/main
       ▼
Local main
       │
       │ git push origin main
       ▼
Your Fork
```

---

# 12. Complete Fork Workflow

Suppose the original project is:

```text id="5qgjj9"
git@github.com:company/project.git
```

### Step 1 — Fork on GitHub

```text id="t5qz4b"
company/project
      │
     Fork
      ↓
your-username/project
```

### Step 2 — Clone your fork

```bash id="m0j3ud"
git clone git@github.com:your-username/project.git
```

### Step 3 — Enter project

```bash id="4p1f6b"
cd project
```

### Step 4 — Check remote

```bash id="2ezv8u"
git remote -v
```

You'll see:

```text id="7w4h1e"
origin → your-username/project
```

### Step 5 — Add upstream

```bash id="s8n3j9"
git remote add upstream git@github.com:company/project.git
```

### Step 6 — Verify

```bash id="fl9x4k"
git remote -v
```

Now:

```text id="1m0o4c"
origin   → Your Fork
upstream → Original Repository
```

---

# 13. Creating a Feature Branch

Before making changes, update your local `main`:

```bash id="j0e1jk"
git switch main
git fetch upstream
git merge upstream/main
```

Create a feature branch:

```bash id="u5r5m9"
git switch -c feature/add-search
```

Make your changes.

Stage:

```bash id="5b9l6r"
git add .
```

Commit:

```bash id="8a4y7s"
git commit -m "Add search functionality"
```

---

# 14. Push the Feature Branch to Your Fork

Push to **your fork**, not directly to the original repository:

```bash id="v7t0c4"
git push -u origin feature/add-search
```

Now:

```text id="6gcv85"
Local
  │
  │ push
  ▼
Your Fork
  │
  │ Pull Request
  ▼
Original Repository
```

---

# 15. Create Pull Request

On GitHub:

```text id="7q1gri"
Your Fork
    │
    │
    ▼
feature/add-search
    │
    │ Pull Request
    ▼
Original Repository
    │
    ▼
main
```

You are requesting:

> Merge my changes into the original project's `main` branch.

The project maintainer reviews your changes.

If approved, your changes are merged into the original project.

---

# 16. `origin` vs `upstream`

This is the most important concept in forking.

| Remote     | Usually points to   | Purpose                    |
| ---------- | ------------------- | -------------------------- |
| `origin`   | Your fork           | Push your changes          |
| `upstream` | Original repository | Get latest project changes |

Remember:

```text id="y6q2m1"
                 Original Repository
                         ▲
                         │
                     upstream
                         │
                         │
                  Local Repository
                         │
                       origin
                         │
                         ▼
                      Your Fork
```

### Typical commands

Get changes from original:

```bash id="p73vvp"
git fetch upstream
```

Push your work to your fork:

```bash id="3d9nqk"
git push origin feature/my-feature
```

---

# 17. Important Remote Commands

### List remotes

```bash id="1t2x1h"
git remote
```

### Show remote URLs

```bash id="3ry9jc"
git remote -v
```

### Add upstream

```bash id="f4g4lo"
git remote add upstream <original-repository-url>
```

### Fetch upstream

```bash id="3m8tde"
git fetch upstream
```

### Remove upstream

```bash id="9r6ylo"
git remote remove upstream
```

### Change upstream URL

```bash id="e2r1m0"
git remote set-url upstream <new-url>
```

### Inspect upstream

```bash id="x4m9jp"
git remote show upstream
```

---

# 18. Fork vs Clone

These are also different concepts.

### Fork

Creates a copy of a repository **on GitHub**.

```text id="h4w2a5"
GitHub
Original
   │
   │ Fork
   ▼
Your GitHub Account
```

### Clone

Downloads a repository **from a remote repository to your local computer**.

```text id="yd9d7j"
GitHub
   │
   │ git clone
   ▼
Your Computer
```

Typical workflow:

```text id="m2i9d6"
Fork
 ↓
Clone
 ↓
Modify
 ↓
Commit
 ↓
Push
 ↓
Pull Request
```

---

# 19. Complete Open-Source Contribution Workflow

```text id="5rj0w7"
              Original Repository
                     │
                     │ Fork
                     ▼
                  Your Fork
                     │
                     │ git clone
                     ▼
                Local Repository
                     │
                     │
               git remote add
                 upstream
                     │
                     ▼
              Create Feature Branch
                     │
                     ▼
                Make Changes
                     │
                     ▼
                   Commit
                     │
                     │ git push origin
                     ▼
                  Your Fork
                     │
                     │ Pull Request
                     ▼
              Original Repository
                     │
                     ▼
                   Review
                     │
                     ▼
                   Merge
```

## Key Commands

```bash id="g3s2n5"
# Clone your fork
git clone git@github.com:your-username/project.git

# Enter project
cd project

# Check remotes
git remote -v

# Add original repository
git remote add upstream git@github.com:company/project.git

# Get changes from original repository
git fetch upstream

# Update local main
git switch main
git merge upstream/main

# Create feature branch
git switch -c feature/my-feature

# Stage changes
git add .

# Commit
git commit -m "Add my feature"

# Push to your fork
git push -u origin feature/my-feature
```

### The core idea

```text id="2x8c0v"
ORIGINAL REPOSITORY
        │
      Fork
        ↓
    YOUR FORK
        │
      Clone
        ↓
LOCAL REPOSITORY
   │            │
   │ origin     │ upstream
   ↓            ↓
Your Fork    Original Repo
   │
   │ Push
   ↓
Your Fork
   │
   │ Pull Request
   ↓
Original Repository
```

**`origin` = your fork.**
**`upstream` = the original project.**
**Fork = GitHub-side copy.**
**Clone = local copy.**
