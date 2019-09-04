# Big-O

## Time Complexity

1. Fibonacci
```python
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```
2. Fibonacci in loop
```python
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(n):
    fib(n)
```

3. Cached Fibonacci
```python
def cached_fib(n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = cached_fib(n-1, memo) + cached_fib(n-2, memo)
    return memo[n]
```

## Space Complexity
1. Fibonacci
```python
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```

2. Cached Fibonacci
```python
def cached_fib(n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = cached_fib(n-1, memo) + cached_fib(n-2, memo)
    return memo[n]
```

