# Programming

## Internal Computer Programming
The CPU can be single core or multiple core.

How are the instructions processed?
1. the instruction is fetched (retrieved) from memory in an order stored in an instruction register.
2. the instruction is decoded.
3. if necessary, RAM is accessed for information.
4. the instruction is sent to the ALU (Arithmetic Logic Unit)
5. the result is processed and sent to the appropriate components, including any mathematical processing and/or IO device.


Why is this important?
- in order to give the computer instructions we want to understand how it works with instructions.
- we can write better programms when we know what we're working with (i.e. parallel programming).


## IDE
Integrated Development Environment: combines all key aspects of writing programs
- syntax highlighting
- error checking
- compiling
- executing
- file/folder management
- package/namespace management

Whu use an IDE?
- efficiency/accuracy
- shortcuts
- industry standards


## Interpreted vs Compiled
Compiled:

- programmer writes in high-level language
- code is then compiled to low-level executable: it gives machine level instructions, can run more quickly
- changes require a new compile (build)
- more efficient than interpreted
- example: C, Java

Interpreted:

- programmer writes in high-level language
- code is interpreted and executed in an interpreter.
- changes are immediately available.
- not as efficient as compiled languages.
- more portable than compiled languages (web browsers in any operating systems, tends to be more interpreted)
- example: javascript, PHP


## C++ vs Python
- memory leak
- segmentation dump
- logic errors! (better in C)
- python is slow