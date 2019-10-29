# Pandas

## `groupby`

Pandas `dataframe.groupby()` function is used to split the data into groups based on some criteria. pandas objects can be split on any of their axes. The abstract definition of grouping is to provide a mapping of labels to group names.

```python
>>> df = pd.read_csv('datasets/sales.csv`)
>>> groupby = df.groupby(by='COUNTRY')
>>> groupby.first().iloc[:4, :4]  # print the first entry of every group
        QUANTITYORDERED	PRICEEACH	SALES	STATUS
COUNTRY
Australia	37	100.0	3965.66	Shipped
Austria	41	100.0	7737.93	Shipped
Belgium	30	100.0	3508.80	Shipped
Canada	47	100.0	9064.89	Shipped
>>> groupby.get_group('USA')
    QUANTITYORDERED	PRICEEACH	SALES	STATUS
0	30	95.70	2871.00	Shipped
3	45	83.26	3746.70	Shipped
4	49	100.00	5205.27	Shipped
5	36	96.66	3479.76	Shipped
8	22	98.57	2168.54	Shipped
...	...	...	...	...
2804	28	64.43	1804.04	Shipped
2807	36	63.34	2280.24	Shipped
2809	23	65.52	1506.96	Cancelled
2817	42	97.16	4080.72	Shipped
2822	47	65.52	3079.44	On Hold
1004 rows × 4 columns
>>> groupby.last()  # print the last entry of every group
```

```python
>>> groupby.size()
COUNTRY
Australia       185
Austria          55
Belgium          33
Canada           70
Denmark          63
Finland          92
France          314
Germany          62
Ireland          16
Italy           113
Japan            52
Norway           85
Philippines      26
Singapore        79
Spain           342
Sweden           57
Switzerland      31
UK              144
USA            1004
dtype: int64
```

### `sum`, `mean`, `max`, `min`
```python
>>> groupby.mean()
        QUANTITYORDERED	PRICEEACH	SALES	MONTH_ID	YEAR_ID
COUNTRY					
Australia	33.762162	83.508865	3408.773514	7.270270	2003.816216
Austria	35.890909	86.530182	3673.864182	6.963636	2003.836364
Belgium	32.545455	87.494242	3285.230909	5.696970	2004.181818
Canada	32.757143	85.100714	3201.122286	7.785714	2003.914286
Denmark	34.873016	87.363333	3899.002381	7.047619	2003.619048
Finland	34.695652	83.936413	3582.412065	5.271739	2004.065217
France	35.318471	82.550541	3537.950701	6.242038	2003.926752
Germany	34.645161	83.617742	3556.001452	8.467742	2003.661290
Ireland	30.625000	86.123750	3609.776875	5.062500	2004.000000
Italy	33.389381	82.561062	3315.701858	7.681416	2003.734513
Japan	35.423077	82.505000	3618.611731	4.884615	2004.192308
Norway	33.435294	86.096235	3617.220000	8.352941	2003.376471
Philippines	36.961538	82.499615	3615.989615	6.076923	2003.153846
Singapore	34.936709	83.315190	3651.752025	7.139241	2003.518987
Spain	36.342105	81.995731	3554.640117	6.722222	2003.921053
Sweden	35.192982	86.728246	3684.459825	8.824561	2003.824561
Switzerland	34.774194	87.519032	3797.211613	5.290323	2004.000000
UK	34.812500	82.518750	3325.558750	8.097222	2003.701389
USA	35.516932	83.824353	3613.528715	7.350598	2003.796813
>>> groupby.min(), groupby.max(), groupby.sum()
>>> groupby.get_group('USA').mean()['SALES']
>>> groupby.mean()['SALES']['USA']
```

### `agg`
Let's assume you want to apply some method based on the variable.

params:
- `func`: Function to use for aggregating the data. If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. For a DataFrame, can pass a dict, if the keys are DataFrame column names.
  Accepted combinations are:
  - string function name.
  - function.
  - list of functions.
  - dict of column names -> functions (or list of functions).

```python
>>> groupby.agg('sum')  # identical to groupby.agg(sum)
	QUANTITYORDERED	PRICEEACH	SALES	MONTH_ID	YEAR_ID
COUNTRY					
Australia	6246	15449.14	630623.10	1345	370706
Austria	1974	4759.16	202062.53	383	110211
Belgium	1074	2887.31	108412.62	188	66138
Canada	2293	5957.05	224078.56	545	140274
Denmark	2197	5503.89	245637.15	444	126228
Finland	3192	7722.15	329581.91	485	184374
France	11090	25920.87	1110916.52	1960	629233
Germany	2148	5184.30	220472.09	525	124227
Ireland	490	1377.98	57756.43	81	32064
Italy	3773	9329.40	374674.31	868	226422
Japan	1842	4290.26	188167.81	254	104218
Norway	2842	7318.18	307463.70	710	170287
Philippines	961	2144.99	94015.73	158	52082
Singapore	2760	6581.90	288488.41	564	158278
Spain	12429	28042.54	1215686.92	2299	685341
Sweden	2006	4943.51	210014.21	503	114218
Switzerland	1078	2713.09	117713.56	164	62124
UK	5013	11882.70	478880.46	1166	288533
USA	35659	84159.65	3627982.83	7380	2011812
>>> groupby.agg([sum, np.mean])['SALES']
        sum	mean
COUNTRY
Australia	630623.10	3408.773514
Austria	202062.53	3673.864182
Belgium	108412.62	3285.230909
Canada	224078.56	3201.122286
Denmark	245637.15	3899.002381
Finland	329581.91	3582.412065
France	1110916.52	3537.950701
Germany	220472.09	3556.001452
Ireland	57756.43	3609.776875
Italy	374674.31	3315.701858
Japan	188167.81	3618.611731
Norway	307463.70	3617.220000
Philippines	94015.73	3615.989615
Singapore	288488.41	3651.752025
Spain	1215686.92	3554.640117
Sweden	210014.21	3684.459825
Switzerland	117713.56	3797.211613
UK	478880.46	3325.558750
USA	3627982.83	3613.528715
>>> groupby.agg({'SALES': [min, 'mean'], 'PRICEEACH': 'mean'})
SALES	PRICEEACH
        min	mean	mean
COUNTRY
Australia	652.35	3408.773514	83.508865
Austria	640.05	3673.864182	86.530182
Belgium	881.40	3285.230909	87.494242
Canada	1119.93	3201.122286	85.100714
Denmark	1146.50	3899.002381	87.363333
Finland	891.03	3582.412065	83.936413
France	482.13	3537.950701	82.550541
Germany	948.99	3556.001452	83.617742
Ireland	1056.40	3609.776875	86.123750
Italy	577.60	3315.701858	82.561062
Japan	553.95	3618.611731	82.505000
Norway	1129.04	3617.220000	86.096235
Philippines	1173.15	3615.989615	82.499615
Singapore	785.64	3651.752025	83.315190
Spain	683.80	3554.640117	81.995731
Sweden	1467.48	3684.459825	86.728246
Switzerland	1205.04	3797.211613	87.519032
UK	710.20	3325.558750	82.518750
USA	541.14	3613.528715	83.824353
```