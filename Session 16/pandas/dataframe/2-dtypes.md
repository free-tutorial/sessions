# Pandas
## Data Types

A possible confusing point about pandas data types is that there is some overlap between pandas, python and numpy. This table summarizes the key points:

|Pandas|Python|Numpy|Usage|
|--|--|--|--|
|`object`|`str`|string_, unicode_|text|
|`int64`|`int`|`int_`, `int8`, `int16`, `int32`, `int64`, `uint8`, `uint16`, `uint32`, `uint64`|integer numbers|
|`float64`|`float`|	`float_`, `float16`, `float32`, `float64`|floating point numbers|
|`bool`|`bool`|`bool_`|`True`/`False` values|
|`datetime64`|NA|`datetime64[ns]`|Date and Time values|
|`timedelta[ns]`|NA|NA|difference between two datetimes|
|`category`|NA|NA|finite list of text values|

Read [`./dtype.csv`](./dtype.csv) file:
```python
import numpy as np
import pandas as pd

df = pd.read_csv("sales_data_types.csv")
```

```python
>>> df['2016'] + df['2017']
0      $125,000.00$162500.00
1    $920,000.00$101,2000.00
2        $50,000.00$62500.00
3      $350,000.00$490000.00
4        $15,000.00$12750.00
dtype: object
```

This does not look right. We would like to get totals added together but pandas is just concatenating the two values together to create one long string. A clue to the problem is the line that says dtype: object. An object is a string in pandas so it performs a string operation instead of a mathematical one.

If we want to see what all the data types are in a dataframe, use `df.dtypes`:
```python
>>> df.dtypes
Customer Number    float64
Customer Name       object
2016                object
2017                object
Percent Growth      object
Jan Units           object
Month                int64
Day                  int64
Year                 int64
Active              object
dtype: object
```

Additionally, the `df.info()` function shows even more useful info:
```python
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 10 columns):
Customer Number    5 non-null float64
Customer Name      5 non-null object
2016               5 non-null object
2017               5 non-null object
Percent Growth     5 non-null object
Jan Units          5 non-null object
Month              5 non-null int64
Day                5 non-null int64
Year               5 non-null int64
Active             5 non-null object
dtypes: float64(1), int64(3), object(6)
memory usage: 480.0+ bytes
```

After looking at the automatically assigned data types, there are several concerns:
1. The Customer Number is a float64 but it should be an int64
2. The 2016 and 2017 columns are stored as objects, not numerical values such as a float64 or int64
3. Percent Growth and Jan Units are also stored as objects not numerical values
4. We have Month , Day and Year columns that should be converted to datetime64
5. The Active column should be a boolean

Until we clean up these data types, it is going to be very difficult to do much additional analysis on this data.

In order to convert data types in pandas, there are three basic options:
1. Use `astype()` to force an appropriate dtype
2. Create a custom function to convert the data
3. Use pandas functions such as `to_numeric()` or `to_datetime()`


### `astype()` function
The simplest way to convert a pandas column of data to a different type is to use astype() . For instance, to convert the Customer Number to an integer we can call it like this:
```python
>>> df['Customer Number'].astype('int')
0     10002
1    552278
2     23477
3     24900
4    651029
Name: Customer Number, dtype: int64
>>> df["Customer Number"] = df['Customer Number'].astype('int')
>>> df.dtypes
Customer Number     int64
Customer Name      object
2016               object
2017               object
Percent Growth     object
Jan Units          object
Month               int64
Day                 int64
Year                int64
Active             object
dtype: object
```

### Custom Conversion Functions
Since this data is a little more complex to convert, we can build a custom function that we apply to each value and convert to the appropriate data type.

For currency conversion (of this specific data set), here is a simple function we can use:
```python
def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)
```

Also of note, is that the function converts the number to a python float but pandas internally converts it to a float64. It is recommended to allow pandas to convert to specific size float or int as it determines appropriate. There is no need for you to try to downcast to a smaller or upcast to a larger byte size unless you really know why you need to do it.

Now, we can use the pandas apply function to apply this to all the values in the 2016 column.
```python
>>> df['2016'].apply(convert_currency)
0    125000.0
1    920000.0
2     50000.0
3    350000.0
4     15000.0
Name: 2016, dtype: float64
```

Using `lambda` functions:
```python
df['2016'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
```

```python
>>> df['2016'] = df['2016'].apply(convert_currency)
>>> df['2017'] = df['2017'].apply(convert_currency)
>>> df.dtypes
Customer Number      int64
Customer Name       object
2016               float64
2017               float64
Percent Growth      object
Jan Units           object
Month                int64
Day                  int64
Year                 int64
Active              object
dtype: object
```

The process for fixing the Percent Growth column:
```python
>>> df['Percent Growth'] = df['Percent Growth'].apply(lambda x: x.replace('%', '')).astype('float') / 100
```

Using lambda we can streamline the code into 1 line which is a perfectly valid approach. I have three main concerns with this approach:

1. If you are just learning python/pandas or if someone new to python is going to be maintaining code, I think the longer function is more readable. The primary reason is that it includes comments and can be broken down into a couple of steps. lambda functions are a little more difficult for the new user to grasp.
2. Secondly, if you are going to be using this function on multiple columns, I prefer not to duplicate the long lambda function.


The final custom function is using `np.where()` to convert the active column to a boolean. There are several possible ways to solve this specific problem. The `np.where()` approach is useful for many types of problems.

```python
>>> df["Active"] = np.where(df["Active"] == "Y", True, False)
>>> df.dtypes
Customer Number    float64
Customer Name       object
2016                object
2017                object
Percent Growth      object
Jan Units           object
Month                int64
Day                  int64
Year                 int64
Active                bool
dtype: object
```

### Pandas Helper Functions
Pandas has a middle ground between the blunt `astype()` function and the more complex custom functions. These helper functions can be very useful for certain data type conversions.

There have not been anything done with the date columns or the `Jan Units` column. Both of these can be converted simply using built in pandas functions such as `pd.to_numeric()` and `pd.to_datetime()`.

#### `pd.to_numeric()`
The reason the `Jan Units` conversion is problematic is the inclusion of a non-numeric value in the column. If we tried to use `astype()` we would get an error (as described earlier). The `pd.to_numeric()` function can handle these values more gracefully:

```python
>>> pd.to_numeric(df['Jan Units'], errors='coerce')
0    500.0
1    700.0
2    125.0
3     75.0
4      NaN
Name: Jan Units, dtype: float64
```

`errors` param: {`ignore`, `raise`, `coerce`}, default `raise`
- If `raise`, then invalid parsing will raise an exception
- If `coerce`, then invalid parsing will be set as `NaN`
- If `ignore`, then invalid parsing will return the input

There are a couple of items of note. First, the function easily processes the data and creates a float64 column. Additionally, it replaces the invalid `"Closed"` value with a NaN value because we passed errors=coerce . We can leave that value there or fill it in with a `0` using `fillna(0)`:

```python
>>> pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)
0    500.0
1    700.0
2    125.0
3     75.0
4      0.0
Name: Jan Units, dtype: float64
```

#### `pd.to_datetime()`
Converting the separate month, day and year columns into a datetime with the pandas `pd.to_datetime() `function is quite configurable but also pretty smart by default.

```python
>>> df['Start_Date'] = pd.to_datetime(df[['Month', 'Day', 'Year']])
>>> df['Start_Date']
0   2015-01-10
1   2014-06-15
2   2016-03-29
3   2015-10-27
4   2014-02-02
dtype: datetime64[ns]
```

`pd.to_datetime()` accepts many data types as `arg`:
- integer
- float
- string
- datetime
- list
- tuple
- 1-d array
- Series
- DataFrame

`integer` and `float`:
```python
>>> pd.to_datetime(100, unit='d')
Timestamp('1970-01-11 00:00:00')
>>> pd.to_datetime(10, unit='s')
Timestamp('1970-01-01 00:00:10')
>>> pd.to_datetime(20.125, unit='d')  # 20 days + 1/8 day = 20 days + 3 hours
Timestamp('1970-01-21 03:00:00')
```
`unit` : string, default `ns`
unit of the arg (`D`,`s`,`ms`,`us`,`ns`) denote the unit, which is an integer or float number.

`string`:
```python
>>> pd.to_datetime('20-5-18')
Timestamp('2018-05-20 00:00:00')
>>> pd.to_datetime('5-20-18')
Timestamp('2018-05-20 00:00:00')
>>> pd.to_datetime('5/20/2018')
Timestamp('2018-05-20 00:00:00')
```

`datetime`:
```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> pd.to_datetime(now)
Timestamp('2019-10-20 23:10:39.283977')
```

`list`, `tuple`, `1d-array`, or `Series`:
```python
>>> pd.to_datetime([1, 2, 3, 4, 5], unit='d')
DatetimeIndex(['1970-01-02', '1970-01-03', '1970-01-04', '1970-01-05', '1970-01-06'], dtype='datetime64[ns]', freq=None)
>>> pd.to_datetime(pd.Series([1,2,3,4,5]), unit='d')
0   1970-01-02
1   1970-01-03
2   1970-01-04
3   1970-01-05
4   1970-01-06
dtype: datetime64[ns]
```

`DataFrame`:
```python
>>> pd.to_datetime(df[['Month', 'Day', 'Year']])
0   2015-01-10
1   2014-06-15
2   2016-03-29
3   2015-10-27
4   2014-02-02
dtype: datetime64[ns]
```

Now the data is properly converted to all the types we need:

```python
Customer Number             int64
Customer Name              object
2016                      float64
2017                      float64
Percent Growth            float64
Jan Units                 float64
Month                       int64
Day                         int64
Year                        int64
Active                       bool
Start_Date         datetime64[ns]
```

### References
- https://pbpython.com/pandas_dtypes.html