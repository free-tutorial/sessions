# Git

## Why Source Control
You can think of a version control system (short: "VCS") as a kind of "database". It lets you save a snapshot of your complete project at any time you want. When you later take a look at an older snapshot (let's start calling it "version"), your VCS shows you exactly how it differed from the previous one.

![git](git.png =400x)

- It works just as well for an HTML website as it does for a design project or an iPhone app
- It lets you work with any tool you like; it doesn't care what kind of text editor, graphics program, file manager or other tool you use

A version control system records the changes you make to your project's files. This is what version control is about.

Why use version control system:
1. Collaboration
2. Storing Versions (Properly)
   1. How much do you save? Only the changed files or the complete project?
   2. How do you name these versions?
   3. How do you know what exactly is different in these versions?
3. Restoring Previous Versions
4. Understanding What Happened
5. Backup

## What is version control? Centralized vs. DVCS

### Centralized Version Control

Centralized version control systems are based on the idea that there is a single “central” copy of your project somewhere (probably on a server), and programmers will “commit” their changes to this central copy.

With Centralized version control, programmers no longer have to keep many copies of files on their hard drives manually, because the version control tool can talk to the central copy and retrieve any version they need on the fly.

Note: In centralized version control, programmer needs connection to central server for most operations.

#### A Typical Centralized Version Control Workflow
When you’re working with a centralized verison control system, your workflow for adding a new feature or fixing a bug in your project will usually look something like this:

Pull down any changes other people have made from the central server.
Make your changes, and make sure they work properly.
Commit your changes to the central server, so other programmers can see them.

### Distributed Version Control

These systems do not necessarily rely on a central server to store all the versions of a project’s files. Instead, every developer “clones” a copy of a repository and has the full history of the project on their own hard drive. This copy (or “clone”) has all of the metadata of the original.

This method may sound wasteful, but in practice, it’s not a problem. Most programming projects consist mostly of plain text files (and maybe a few images), and disk space is so cheap that storing many copies of a file doesn’t create a noticable dent in a hard drive’s free space. Modern systems also compress the files to use even less space.

One common misconception about distributed version control systems is that there cannot be a central project repository. This is simply not true – there is nothing stopping you from saying “this copy of the project is the authoritative one.” This means that instead of a central repository being required by the tools you use, it is now optional and purely a social issue.

Note:
- Most operations are local
- Central server is not required

## What is Git?
- Distributed source control system
  - Not required to be decentralized
- Massively scales
- Open source
- Developed for Linux project requirements
- Most operations are local

## References
- https://www.git-tower.com/learn/git/ebook/en/desktop-gui/basics/what-is-version-control#start
- https://www.atlassian.com/blog/software-teams/version-control-centralized-dvcs

