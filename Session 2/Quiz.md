# Quiz #1

## Questions
1. indicate hidden files:
   - [ ] ~/.bashrc
   - [ ] /home/ali
   - [ ] /home/ali/project/.git
   - [ ] /home/ali/project/.gitignore
   - [ ] /home/ali/project/setup.py

2. which command locates a command in ubuntu?
   1. `locate`
   2. `find`
   3. `which`
   4. `echo`

3. running `ls -l` on a file, will result a pattern like `-rw-rw-r-- 1 jason users 10400 Sep 27 08:52 sales.data`. What is `jason` and `users`?
4. referring to previous question, why directories space is often reported as 4096 bytes?
5. which of the following are equivalent to O(N)? why?
   - [ ] O(2N)
   - [ ] O(N + Log(N)
   - [ ] O(N + M)

6. what is time complexity?
```java
int factorial(int n){
    if (n<0){
        return -1;
    } else if (n == 0) {
        return 1;
    } else {
        return n * factorial(n -1);
    }
}
```