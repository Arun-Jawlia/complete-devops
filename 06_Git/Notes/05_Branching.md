# Git Branches

## 1. What Are Branches?

### Definition

A **Git branch** is an independent line of development in a Git repository.

Branches allow you to work on changes without directly modifying the `main` branch.

Think of a branch as a separate path from your project's existing history:

```text
                  feature-login
                       ↓
A ─── B ────────────── C
      │
      └─────────────── main
```

A branch does **not** create a completely separate copy of your entire project. It is essentially a movable reference to commits in Git's history.

### Common branches

```text
main
develop
feature/login
feature/payment
bugfix/navbar
```

`main` is commonly used as the primary branch.

> Older repositories often use `master` instead of `main`. The commands are the same; only the branch name changes.

---

# 2. Use of Branches

Branches are mainly used to **isolate different types of work**.

### Example

Suppose your application is already running on:

```text
main
```

You need to develop a login feature.

Instead of directly changing `main`:

```text
main
 ↓
Modify login
 ↓
Something breaks
```

Create a feature branch:

```text
main
  │
  └── feature/login
          │
          ├── Login UI
          ├── Authentication
          └── Validation
```

The `main` branch remains stable while you work on the feature.

### Common uses

| Branch           | Purpose                 |
| ---------------- | ----------------------- |
| `main`           | Stable/production code  |
| `develop`        | Development integration |
| `feature/login`  | New feature             |
| `bugfix/payment` | Bug fix                 |
| `hotfix/api`     | Urgent production fix   |

---

# 3. Making a New Branch

First check your existing branches:

```bash
git branch
```

Example:

```text
* main
```

The `*` indicates your **current branch**.

### Create a new branch

```bash
git branch feature-login
```

Check:

```bash
git branch
```

Output:

```text
  feature-login
* main
```

The branch has been created, but you are **still on `main`**.

---

# 4. Switching to a Branch

Use:

```bash
git switch feature-login
```

Now:

```bash
git branch
```

Output:

```text
* feature-login
  main
```

The `*` has moved to `feature-login`.

---

## Create and Switch in One Command

Instead of:

```bash
git branch feature-login
git switch feature-login
```

you can use:

```bash
git switch -c feature-login
```

This:

1. Creates the branch
2. Immediately switches to it

Example:

```bash
git switch -c feature-login
```

Output:

```text
Switched to a new branch 'feature-login'
```

---

# 5. Making Changes on a Branch

Suppose you are currently on:

```text
feature-login
```

Check:

```bash
git branch
```

Output:

```text
  main
* feature-login
```

Make your changes:

```bash
echo "Login Feature" >> README.md
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
git commit -m "Add login feature"
```

Your history now looks like:

```text
              feature-login
                    ↓
A ─── B ─────────── C
      ↑
     main
```

The `main` branch has not received commit `C`.

---

# 6. Switching Back to Main

Use:

```bash
git switch main
```

Check:

```bash
git branch
```

Output:

```text
* main
  feature-login
```

Now you are working on `main`.

The changes committed on `feature-login` are not part of `main` yet.

---

# 7. Merging a Branch into Main

### Definition

**Merging** combines the changes from one branch into another branch.

Suppose:

```text
main
  │
  └── feature-login
           │
           ▼
      Login changes
```

You want to bring the login changes into `main`.

### Step 1 — Switch to main

```bash
git switch main
```

### Step 2 — Merge the feature branch

```bash
git merge feature-login
```

Git incorporates the commits from `feature-login` into `main`.

The history may become:

```text
A ─── B ─── C
          ↑
         main
```

If Git performs a fast-forward merge, there may not be a separate merge commit.

---

# 8. Fast-Forward Merge

Suppose the history is:

```text
A ─── B
      │
     main
```

Create a feature branch and add a commit:

```text
A ─── B ─── C
      │     ↑
     main  feature
```

When you run:

```bash
git switch main
git merge feature
```

Git can simply move `main` forward:

```text
A ─── B ─── C
           ↑
          main
```

This is called a **fast-forward merge**.

---

# 9. Merging with Different Branch Histories

Suppose both branches have new commits:

```text
          C ─── D
         /       \
A ─── B           ?
         \       /
          E ─── F
```

For example:

```text
main:     A → B → E
feature:       B → C → D
```

When merging:

```bash
git switch main
git merge feature
```

Git may create a merge commit:

```text
          C ─── D
         /       \
A ─── B           M
         \       /
          E ────
```

`M` represents the merge commit.

---

# 10. Pushing New Changes to the Remote Main Branch

After merging your feature branch locally:

```bash
git switch main
git merge feature-login
```

Your local `main` now contains the feature.

To send it to GitHub:

```bash
git push origin main
```

The workflow is:

```text
Feature Branch
      │
      │ git merge
      ▼
Local main
      │
      │ git push
      ▼
GitHub main
```

---

# 11. Complete Example

Let's go through the entire process.

### Step 1 — Start on main

```bash
git switch main
```

### Step 2 — Create feature branch

```bash
git switch -c feature-login
```

### Step 3 — Make changes

```bash
echo "Login Feature" >> README.md
```

### Step 4 — Check changes

```bash
git status
```

### Step 5 — Stage

```bash
git add README.md
```

### Step 6 — Commit

```bash
git commit -m "Add login feature"
```

### Step 7 — Go back to main

```bash
git switch main
```

### Step 8 — Merge feature

```bash
git merge feature-login
```

### Step 9 — Push main to GitHub

```bash
git push origin main
```

Final flow:

```text
                 feature-login
                       │
                       │
main ────────┐         │
             │         ▼
             │      Commit
             │         │
             └──── merge
                    │
                    ▼
                 main
                    │
                 git push
                    │
                    ▼
                  GitHub
```

---

# 12. Pushing a New Branch to GitHub

If you want to push the feature branch itself to GitHub **before merging**:

```bash
git push -u origin feature-login
```

After the first push:

```bash
git push
```

The remote repository will then contain:

```text
GitHub
│
├── main
└── feature-login
```

This is commonly used when working with **Pull Requests**.

---

# 13. `main` vs `master`

You may encounter both:

```text
main
master
```

They are simply branch names.

Modern repositories commonly use:

```text
main
```

Older repositories may use:

```text
master
```

If your repository uses `master`, use:

```bash
git switch master
```

and:

```bash
git push origin master
```

If it uses `main`:

```bash
git switch main
git push origin main
```

You can check your current branch with:

```bash
git branch
```

---

# Important Commands

| Command                       | Purpose                          |
| ----------------------------- | -------------------------------- |
| `git branch`                  | List local branches              |
| `git branch <name>`           | Create a branch                  |
| `git switch <name>`           | Switch branches                  |
| `git switch -c <name>`        | Create and switch                |
| `git merge <branch>`          | Merge branch into current branch |
| `git push origin main`        | Push main to remote              |
| `git push -u origin <branch>` | Push new branch and set upstream |
| `git branch -d <name>`        | Delete a merged local branch     |

### Core workflow

```text
Create Branch
     ↓
Switch to Branch
     ↓
Make Changes
     ↓
git add
     ↓
git commit
     ↓
Switch to main
     ↓
git merge feature
     ↓
git push origin main
```
