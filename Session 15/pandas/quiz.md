# Pandas Quiz #1

1. Which of the following way will **NOT** create Series object?

- [ ] `pd.Series([[1,3,5], 3, 5]])`
- [ ] `pd.Series([[1,3,5]])`
- [ ] `pd.Series([1,3,5], [3, 5])`
- [ ] `pd.Series([1,3,5])`

2. Which Datatype `.Series` method can not accept?

- [ ] `dict`
- [ ] `set`
- [ ] `list`
- [ ] `int`
- [ ] `str`

3. Which parameter of `.read_csv` emthod determine what kind of object will be returned?

- [ ] `squeeze`
- [ ] `header`
- [ ] `sep`
- [ ] `filename`

1. Below code will return Series object.

- [ ] False
- [ ] True

5. by default how many column `.head()` will return?

- [ ] 5
- [ ] 2
- [ ] All
- [ ] 1

6. s = pd.Series([1,2,3,4,5])
what is the output of `s[:9]`?

7. Series can hold any data type
- [ ] True
- [ ] False


## Solution
1. `pd.Series([1,3,5], [3, 5])`
2. `set` (`set` is unordered)
3. `squeeze` (`squeeze == True`: `Series` else `DataFrame`)
4. False
5. All
6. 
```
0    1
1    2
2    3
3    4
4    5
dtype: int64
```
7. True