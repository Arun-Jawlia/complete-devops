# Git Stashing

## 1. What is Git Stash?

### Definition

**Git Stash temporarily saves your uncommitted changes and cleans your working directory.**

It is useful when you are working on something but suddenly need to switch to another branch without committing your incomplete work.

### Example

You are working on:

```text
feature/login
```

You have modified:

```text
login.html
login.js
```

But your work is incomplete.

Suddenly, you need to switch to `main` to fix an urgent bug.

Instead of making an unnecessary commit:

```text
WIP: login changes
```

you can stash your changes:

```bash
git stash
```

Your working directory becomes clean.

```text
Before stash:

Working Directory
├── login.html  ← modified
└── login.js    ← modified

        ↓ git stash

Working Directory
└── clean
```

Your changes are stored by Git and can be restored later.

---

# 2. Why Do We Use Stashing?

Stashing is useful when:

* You have unfinished work.
* You need to switch branches.
* You need to pull or merge changes.
* You need to quickly fix another issue.
* You don't want to create a temporary commit.
* You want to temporarily clean your working directory.

### Typical scenario

```text
Working on feature/login
        ↓
Unfinished changes
        ↓
Urgent bug on main
        ↓
git stash
        ↓
Switch to main
        ↓
Fix bug
        ↓
Switch back to feature/login
        ↓
git stash pop
        ↓
Continue work
```

---

# 3. Basic `git stash`

Check your changes:

```bash
git status
```

Example:

```text
Changes not staged for commit:
    modified: login.js
```

Stash the changes:

```bash
git stash
```

or:

```bash
git stash push
```

Check status:

```bash
git status
```

Now:

```text
nothing to commit, working tree clean
```

Your changes have been temporarily stored.

---

# 4. View Stashes

To see your saved stashes:

```bash
git stash list
```

Example:

```text
stash@{0}: WIP on feature/login
stash@{1}: WIP on feature/payment
stash@{2}: WIP on main
```

Each stash has an identifier:

```text
stash@{0}
stash@{1}
stash@{2}
```

The most recent stash is normally:

```text
stash@{0}
```

---

# 5. Adding a Message to a Stash

Instead of creating an unnamed stash:

```bash
git stash
```

you can provide a meaningful message:

```bash
git stash push -m "Login page changes"
```

Check:

```bash
git stash list
```

Example:

```text
stash@{0}: On feature/login: Login page changes
```

This is useful when you have multiple stashes.

---

# 6. Restoring Stashed Changes

There are two common commands:

```bash
git stash apply
```

and:

```bash
git stash pop
```

Both restore stashed changes, but they behave differently.

---

# 7. `git stash apply`

### Definition

`git stash apply` restores the changes **but keeps the stash** in the stash list.

Example:

```bash
git stash apply
```

Before:

```text
stash list
stash@{0}
```

After:

```text
Working Directory
       ↑
   changes restored

stash list
stash@{0}  ← still exists
```

Check:

```bash
git stash list
```

The stash is still there.

---

# 8. `git stash pop`

### Definition

`git stash pop` restores the changes and **removes the stash from the stash list** if the application succeeds.

```bash
git stash pop
```

Conceptually:

```text
Stash
  │
  │ git stash pop
  ▼
Working Directory

Stash entry removed
```

### Difference

```text
git stash apply
    ↓
Restore changes
    ↓
Keep stash


git stash pop
    ↓
Restore changes
    ↓
Remove stash
```

---

# 9. Apply a Specific Stash

Suppose:

```bash
git stash list
```

shows:

```text
stash@{0}: Login changes
stash@{1}: Payment changes
stash@{2}: Dashboard changes
```

To apply the payment changes:

```bash
git stash apply stash@{1}
```

To pop that specific stash:

```bash
git stash pop stash@{1}
```

---

# 10. Stashing Staged and Unstaged Changes

Suppose you have:

```text
README.md     → staged
login.js      → unstaged
```

Normally:

```bash
git stash
```

stashes the working changes while preserving the appropriate index state behavior.

If you explicitly want to stash staged changes as well:

```bash
git stash push --staged
```

This is useful when you want to temporarily put **staged changes** away too.

---

# 11. Stashing Untracked Files

By default, `git stash` does not include untracked files.

Example:

```text
git status

modified: login.js
untracked: test.js
```

Run:

```bash
git stash
```

The modified file is stashed, but the untracked file remains.

To include untracked files:

```bash
git stash -u
```

or:

```bash
git stash --include-untracked
```

Now both tracked modifications and untracked files are stashed.

---

# 12. Stashing Everything Including Ignored Files

Sometimes you also want to stash ignored files.

Use:

```bash
git stash -a
```

or:

```bash
git stash --all
```

This can include:

* Tracked files
* Untracked files
* Ignored files

Be careful with this because ignored files may include generated files, build artifacts, or environment-specific files.

---

# 13. Stash Only Specific Files

You don't always have to stash everything.

For example:

```text
README.md
login.js
payment.js
```

You only want to stash `login.js`.

Use:

```bash
git stash push -m "Login work" -- login.js
```

Now only the specified path is included.

---

# 14. Viewing Stash Contents

To inspect what a stash contains:

```bash
git stash show
```

For a summary:

```text
 login.js | 10 +++++++---
```

To see the complete diff:

```bash
git stash show -p
```

or:

```bash
git stash show --patch
```

This lets you inspect the actual changes stored inside the stash.

---

# 15. Deleting a Stash

If you no longer need a particular stash:

```bash
git stash drop stash@{0}
```

Example:

```text
stash@{0}: Login changes
```

Run:

```bash
git stash drop stash@{0}
```

That stash is removed.

---

# 16. Delete All Stashes

To remove every stash:

```bash
git stash clear
```

After:

```bash
git stash list
```

you should see no stash entries.

### Important

`git stash clear` permanently removes all stash entries.

Use it carefully.

---

# 17. Stashing While Switching Branches

This is one of the most common real-world uses.

Suppose:

```text
feature/login
```

You have unfinished changes:

```text
login.js
login.html
```

Check:

```bash
git status
```

Stash:

```bash
git stash push -m "Incomplete login work"
```

Switch to main:

```bash
git switch main
```

Work on the urgent issue.

After completing it:

```bash
git add .
git commit -m "Fix production bug"
```

Return to your feature branch:

```bash
git switch feature/login
```

Check stashes:

```bash
git stash list
```

Restore your work:

```bash
git stash pop
```

Your unfinished login work is back.

---

# 18. Stashing Before Pulling Changes

Sometimes you have local changes:

```text
Working Directory
       │
       └── Uncommitted changes
```

and need to update your branch.

You can stash:

```bash
git stash
```

Then:

```bash
git pull origin main
```

Restore your work:

```bash
git stash pop
```

The flow is:

```text
Local Changes
     │
 git stash
     ↓
Clean Working Tree
     │
 git pull
     ↓
Latest Remote Changes
     │
git stash pop
     ↓
Your Local Changes
```

### Important

Stashing does **not** guarantee that your changes will apply cleanly after a pull or merge.

You can encounter conflicts.

---

# 19. Stash Conflicts

Suppose you stash changes from:

```text
feature/login
```

Then `main` changes the same lines.

Later:

```bash
git stash pop
```

Git may encounter a conflict.

You may see:

```text
CONFLICT (content): Merge conflict in login.js
```

Now resolve the conflict manually.

Check:

```bash
git status
```

Edit the conflicting file and resolve the conflict.

Then:

```bash
git add login.js
```

After resolving, continue your work.

---

# 20. Creating a Branch from a Stash

You can create a new branch directly from a stash:

```bash
git stash branch feature/login stash@{0}
```

This:

1. Creates a new branch
2. Switches to it
3. Applies the stash
4. Removes the stash if successfully applied

Example:

```text
stash@{0}
    │
    │ git stash branch
    ▼
feature/login
```

This is useful when you realize that your stashed work should actually belong to a different branch.

---

# 21. Stash vs Commit

These are different concepts.

| Stash                             | Commit                                |
| --------------------------------- | ------------------------------------- |
| Temporary storage                 | Permanent project history             |
| Usually for unfinished work       | Usually for completed logical changes |
| Not part of normal commit history | Part of Git history                   |
| Useful when switching context     | Used to record project progress       |
| Can be dropped                    | Can be reverted/reset                 |

### Example

Don't usually do:

```bash
git add .
git commit -m "Work in progress"
```

just because you need to switch branches.

Instead:

```bash
git stash
```

Then return later:

```bash
git stash pop
```

---

# 22. Stash Workflow

### Save work

```bash
git stash push -m "My unfinished work"
```

### View stashes

```bash
git stash list
```

### Restore but keep stash

```bash
git stash apply
```

### Restore and remove stash

```bash
git stash pop
```

### Inspect stash

```bash
git stash show -p
```

### Remove one stash

```bash
git stash drop stash@{0}
```

### Remove all stashes

```bash
git stash clear
```

---

# 23. Complete Real-World Example

You are working on a login feature:

```bash
git switch -c feature/login
```

Modify files:

```text
login.html
login.js
```

Check:

```bash
git status
```

You get an urgent request to fix a bug on `main`.

Save your incomplete work:

```bash
git stash push -m "Incomplete login feature"
```

Switch to main:

```bash
git switch main
```

Fix the bug:

```bash
git add .
git commit -m "Fix navbar bug"
```

Switch back:

```bash
git switch feature/login
```

Check your stash:

```bash
git stash list
```

Output:

```text
stash@{0}: On feature/login: Incomplete login feature
```

Restore it:

```bash
git stash pop
```

Continue development:

```text
feature/login
      │
      ├── Login UI
      ├── Authentication
      └── Validation
```

When complete:

```bash
git add .
git commit -m "Add login functionality"
git push -u origin feature/login
```

---

# 24. Important Stash Commands

| Command                       | Purpose                     |
| ----------------------------- | --------------------------- |
| `git stash`                   | Stash current changes       |
| `git stash push -m "message"` | Stash with a message        |
| `git stash list`              | List all stashes            |
| `git stash apply`             | Restore stash, keep stash   |
| `git stash pop`               | Restore stash, remove stash |
| `git stash apply stash@{1}`   | Apply specific stash        |
| `git stash show`              | Show stash summary          |
| `git stash show -p`           | Show complete stash diff    |
| `git stash -u`                | Include untracked files     |
| `git stash -a`                | Include ignored files       |
| `git stash drop`              | Delete a stash              |
| `git stash clear`             | Delete all stashes          |
| `git stash branch`            | Create branch from stash    |

### Core idea

```text
Uncommitted Work
       │
       │ git stash
       ▼
    Stash Area
       │
       │ switch branch / pull / fix issue
       ▼
   Other Work
       │
       │ return
       ▼
 git stash pop
       │
       ▼
Uncommitted Work Restored
```

**Remember:** `stash` is a **temporary parking area for uncommitted changes**. It is not a replacement for commits and is not part of the normal project commit history.
