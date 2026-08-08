# Linux Commands

```text
ls - The most frequently used command in Linux to list directories
pwd - Print working directory command in Linux
cd - Linux command to navigate through directories
mkdir - Command used to create directories in Linux
mv - Move or rename files in Linux
cp - Similar usage as mv but for copying files in Linux
rm - Delete files or directories
touch - Create blank/empty files
ln - Create symbolic links (shortcuts) to other files
cat - Display file contents on the terminal
clear - Clear the terminal display
echo - Print any text that follows the command
man - Access manual pages for all Linux commands
uname - Linux command to get basic information about the OS
whoami - Get the active username
tar - Command to extract and compress files in Linux
grep - Search for a string within an output
head - Return the specified number of lines from the top
tail - Return the specified number of lines from the bottom
export - Export environment variables in Linux
zip - Zip files in Linux
unzip - Unzip files in Linux
ssh - Secure Shell command in Linux
service - Linux command to start and stop services
ps - Display active processes
kill and killall - Kill active processes by process ID or name
df - Display disk filesystem information
chmod - Command to change file permissions
ifconfig - Display network interfaces and IP addresses
wget - Direct download files from the internet
ufw - Firewall command
apt, pacman, yum, rpm - Package managers depending on the distro
sudo - Command to escalate privileges in Linux
alias - Create custom shortcuts for your regularly used commands
whereis - Locate the binary, source, and manual pages for a command
whatis - Find what a command is used for
top - View active processes live with their system usage
```


# Linux Commands — Quick Notes

These are some of the most commonly used Linux commands, especially useful for **DevOps, Cloud, and System Administration**.

---

## 1. `ls` — List Files and Directories

Lists files and directories in the current location.

```bash
ls
```

Useful options:

```bash
ls -l      # Detailed information
ls -a      # Show hidden files
ls -la     # Detailed + hidden files
ls -lh     # Human-readable sizes
```

---

## 2. `pwd` — Print Working Directory

Shows the **absolute path** of your current directory.

```bash
pwd
```

Example:

```text
/home/arun/projects
```

---

## 3. `cd` — Change Directory

Used to move between directories.

```bash
cd projects
```

Go one level up:

```bash
cd ..
```

Go to home directory:

```bash
cd ~
```

Go to the previous directory:

```bash
cd -
```

---

## 4. `mkdir` — Make Directory

Creates a new directory.

```bash
mkdir projects
```

Create nested directories:

```bash
mkdir -p projects/devops/linux
```

---

## 5. `mv` — Move / Rename

Move a file:

```bash
mv file.txt documents/
```

Rename a file:

```bash
mv old.txt new.txt
```

---

## 6. `cp` — Copy

Copies files or directories.

```bash
cp file.txt backup.txt
```

Copy a directory:

```bash
cp -r project backup/
```

---

## 7. `rm` — Remove

Deletes files or directories.

```bash
rm file.txt
```

Delete a directory:

```bash
rm -r project/
```

Force deletion:

```bash
rm -rf project/
```

⚠️ `rm -rf` is powerful and can permanently delete files. Use it carefully.

---

## 8. `touch` — Create Empty File

Creates a blank file.

```bash
touch app.py
```

It can also update the file's timestamp if the file already exists.

---

## 9. `ln` — Create Links

Creates links between files.

### Symbolic Link

```bash
ln -s /var/www/html website
```

Here `website` acts like a shortcut pointing to `/var/www/html`.

---

## 10. `cat` — Display File Contents

Displays the contents of a file.

```bash
cat file.txt
```

You can also combine files:

```bash
cat file1.txt file2.txt
```

---

## 11. `clear` — Clear Terminal

Clears the visible terminal screen.

```bash
clear
```

Shortcut:

```text
Ctrl + L
```

---

## 12. `echo` — Print Text

Prints text to the terminal.

```bash
echo "Hello Linux"
```

It is also commonly used with variables:

```bash
name="Arun"
echo $name
```

---

## 13. `man` — Manual

Displays the manual/help page for a command.

```bash
man ls
```

For example:

```bash
man chmod
```

Press `q` to exit.

---

## 14. `uname` — System Information

Displays information about the operating system/kernel.

```bash
uname
```

More detailed information:

```bash
uname -a
```

---

## 15. `whoami` — Current User

Displays the username of the currently logged-in user.

```bash
whoami
```

Example:

```text
arun
```

---

## 16. `tar` — Archive Files

Used to create and extract archive files.

Create a `.tar` archive:

```bash
tar -cvf backup.tar project/
```

Extract:

```bash
tar -xvf backup.tar
```

Create compressed `.tar.gz`:

```bash
tar -czvf backup.tar.gz project/
```

Extract:

```bash
tar -xzvf backup.tar.gz
```

Common options:

```text
c → create
x → extract
v → verbose
f → file
z → gzip
```

---

## 17. `grep` — Search Text

Searches for a specific string in text.

```bash
grep "error" logfile.txt
```

Case-insensitive search:

```bash
grep -i "error" logfile.txt
```

It becomes very powerful with pipes:

```bash
ps aux | grep nginx
```

---

## 18. `head` — First Lines

Displays the beginning of a file.

```bash
head file.txt
```

Show first 5 lines:

```bash
head -n 5 file.txt
```

---

## 19. `tail` — Last Lines

Displays the end of a file.

```bash
tail file.txt
```

Show last 5 lines:

```bash
tail -n 5 file.txt
```

Very useful for monitoring logs:

```bash
tail -f app.log
```

`-f` continuously watches the file for new content.

---

## 20. `export` — Environment Variables

Creates an environment variable available to processes launched from the current shell.

```bash
export APP_ENV=production
```

Check it:

```bash
echo $APP_ENV
```

This is commonly used for configuration and secrets handling, although sensitive secrets should generally be managed through dedicated secret-management systems.

---

## 21. `zip` — Compress Files

Creates a ZIP archive.

```bash
zip backup.zip file.txt
```

Zip a directory:

```bash
zip -r backup.zip project/
```

---

## 22. `unzip` — Extract ZIP Files

Extracts a ZIP archive.

```bash
unzip backup.zip
```

Extract to a specific directory:

```bash
unzip backup.zip -d backup/
```

---

## 23. `ssh` — Secure Shell

Used to securely connect to a remote Linux machine.

```bash
ssh username@server-ip
```

Example:

```bash
ssh ubuntu@192.168.1.10
```

This is extremely important in **AWS and DevOps**, where you frequently connect to remote servers.

---

## 24. `service` — Manage Services

Used on some Linux systems to start, stop, restart, or check services.

```bash
sudo service nginx start
```

```bash
sudo service nginx stop
```

```bash
sudo service nginx restart
```

On modern Linux distributions, `systemctl` is generally preferred:

```bash
sudo systemctl start nginx
```

---

## 25. `ps` — View Processes

Displays currently running processes.

```bash
ps
```

Common:

```bash
ps aux
```

This gives a more detailed list of running processes.

---

## 26. `kill` — Terminate Process

Terminates a process using its **PID (Process ID)**.

```bash
kill 1234
```

Force termination:

```bash
kill -9 1234
```

`SIGKILL` should generally be used only when a normal termination does not work.

---

## 27. `killall` — Kill by Process Name

Terminates processes by name.

```bash
killall nginx
```

Use carefully because it can affect multiple processes with the same name.

---

## 28. `df` — Disk Usage

Shows filesystem disk usage.

```bash
df
```

Human-readable format:

```bash
df -h
```

Example:

```text
Filesystem   Size   Used   Avail   Use%
/dev/sda1     50G    20G     28G    42%
```

---

## 29. `chmod` — Change Permissions

Changes file or directory permissions.

```bash
chmod 755 script.sh
```

Common permissions:

```text
r = read
w = write
x = execute
```

Example:

```bash
chmod +x script.sh
```

Makes the script executable.

---

## 30. `ifconfig` — Network Information

Displays network interfaces and IP information.

```bash
ifconfig
```

However, `ifconfig` is considered legacy on many modern Linux distributions.

Use:

```bash
ip addr
```

instead.

---

## 31. `wget` — Download Files

Downloads files from the Internet.

```bash
wget https://example.com/file.zip
```

Useful for downloading packages, scripts, and resources from a URL.

---

## 32. `ufw` — Uncomplicated Firewall

A simple firewall management tool commonly used on Ubuntu.

Check status:

```bash
sudo ufw status
```

Allow SSH:

```bash
sudo ufw allow 22
```

Allow HTTP:

```bash
sudo ufw allow 80
```

Enable firewall:

```bash
sudo ufw enable
```

---

# 33. Package Managers

Package managers install, update, and remove software.

### Ubuntu / Debian

```bash
sudo apt update
sudo apt install nginx
```

### RHEL / Fedora

Modern RHEL/Fedora systems commonly use:

```bash
sudo dnf install nginx
```

Older systems may use:

```bash
sudo yum install nginx
```

### Arch Linux

```bash
sudo pacman -S nginx
```

### RPM

`rpm` is a low-level package management tool for RPM packages:

```bash
rpm -qa
```

---

## 34. `sudo` — Superuser Privileges

Runs a command with elevated privileges.

```bash
sudo apt update
```

For example, installing software generally requires administrator privileges.

---

## 35. `alias` — Create Command Shortcuts

Creates a shortcut for a command.

```bash
alias ll="ls -la"
```

Now:

```bash
ll
```

runs:

```bash
ls -la
```

To see aliases:

```bash
alias
```

---

## 36. `whereis` — Locate Command Files

Shows locations related to a command, such as its binary and manual page.

```bash
whereis python
```

Example output may include:

```text
python: /usr/bin/python /usr/share/man/...
```

---

## 37. `whatis` — Command Description

Provides a short description of a command.

```bash
whatis ls
```

Example:

```text
ls - list directory contents
```

---

## 38. `top` — Live Process Monitoring

Displays running processes and system resource usage in real time.

```bash
top
```

It can show:

* CPU usage
* Memory usage
* Running processes
* Process IDs
* System load

Press:

```text
q
```

to exit.

---

# Quick Revision

| Command                  | Purpose                   |
| ------------------------ | ------------------------- |
| `ls`                     | List files/directories    |
| `pwd`                    | Show current directory    |
| `cd`                     | Navigate directories      |
| `mkdir`                  | Create directory          |
| `mv`                     | Move/rename               |
| `cp`                     | Copy                      |
| `rm`                     | Delete                    |
| `touch`                  | Create file               |
| `ln`                     | Create links              |
| `cat`                    | Read file                 |
| `clear`                  | Clear terminal            |
| `echo`                   | Print text                |
| `man`                    | Manual/help               |
| `uname`                  | System information        |
| `whoami`                 | Current user              |
| `tar`                    | Archive/extract           |
| `grep`                   | Search text               |
| `head`                   | First lines               |
| `tail`                   | Last lines                |
| `export`                 | Set environment variable  |
| `zip`                    | Create ZIP                |
| `unzip`                  | Extract ZIP               |
| `ssh`                    | Remote connection         |
| `systemctl` / `service`  | Manage services           |
| `ps`                     | View processes            |
| `kill`                   | Kill process              |
| `df`                     | Disk usage                |
| `chmod`                  | Change permissions        |
| `ip`                     | Network information       |
| `wget`                   | Download files            |
| `ufw`                    | Manage firewall           |
| `apt` / `dnf` / `pacman` | Package management        |
| `sudo`                   | Run as administrator      |
| `alias`                  | Command shortcut          |
| `whereis`                | Locate command files      |
| `whatis`                 | Short command description |
| `top`                    | Live process monitoring   |
