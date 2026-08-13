# Commits

## 1. Removing Changes from Stage

### Definition

Sometimes you stage a file using `git add`, but later decide that you **don't want that change included in the next commit**.

You can remove it from the staging area without deleting the actual changes from your file.

### Command

```bash
git restore --staged <file>
```

### Example

Suppose you modify:

```text
README.md
```

Stage it:

```bash
git add README.md
```

Check status:

```bash
git status
```

You will see:

```text
Changes to be committed:
    modified: README.md
```

Now remove it from staging:

```bash
git restore --staged README.md
```

Check again:

```bash
git status
```

Now:

```text
Changes not staged for commit:
    modified: README.md
```

### Important

`git restore --staged`:

* Removes the file from the **staging area**
* Keeps your changes in the **working directory**
* Does **not** delete your modifications

```text
Staging Area
     │
     │ git restore --staged
     ▼
Working Directory
```

---

# 2. Viewing the Overall History of the Project

### Definition

Git maintains the complete history of commits made to the repository.

To view the commit history:

```bash
git log
```

Example:

```text
commit a82f91c
Author: Arun
Date: ...

    Add login page

commit 72b4e11
Author: Arun
Date: ...

    Add README

commit 31ac812
Author: Arun
Date: ...

    Initial commit
```

Each commit contains information such as:

* Commit ID
* Author
* Date
* Commit message

### Short History

For a more compact view:

```bash
git log --oneline
```

Example:

```text
a82f91c Add login page
72b4e11 Add README
31ac812 Initial commit
```

This is commonly used to get a quick overview of the project's history.

---

# 3. Making Few More Commits

After the first commit, you can continue modifying your project and create additional commits.

Suppose you have:

```text
README.md
```

Add some content:

```bash
echo "This is my Git project." >> README.md
```

Check the changes:

```bash
git status
```

Stage the change:

```bash
git add README.md
```

Commit:

```bash
git commit -m "Add project description"
```

Now make another change:

```bash
echo "Learning Git and GitHub." >> README.md
```

Stage:

```bash
git add README.md
```

Commit:

```bash
git commit -m "Add Git learning information"
```

View the history:

```bash
git log --oneline
```

You might get:

```text
c92a31f Add Git learning information
b41d82a Add project description
a82f91c Initial commit
```

The project now has multiple snapshots:

```text
Initial commit
      ↓
Add project description
      ↓
Add Git learning information
```

Each commit represents a point in the project's history.

---

# 4. Removing a Commit from the History of a Project

There are different ways to remove commits depending on **which commit you want to remove** and whether the commit has already been shared with others.

For learning purposes, consider:

```text
A → B → C
```

where:

```text
A = Initial commit
B = Add README
C = Add documentation
```

## Remove the Most Recent Commit

If you want to remove the latest commit:

```bash
git reset --soft HEAD~1
```

### What happens?

```text
Before:

A → B → C
        ↑
       HEAD
```

After:

```text
A → B
     ↑
    HEAD
```

The commit `C` is removed from the commit history, but its changes remain **staged**.

---

## Remove the Latest Commit and Keep Changes Unstaged

Use:

```bash
git reset HEAD~1
```

or explicitly:

```bash
git reset --mixed HEAD~1
```

Result:

```text
Commit C
   ↓
Removed from history

Changes
   ↓
Working Directory
```

Your changes are preserved, but they are no longer staged.

---

## Remove the Latest Commit and Delete Its Changes

Use:

```bash
git reset --hard HEAD~1
```

This moves `HEAD` back one commit and discards the changes introduced by the removed commit.

```text
Before:

A → B → C
        ↑
       HEAD

After:

A → B
     ↑
    HEAD
```

### ⚠️ Important

`git reset --hard` can permanently discard uncommitted work.

Use it carefully.

---

# 5. Understanding `HEAD`

`HEAD` is a reference to the **current commit** you're working from.

For example:

```text
A → B → C
        ↑
       HEAD
```

`HEAD~1` means:

> The commit immediately before `HEAD`.

So:

```bash
git reset --soft HEAD~1
```

means:

> Move `HEAD` back by one commit while keeping the changes staged.

Similarly:

```bash
git reset --hard HEAD~2
```

moves back two commits and discards the changes associated with those commits from the working tree.

---

# 6. Summary of Removing Commits

| Command                    | Commit removed? | Changes kept? | Changes staged? |
| -------------------------- | --------------: | ------------: | --------------: |
| `git reset --soft HEAD~1`  |             Yes |           Yes |             Yes |
| `git reset --mixed HEAD~1` |             Yes |           Yes |              No |
| `git reset --hard HEAD~1`  |             Yes |            No |              No |

### Easy way to remember

```text
--soft
Commit removed
Changes kept
Changes staged

--mixed
Commit removed
Changes kept
Changes unstaged

--hard
Commit removed
Changes deleted
```

---

# Complete Workflow

```bash
# View history
git log --oneline

# Make a change
echo "New information" >> README.md

# Stage
git add README.md

# Commit
git commit -m "Add new information"

# View history
git log --oneline

# Remove latest commit but keep changes staged
git reset --soft HEAD~1

# Check status
git status
```

The key concepts are:

```text
Working Directory
       │
    git add
       ▼
Staging Area
       │
  git commit
       ▼
Commit History
       │
   git log
       │
       ▼
View History
```

And when correcting the latest commit:

```text
Commit History
      │
      │ git reset
      ▼
Previous Commit
```
