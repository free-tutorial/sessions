# Pandas

## Options

### `max_rows` and `max_columns`
```python
>>> pd.options.display.max_columns
20
>>> pd.options.display.max_rows
60
>>> pd.options.display.max_columns = 100
>>> pd.options.display.max_rows = 200
>>> pd.get_option('max_rows')
200
>>> pd.reset_option('max_rows')
>>> pd.options.display.max_rows
60
>>> pd.set_option('max_rows', 200)
>>> pd.describe_option('max_rows')
display.max_rows : int
    If max_rows is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.

    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 60] [currently: 60]
```

### Precision

```python
>>> pd.describe_option('precision')
display.precision : int
    Floating point output precision (number of significant digits). This is
    only a suggestion
    [default: 6] [currently: 6]
>>> df = pd.DataFrame(np.random.randn(5,5))
>>> df
0	1	2	3	4
0	-1.477866	1.560853	-0.387924	0.498171	-0.985347
1	-0.371394	0.926771	0.111289	0.236505	-0.132310
2	-0.910334	1.495322	-1.624014	0.756997	0.537706
3	0.836827	1.574358	0.575808	-0.306461	0.563321
4	0.513420	-0.711686	0.225493	0.555288	-1.100464
>>> pd.options.display.precision
6
>>> pd.options.display.precision = 3
>>> df
0	1	2	3	4
0	0.499	-0.513	-0.026	0.653	-1.649
1	1.149	-2.572	-0.152	1.767	0.072
2	-0.880	-0.632	1.069	0.109	2.199
3	0.295	0.767	1.174	-1.299	-0.062
4	-1.106	-0.827	-1.465	-0.688	0.034
>>> pd.options.display.precision = 6
>>> df
0	1	2	3	4
0	-1.477866	1.560853	-0.387924	0.498171	-0.985347
1	-0.371394	0.926771	0.111289	0.236505	-0.132310
2	-0.910334	1.495322	-1.624014	0.756997	0.537706
3	0.836827	1.574358	0.575808	-0.306461	0.563321
4	0.513420	-0.711686	0.225493	0.555288	-1.100464
```
