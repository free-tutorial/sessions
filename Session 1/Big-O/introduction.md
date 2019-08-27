# Big-O

## Time Complexity

### File Transfer Problem
Problem: how to transfer a file?
1. plane: O(1)
2. email: O(s)


### Common Big-Os
- O(1)
- O(Log N)
- O(N)
- O(N Log N)
- O(N^2)
- O(2^N)


### Examples

```java
void printUnorderedPairs(int[] arrayA, int[] arrayB){
    for (int i = 0; i < arrayA.length; i++){
        for (int j = 0; j < arrayB.length; j++){
            /* O(1) work here */
        }
    }
}
```

```java
void printUnorderedPairs(int[] arrayA, int[] arrayB){
    for (int i = 0; i < arrayA.length; i++){
        for (int j = 0; j < arrayB.length; j++){
            for (int k = 0; k <= 100; k++){
                /* O(1) work here */
            }
        }
    }
}
```


```java
int sum(Node node){
    if (node == null) {
        return 0;
    }
    return sum(node.left) + node.value + sum(node.right);
}
```