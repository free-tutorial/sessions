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
