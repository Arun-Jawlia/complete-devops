# Git Basics

## 1. Initializing a Git Repository

### Definition

**Initializing a Git repository** means converting an existing project directory into a Git-managed repository.

We use:

```bash
git init
```

### Example

Create a project:

```bash
mkdir my-project
cd my-project
```

Initialize Git:

```bash
git init
```

Output:

```text
Initialized empty Git repository in .../my-project/.git/
```

Git creates a hidden `.git` directory.

```text
my-project/
└── .git/
```

The `.git` directory contains Git's internal information, including:

* Commit history
* Branch information
* Configuration
* Repository metadata

### Check repository status

```bash
git status
```

Example:

```text
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

> **Important:** `git init` should normally be executed inside your project directory.

---

# 2. Making the First Change

After initializing the repository, create or modify a file.

For example:

```bash
touch README.md
```

Now the project looks like:

```text
my-project/
├── .git/
└── README.md
```

Check Git status:

```bash
git status
```

You may see:

```text
Untracked files:
  README.md
```

### What does "Untracked" mean?

Git sees the file, but Git is **not tracking it yet**.

At this point:

```text
README.md
    ↓
Untracked
    ↓
Git is not tracking this file
```

---

# 3. Staging

### Definition

**Staging** means selecting changes that you want to include in the next commit.

The staging area is also called the **Index**.

Use:

```bash
git add README.md
```

Check the status:

```bash
git status
```

Now you should see:

```text
Changes to be committed:
  new file: README.md
```

The file has moved from:

```text
Working Directory
       ↓
   git add
       ↓
Staging Area
```

### Stage all files

```bash
git add .
```

This stages all changes in the current directory.

### Important

`git add` **does not create a commit**.

It only moves the selected changes into the staging area.

---

# 4. Committing the First Change

### Definition

A **commit** is a snapshot of the staged changes in your Git repository.

Use:

```bash
git commit -m "Initial commit"
```

Example output:

```text
[master abc1234] Initial commit
 1 file changed
 create mode 100644 README.md
```

The workflow is:

```text
Working Directory
       │
       │ git add
       ▼
Staging Area
       │
       │ git commit
       ▼
Git Repository
```

### Check commit history

```bash
git log
```

Example:

```text
commit abc1234
Author: Your Name
Date:   ...

    Initial commit
```

### Why commit messages matter

A commit message should describe the change.

Good:

```bash
git commit -m "Add README file"
```

Bad:

```bash
git commit -m "changes"
```

---

# 5. Adding Data to Files

Now add some data to `README.md`.

For example:

```bash
echo "# My Git Project" > README.md
```

Check the file:

```bash
cat README.md
```

Output:

```text
# My Git Project
```

Now check Git:

```bash
git status
```

Git will show that `README.md` has been modified:

```text
Changes not staged for commit:
  modified: README.md
```

The change is currently in the **Working Directory**, not the staging area.

Stage it:

```bash
git add README.md
```

Then commit it:

```bash
git commit -m "Add project title"
```

---

# Complete Git Basics Workflow

```bash
mkdir my-project
cd my-project

git init

touch README.md

echo "# My Git Project" > README.md

git status

git add README.md

git status

git commit -m "Initial commit"

git log
```

The fundamental Git lifecycle is:

```text
        Create / Modify File
                │
                ▼
        Working Directory
                │
             git add
                │
                ▼
          Staging Area
                │
           git commit
                │
                ▼
        Git Repository
```

### Key Commands

| Command                   | Purpose                         |
| ------------------------- | ------------------------------- |
| `git init`                | Initialize a Git repository     |
| `git status`              | Check current repository status |
| `git add <file>`          | Stage a specific file           |
| `git add .`               | Stage all changes               |
| `git commit -m "message"` | Create a commit                 |
| `git log`                 | View commit history             |
| `cat <file>`              | Display file contents           |
