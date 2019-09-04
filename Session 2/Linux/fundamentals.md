# Linux Fundamentals

## Common Directories
- `/`: root
  - `/bin`: binary or other executalbe programs
  - `/etc`: system configuration files
  - `/home`: home directories
    - `user_name`
      - Documents
      - Downloads
      - Music
      - ...
  - `/opt`: optional or third party softwares
  - `/tmp`: temporary space, typically cleared on reboot
  - `/usr`: user related programs
  - `/var`: variable data, most notably log files
    - `log`
  - `/boot`: files needed to boot the operating system
  - `/cdrom`: mount point for CD-ROMs
  - `/dev`: device files, typically controlled by the operating system and the system administrators.
  - `/lib`: system libraries
  - `/lib64`: system libraries, 64 bit
  - `/lost+found`: Used by the file system to store recovered files after a file system check has been performed.
  - `/media`: Used to mount removable media like CD-ROMs
  - `/mnt`: used to mount external file systems.

## Application Directory Structures
- `/usr/local/application/bin`
- `/usr/local/application/etc`
- `/usr/local/application/lib`
- `/usr/local/application/log`

- `/opt/application/bin`
- `/opt/application/etc`
- `/opt/application/lib`
- `/opt/application/log`

Applications that are not part of the base OS can be installed in:
- `/usr/local`
- `/opt`

## Tilde Expansion

- `~user`: `/home/user`
- `~root`: `/root`
- `~ftp`: `/srv/ftp`

## Multiple line prompt
```
git commit -m "line 1
line 2
line 3
line 4"
```

## Basic Linux Commands
- `ls`
  - `ls -l`: `-rw-rw-r-- 1 jason users 10400 Sep 27 08:52 sales.data`
    - `-rw-rw-r--`: permissions
    - 1: number of links
    - `jason`: owner name
    - `users`: group name
    - 10400: number of bytes in the file
    - Sep 27 08:52: last modification time
    - sales.data: file name
  - `ls -a`: listing all files including hidden files
    - hiden files begin with a period (`.git` for example)
  - `ls -F`: listing files by type
    - `/`: Directory
    - `@`: Link
    - `*`: Executable
  - `ls -t`: list files by time
  - `ls -r`: reverse order
  - `ls -l -a` or `ls -la` or `ls -al`: combine options
- `tree`: similar to `ls`, but creates visual output
  - `tree -d`: list directories only
- `cd`
- `pwd`
- `cat`: concatenates and displays files
- `echo`: displays arguments to the screen
- `man`: displays the online manual
  - `man -k SEARCH_TERM`: searching man pages
- `exit`: exits the shell or your current session
- `clear`: clears the screen
- `reset`: resets the shell or your current session
- `which`: locate a command
- `groups`: displays a user's groups


## Permissions
```bash
$ ls -l
-rw-rw-r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

The 1st character:
|Symbol|Type|
|--|--|
|`-`|regular file|
|`d`|directory|
|`|`|symbolic link|

The 2nd character:
|Symbol|Permission|
|--|--|
|`r`|read|
|`w`|write|
|`x`|execute|

### Permission Categories
|Symbol|Category|
|--|--|
|`u`|User|
|`g`|Group|
|`o`|Other|
|`a`|All|

### Groups
- Every user is in at least one group
- Users belong to many groups
- Groups are used to organize users
- The `groups` command displays a user's groups

### Secret Decoder Ring
`-[type]rw-[user]r--[group]r--[other]`

[type]: directory type
[user]: permissions available to the user
[group]: permissions available to the group
[other]: permissions available to all users

### Change Permissions
- `chmod`: change mode command
- `ugoa`: user category (user, group, other, all)
- `+-=`: add, subtract, or set permissions
- `rwx`: read write, execute

```bash
$ ls -l sales.data
-rw-r--r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

```bash
$ chmod g+w sales.data
$ ls -l sales.data
-rw-rw-r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

```bash
$ chmod g+w sales.data
$ ls -l sales.data
-rw-r--r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

```bash
$ chmod u+rwx,g-r sales.data
$ ls -l sales.data
-rwx---r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

```bash
$ chmod a=r sales.data
$ ls -l sales.data
-r--r--r-- 1 jason users 10400 Sep 27 08:52 sales.data
```

if you don't specify anything after `=`, all permissions are removed

```bash
$ chmod o= sales.data
$ ls -l sales.data
-r--r----- 1 jason users 10400 Sep 27 08:52 sales.data
```

### Numeric Based Permissions
|r|w|x||
|--|--|--|--|
|0|0|0|Value for off|
|1|1|1|Binary value for on|
|4|2|1|Base 10 value for on|

|Octal|Binary|String|Description|
|--|--|--|--|
|0|0|`---`|no permissions|
|1|1|`--x`|execute only|
|2|01|`-w-`|write only|
|3|11|`-wx`|write and execute (2+1)|
|4|100|`r--`|read only|
|5|101|`r-x`|read and execute (4+1)|
|6|110|`rw-`|read and write (4+2)|
|7|111|`rwx`|read, write, and execute (4+2+1)|

Note: in permission order has meaning! read, write, and then execute.

||U|G|O|
|--|--|--|--|
|Symbolic|`rwx`|`r-x`|`r--`|
|Binary|111|101|100|
|Decimal|7|5|4|

### Commonly Used Permissions

|Symbolic|Octal||
|--|--|--|
|`-rwx------`|700|ensure that the file can be read, edited, and executed by the owner, but no one else|
|`-rwxr-xr-x`|755|allows everyone to execute the file, but only the user can edit|
|`-rw-rw-r--`|664|allows a group of people to modify a file and let others read it|
|`-rw-rw----`|660|allows a group of people to modify a file and NOT let others read it|
|`rw-r--r--`|644|allows everyone on the system to read the file, but only the user can edit|

Notes:
- for 777 (gives full permission) and 666, always ask if there is a better way to do that
- 777 gives full permission, anyone can make changes to the script or program and execute it. so if mallicious code was either inserted on purpose or by accident, it can cause trouble.
- if multiple people need access, consider creating a group and limit access to that group.

### Change Group
`chgrp group_name file_name`

```bash
$ ls -l sales.data
-r--r--r-- 1 jason users 10400 Sep 27 08:52 sales.data

$ chgrp sudo sales.data
$ chmod g+w sales.data
$ ls -l sales.data
-r--rw-r-- 1 jason sudo 10400 Sep 27 08:52 sales.data
```

## Working with Spaces in Names
- Just say no to spaces!
- Alternatives:
  - Hyphens ( - )
  - Underscore (_)
  - CamelCase
- Encapsulate the entire file name in quotes
- Use a backslash `\` to escape spaces

## symbolic links
- a link is a point to the actual file or directory
- use the link as if it were the file
- a link can be used to create a shortcut
  - use for long file or directory names
  - use to indicate the current version of software

## Navigating man Pages
- Enter: move down one line
- Space: move down one page
- g: Move to the top of the page
- G: move to the bottom of the page
- q: Quit
