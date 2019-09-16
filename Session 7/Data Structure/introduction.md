# Data Structure

## Big-O

|Data Structure|Time Complexity||||||||Space Complexity|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
||Average||||Worst|||Worst|
||Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|Array|O(1)|O(n)|O(n)|O(n)|O(1)|O(n)|O(n)|O(n)|O(n)|
|Singly-Linked List|O(n)|O(n)|O(1)|O(1)|O(n)|O(n)|O(1)|O(1)|O(n)|
|Doubly-Linked List|O(n)|O(n)|O(1)|O(1)|O(n)|O(n)|O(1)|O(1)|O(n)|
|Hash Table|N/A|O(1)|O(1)|O(1)|N/A|O(n)|O(n)|O(n)|O(n)|


## Stack

A stack uses LIFO (last-in first-out) ordering. As in the stack of dinner plates, the most recent item added to the stack is the first item to be removed.

It uses the following operations:
- `pop()`: Remove the top item from the stack.
- `push()`: Add an item to the top of the stack.
- `peek()`: Return the top of the stack.
- `isEmpty()`: Return true if and only if the stack is empty.

### Stacks vs. Array
- An array is a contiguous block of memory. A stack is a first-in-last-out data structure with access only to the top of the data. In stack we lose the ability of constant-time access to the ith item. However, it allows constant time add and removes as it doesn't require shifting elements around.
- Since many languages do not provide facility for stack, it is backed by either arrays or linked list.
- In arrays, the values can be added or deleted on any side, but in stack the other side is sealed.

![array](./stack.jpg =450x)

## Queue
A queue implements FIFO (first-in first-out) ordering.

It uses the following operations:
- `add(item)`: Add an item to the end of the list.
- `remove()`: Remove the first item in the list.
- `peek()`: Return the top of the queue.
- `isEmpty()`: Return true if and only if the queue is empty.

A queue can be implemented with a linked list. In fact, they are essentially the same thing as long as items are added and removed from opposite sides.

|Data Structure|Time Complexity||||||||Space Complexity|
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
||Average||||Worst|||Worst|
||Access|Search|Insertion|Deletion|Access|Search|Insertion|Deletion|
|Stack|O(n)|O(n)|O(1)|O(1)|O(n)|O(n)|O(1)|O(1)|O(n)|
|Queue|O(n)|O(n)|O(1)|O(1)|O(n)|O(n)|O(1)|O(1)|O(n)|

## Stack & Queue in python

### the `list` Built-in

Python’s built-in list type makes a decent stack data structure as it supports push and pop operations in amortized O(1) time.

Python’s lists are implemented as dynamic arrays internally which means they occasional need to resize the storage space for elements stored in them when elements are added or removed. The list over-allocates its backing storage so that not every push or pop requires resizing and you get an amortized O(1) time complexity for these operations.

The downside is that this makes their performance less consistent than the stable O(1) inserts and deletes provided by a linked list based implementation. On the other hand lists do provide fast O(1) time random access to elements on the stack which can be an added benefit.

Here’s an important performance **caveat** when using lists as stacks:

To get the amortized O(1) performance for inserts and deletes new items must be added to the end of the list with the append() method and removed again from the end using pop(). Stacks based on Python lists grow to the right and shrink to the left.

Adding and removing from the front is much slower and takes O(n) time, as the existing elements must be shifted around to make room for the new element.

### the `collections.deque` Class

The deque class implements a double-ended queue that supports adding and removing elements from either end in O(1) time (non-amortized).

Because deques support adding and removing elements from either end equally well, they can serve both as queues and as stacks.

Python’s deque objects are implemented as doubly-linked lists which gives them excellent and consistent performance for inserting and deleting elements, but poor O(n) performance for randomly accessing elements in the middle of the stack.

