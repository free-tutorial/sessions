# Linux Fundamentals

## Environmental Vairables
Storage location that has a name and a value
- typically uppercase
- access the contents by executing: `echo $VAR_NAME`

For example: `$PATH` contains a list of directories and controls the command search path (when you type in a command in prompt, that command will be searched for in the directoies listed in your `PATH` environment variable)
```
/usr/local/cuda-9.0/bin:/home/ali/anaconda3/envs/chatbot/bin:/home/ali/anaconda3/condabin:/home/Jerry/library/swigtool/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

a command will be searched for first in `/usr/local/cuda-9.0/bin`, then `/home/ali/anaconda3/envs/chatbot/bin`, ...

## Get help
Get help with `--help` or `-h` (try `-h` if `--help` does not work)

For example `ls --help`

## Notes:

- Root access is typically restricted to system administrators
- Root access is required to install, start, or stop and application
- Day to day activities will be performed using a normal account.

## Directory Shortcuts
- `.`: this directory
- `..`: the parent directory
- `cd -` or `cd ..`: change to the previous directory

## Executing Commands
- `$PATH` determines command search path
- you can specify a command with a full path
- you can execute command not in `$PATH`
- `./command`: execute command in this dir

## Create and Remove Directories
- `mkdir [-p] directory`: create a directory
- `rmdir [-p] directory`: remove a directory
- `rm -rf directory`: recursively remove directory

## Find
`find [path] [expression]`

- `-name pattern`: find files and directories that match pattern
- `-iname pattern`: like `-name` but ignores case
- `-ls`: perfoms an ls on each of the found items
- ‍`-mtime days`: find files that are days oldq
- `-mmin minutes`: find files that are n minutes old
- `-size num`: find files that are size num
- `-newer file`: find files that are newer than file.
- `-exec command {} \;`: run command against all the files that are found
- `-type d`: find only directories

example:
- `find . -mtime +10 -mtime -13` find files that are more than 10 days and less than 13 days old.
- `find . -size +1M -size -2G` find files that are more than 1 MB and less than 2 GB.
- `find . -exec file {} \;`
- `find . -exec ls {} \;`

`file` command: best guess to file type and content.

## Locate
`locate pattern`

- list files that matches the pattern
- faster than the file command
- queries an index
- results are not in real time
- may not be enables on all systems.

## Display the File Contents

|Command|Description|
|--|--|
|`cat file`|display file content|
|`more file`|browse through a text file|
|`less file`|more features than more|
|`head file`|output the top portion of file|
|`tail file`|output the bottom portion of file|

Note:
1. `head` and `tail` display only 10 lines by default. change this behaviour with `-n` (`tail -5 file` will display the last 5 lines of the file content)
2. `cat` does not show file contents in real time. use `tail -f file` instead.


## Nano
`nano file`

- nano is a simple editor
- easy to learn
- not as advanced as vi or emacs

## Vi
`vi file`
`vim file`: same as `vi` with more features.
`view file`: starts `vim` in read-only mode.

- has advanced and powerful features
- not intuitive
- harder to learn than nano
- requires a time investment


## Delete, Copy, and Rename
|Command|Description|
|--|--|
|`rm file`|remove file|
|`rm -r dir`|remove directory and its content recursively|
|`rm -f file`|force removal and never prompt for confirmation|
|`cp source_file destination_file`|copy source to destination|
|`cp source_file1 [source_fileN ...] dest_dire`|copy source files to destination|
|`cp -r source dest`|copy directory and its content recursively|
|`mv source dest`|move or rename file and directories|

Note: search patterns can be used to delete multiple files (for example `ls s*`), but always check with `ls pattern` before deletion.

## Sort
|Command|Description|
|--|--|
|`sort file`|sort text in file|
|`sort -u file`|sort and return unique|
|`sort -r file`|sort in reverse order|
|`sort -k F file`|sort by key, `F` is the field number|
|`sort -ru file`|sort in reverse order and return unique|
|`sort -n file`|sort according to the numerical value|

## Disk Usage
|Command|Description|
|--|--|
|`du`|estimate file size|
|`du -k`|estimate file size in kilobytes|
|`du -h`|display sizes in human readable format|
|`du [file|file pattern]`||
|`du -s`|summarize|
|`du -m`|like `--block-size=1M`|

## `grep`
|Command|Description|
|:--|:--|
|`grep keywords file_1 file_2 ...`|print lines matching a pattern|
|`grep -i keywords file_1 file_2 ...`|ignore case|
|`grep -i keywords -r directory`|recursive search in directory|
|`grep -w keywords file_1 file_2 ...`|search for a word and avoid matching substrings|

## Commands Chain
- `du -sm * | sort -nr | head -10`
- `less file.txt | grep "search-terms"`
- `find . | grep "search-trems"`
