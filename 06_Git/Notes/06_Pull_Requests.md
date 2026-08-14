# Pull Requests

## 1. What is a Pull Request?

### Definition

A **Pull Request (PR)** is a request to merge changes from one branch into another branch in a remote Git repository.

A Pull Request is primarily a **GitHub feature**, not a Git command.

Typical workflow:

```text
Developer
   ↓
Create Feature Branch
   ↓
Make Changes
   ↓
Commit
   ↓
Push Branch to GitHub
   ↓
Create Pull Request
   ↓
Code Review
   ↓
Approval
   ↓
Merge
   ↓
main
```

---

# 2. Why Do We Use Pull Requests?

Pull Requests are used to safely introduce changes into important branches such as `main`.

Without a PR:

```text
Developer
    ↓
Changes
    ↓
git push main
    ↓
Production Branch
```

With a PR:

```text
Developer
    ↓
Feature Branch
    ↓
Pull Request
    ↓
Code Review
    ↓
Tests / CI
    ↓
Approval
    ↓
Merge
    ↓
main
```

This gives the team an opportunity to review the code before it becomes part of the main codebase.

### Main uses

* Code review
* Collaboration
* Discussion
* Automated testing
* Quality control
* Reviewing changes before merging
* Maintaining a stable `main` branch

---

# 3. Pull Request vs Git Pull

These are **different concepts**.

### Pull Request

A GitHub collaboration mechanism:

```text
feature branch
      ↓
Pull Request
      ↓
main
```

### `git pull`

A Git command used to retrieve and integrate changes from a remote repository.

```bash
git pull
```

So:

```text
Pull Request ≠ git pull
```

The word "pull" causes confusion, but they are unrelated operations.

---

# 4. Typical Pull Request Workflow

Suppose your team has:

```text
main
```

You need to develop a login feature.

Create:

```text
feature/login
```

Workflow:

```text
main
  │
  └── feature/login
          │
          ├── Login UI
          ├── Authentication
          └── Validation
```

After completing the feature:

```bash
git add .
git commit -m "Add login feature"
git push -u origin feature/login
```

Then create a Pull Request on GitHub:

```text
feature/login
      ↓
Pull Request
      ↓
main
```

---

# 5. Creating a Feature Branch

Start from `main`:

```bash
git switch main
```

Get the latest changes:

```bash
git pull origin main
```

Create a feature branch:

```bash
git switch -c feature/login
```

Check:

```bash
git branch
```

Output:

```text
* feature/login
  main
```

---

# 6. Making Changes

Suppose you modify:

```text
login.html
login.css
login.js
```

Check:

```bash
git status
```

Stage:

```bash
git add .
```

Commit:

```bash
git commit -m "Add login functionality"
```

Now your local history contains:

```text
main
  │
  B
   \
    C ← feature/login
```

---

# 7. Push the Branch to GitHub

The feature branch exists locally.

Push it to GitHub:

```bash
git push -u origin feature/login
```

Now:

```text
Local Repository
       │
       │ git push
       ▼
GitHub
│
├── main
└── feature/login
```

The `-u` option establishes the upstream relationship.

After that, you can normally use:

```bash
git push
```

---

# 8. Creating a Pull Request on GitHub

After pushing your branch, go to the repository on GitHub.

GitHub will usually provide an option such as:

```text
Compare & pull request
```

Click it.

You will select:

```text
base:   main
compare: feature/login
```

Meaning:

> Merge the changes from `feature/login` into `main`.

The direction is important:

```text
feature/login
      │
      │ Pull Request
      ▼
     main
```

---

# 9. Base Branch vs Compare Branch

This is important when creating PRs.

### Base branch

The branch that will **receive the changes**.

Example:

```text
base: main
```

### Compare branch

The branch containing the **changes**.

Example:

```text
compare: feature/login
```

Therefore:

```text
compare branch
     │
     │ changes
     ▼
base branch
```

Example:

```text
feature/login ───────→ main
     compare           base
```

---

# 10. Pull Request Title

The title should clearly describe the change.

Good:

```text
Add user authentication
```

Good:

```text
Fix payment calculation bug
```

Bad:

```text
Changes
```

Bad:

```text
Update
```

The title should allow someone to understand the purpose of the PR quickly.

---

# 11. Pull Request Description

The description explains:

* What was changed?
* Why was it changed?
* How was it implemented?
* How was it tested?
* Are there any known limitations?

Example structure:

```text
## What changed?

Added user login functionality.

## Why?

Users need to authenticate before accessing the dashboard.

## Changes

- Added login form
- Added authentication API
- Added validation
- Added error handling

## Testing

- Tested valid credentials
- Tested invalid credentials
- Tested empty fields
```

---

# 12. Code Review

One of the most important purposes of a Pull Request is **code review**.

A reviewer examines:

```text
Code
 ↓
Logic
 ↓
Architecture
 ↓
Security
 ↓
Performance
 ↓
Maintainability
 ↓
Tests
```

A reviewer can leave comments on specific lines.

For example:

```text
Reviewer:
Can we extract this logic into a separate function?
```

The developer can modify the code and push another commit:

```bash
git add .
git commit -m "Refactor authentication logic"
git push
```

The existing Pull Request automatically updates.

```text
Pull Request
     │
     ├── Commit 1
     ├── Commit 2
     └── Commit 3
```

You **do not need to create another PR** for every new commit to the same branch.

---

# 13. Approving a Pull Request

After reviewing the code, a reviewer may:

```text
Approve
```

or request changes:

```text
Request changes
```

or simply leave comments.

A typical workflow:

```text
Developer creates PR
        ↓
Reviewer reviews
        ↓
   ┌────┴────┐
   ↓         ↓
Approve   Changes needed
   ↓         ↓
Merge      Developer fixes
             ↓
          git push
             ↓
          Review again
```

---

# 14. What Happens When Changes Are Requested?

Suppose the reviewer says:

> Add tests for the authentication logic.

You make the changes locally:

```bash
git switch feature/login
```

Add tests.

Then:

```bash
git add .
git commit -m "Add authentication tests"
git push
```

GitHub automatically updates the existing Pull Request.

```text
Existing PR
     │
     ├── Original changes
     └── New test changes
```

The reviewer can review the new changes.

---

# 15. Merge a Pull Request

Once the PR is approved and required checks pass, it can be merged.

GitHub provides merge options depending on repository settings.

Conceptually:

```text
feature/login
      │
      │ Merge
      ▼
     main
```

After merging:

```text
main
 │
 ├── Existing commits
 │
 └── Login feature
```

---

# 16. Types of Merge

GitHub commonly provides three merge strategies.

## 16.1 Create a Merge Commit

History may look like:

```text
       C ─── D
      /       \
A ─── B       M
      \       /
       ──────
```

`M` is the merge commit.

---

## 16.2 Squash and Merge

Multiple feature commits are combined into a single commit.

Before:

```text
feature/login

C1 → C2 → C3
```

After:

```text
main

C
```

This produces a cleaner main branch history.

Example:

```text
Add login feature
```

instead of:

```text
Fix login
Fix login again
Fix typo
Final fix
Update
```

---

## 16.3 Rebase and Merge

The feature commits are replayed onto the latest base branch.

Conceptually:

```text
Before:

A ─── B ─── C
      \
       D ─── E
```

After rebasing:

```text
A ─── B ─── C ─── D' ─── E'
```

The commits get new commit IDs because their history has been rewritten.

---

# 17. Updating Your Feature Branch Before Creating/Merging a PR

Suppose another developer has pushed changes to `main`.

Your branch:

```text
main
A ─── B ─── C
```

Remote `main`:

```text
A ─── B ─── C ─── D
```

Update your local `main`:

```bash
git switch main
git pull origin main
```

Then switch back:

```bash
git switch feature/login
```

You can merge the updated `main`:

```bash
git merge main
```

Or, if your team uses rebase:

```bash
git rebase main
```

Then push your updated feature branch.

With rebase, you may need:

```bash
git push --force-with-lease
```

Use force-pushing carefully, especially on shared branches.

---

# 18. Pull Request Checks / CI

Modern GitHub repositories often run automated checks when a PR is opened or updated.

Example:

```text
Pull Request
     ↓
GitHub Actions
     ↓
Build
     ↓
Unit Tests
     ↓
Lint
     ↓
Security Checks
     ↓
Status
```

You might see:

```text
✓ Build
✓ Tests
✓ Lint
✗ Security Scan
```

If required checks fail, the repository may prevent merging until the problem is fixed.

---

# 19. Pull Request Review Rules

Teams can configure branch protection/rules for `main`.

For example:

```text
main
 │
 ├── Pull Request required
 ├── 1 approval required
 ├── CI tests must pass
 └── Direct push restricted
```

This prevents developers from directly pushing potentially unsafe changes into the main branch.

---

# 20. Pull Request Conversation

A PR is not only for merging code.

It can also become a discussion area.

Example:

```text
Developer:
I implemented authentication using JWT.

Reviewer:
Why did you choose JWT instead of sessions?

Developer:
The application is using a stateless API architecture.

Reviewer:
Makes sense. Please add expiration handling.

Developer:
Done.
```

This discussion becomes part of the project's development context.

---

# 21. Pull Request vs Branch vs Commit

These concepts are different.

| Concept          | Purpose                                   |
| ---------------- | ----------------------------------------- |
| **Branch**       | Separate line of development              |
| **Commit**       | Snapshot of changes                       |
| **Pull Request** | Request to merge one branch into another  |
| **Repository**   | Project + Git history                     |
| **Remote**       | Location of a repository hosted elsewhere |

Relationship:

```text
Repository
    │
    ├── main
    │
    └── feature/login
             │
             ├── Commit
             ├── Commit
             └── Commit
                    │
                    ▼
              Pull Request
                    │
                    ▼
                   main
```

---

# 22. Complete Pull Request Workflow

Here is the complete practical workflow:

### 1. Update main

```bash
git switch main
git pull origin main
```

### 2. Create feature branch

```bash
git switch -c feature/login
```

### 3. Make changes

```text
Edit files
```

### 4. Check changes

```bash
git status
```

### 5. Stage

```bash
git add .
```

### 6. Commit

```bash
git commit -m "Add login functionality"
```

### 7. Push feature branch

```bash
git push -u origin feature/login
```

### 8. Create Pull Request

On GitHub:

```text
feature/login → main
```

### 9. Review

```text
Reviewer
   ↓
Comments
   ↓
Changes
   ↓
New commit
   ↓
git push
```

### 10. CI/CD checks

```text
Build
Tests
Lint
Security
```

### 11. Approval

```text
Approved ✓
```

### 12. Merge

```text
feature/login
      ↓
     main
```

---

# 23. After the PR Is Merged

Switch back to `main`:

```bash
git switch main
```

Update it:

```bash
git pull origin main
```

Optionally delete the local feature branch:

```bash
git branch -d feature/login
```

Delete the remote branch if needed:

```bash
git push origin --delete feature/login
```

Final state:

```text
GitHub

main
 │
 ├── Existing code
 └── Login feature

feature/login
 └── Deleted after merge
```

---

# 24. Pull Request Flow in a Real Development Team

```text
              Developer
                  │
                  ▼
           Create Branch
                  │
                  ▼
          feature/payment
                  │
            Code Changes
                  │
                  ▼
               Commit
                  │
                  ▼
              git push
                  │
                  ▼
               GitHub
                  │
                  ▼
          Create Pull Request
                  │
          ┌───────┴────────┐
          ▼                ▼
      Code Review        CI/CD
          │                │
          └───────┬────────┘
                  ▼
              Approval
                  │
                  ▼
                Merge
                  │
                  ▼
                main
                  │
                  ▼
              Deployment
```

## Key Commands Used Around Pull Requests

```bash
# Update main
git switch main
git pull origin main

# Create feature branch
git switch -c feature/login

# Check changes
git status

# Stage changes
git add .

# Commit
git commit -m "Add login feature"

# Push branch
git push -u origin feature/login

# Update feature branch with main
git merge main

# Push additional PR changes
git push

# Delete local branch after merge
git branch -d feature/login

# Delete remote branch
git push origin --delete feature/login
```

### The most important concept

```text
Branch
   ↓
Work independently
   ↓
Commit
   ↓
Push branch
   ↓
Pull Request
   ↓
Review + CI
   ↓
Approval
   ↓
Merge
   ↓
main
```

A **Pull Request is therefore the controlled collaboration mechanism between a developer's branch and a target branch**, usually `main`.
