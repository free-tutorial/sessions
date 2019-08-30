# Exercises

# #1: Guess Number Higher or Lower
We are playing the Guess Game. The game is as follows:

1. I pick a number from 1 to n. You have to guess which number I picked.
2. Every time you guesss wrong, I'll tell you whether the number is higher or lower.

Note: You call a guess(int num) which returns 3 possible results (-1, 1, or 0).

```python
def guessNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
```
- Assigned to:

# #2: Sqrt(x)
Implement `sqrt(x)`.

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

```python
def mySqrt( x):
    """
    :type x: int
    :rtype: int
    """
```
- Assinged to:

# #3: Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

Notes:
- You are given a target value to search. If found in the array return its index, otherwise return -1.
- You may assume no duplicate exists in the array.

```python
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
```

Your algorithm's runtime complexity must be in the order of `O(log n)`.
- Assinged to:

# #4: First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

```python
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
```

- Assigned to:

# #5: Find Peak Element
A peak element is an element that is greater than its neighbors.

Given an input array nums, where `nums[i] ≠ nums[i+1]`, find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that `nums[-1] = nums[n] = -∞`.

```python
def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
```

# #6: Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

You may assume no duplicate exists in the array.

```python
def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
```
