# Python Datetimes


## `datetime`
Python datetime is a module to work with dates in python which has basically 4 main objects for date and time operations:
- `date`
- `time`
- `datetime`
- `timedelta`


Note:
- Objects of these types are immutable.
- Objects of these types are hashable, meaning that they can be used as dictionary keys.
- Objects of these types support efficient pickling via the pickle module.

### `datetime`
We can use `now()` method to create a datetime object containing the current local date and time.

```python
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 10, 24, 16, 31, 17, 389391)
```
```python
>>> datetime.today()
datetime.datetime(2019, 10, 24, 16, 30, 58, 469015)
>>> datetime(2019, 9, 4)
datetime.datetime(2019, 9, 4, 0, 0)
>>> datetime(2019, 9, 4, 20, 30)
datetime.datetime(2019, 9, 4, 20, 30)
```

### `date`
You can instantiate date objects from the date class. A date object represents a date (year, month and day).
```python
>>> from datetime import date
>>> date.today()  # YYYY-MM-DD format
datetime.date(2019, 10, 24)
>>> date(2019, 9, 4)
datetime.date(2019, 9, 4)
```

### `time`
```python
>>> time(12, 10, 30)
datetime.time(12, 10, 30)
```

### `timedelta`
```python
>>> from datetime import timedelta
>>> delta = timedelta(
...     days=50,
...     seconds=27,
...     microseconds=10,
...     milliseconds=29000,
...     minutes=5,
...     hours=8,
...     weeks=2
... )
>>> # Only days, seconds, and microseconds remain
>>> delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)
```

Arithmetic Examples:
1. 
```python
>>> # Components of another_year add up to exactly 365 days
>>> from datetime import timedelta
>>> year = timedelta(days=365)
>>> another_year = timedelta(weeks=40, days=84, hours=23,
...                          minutes=50, seconds=600)
>>> year == another_year
True
>>> year.total_seconds()
31536000.0
```

2. 
```python
>>> from datetime import timedelta
>>> year = timedelta(days=365)
>>> ten_years = 10 * year
>>> ten_years
datetime.timedelta(days=3650)
>>> ten_years.days // 365
10
>>> nine_years = ten_years - year
>>> nine_years
datetime.timedelta(days=3285)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)
```