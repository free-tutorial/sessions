# Pandas

## Multi-Index

```python
>>> df = pd.read_csv('datasets/drinks.csv')
>>> df.set_index(keys=['country', 'continent'], inplace=True)
        beer_servings	spirit_servings	wine_servings	total_litres_of_pure_alcohol
country	continent
Afghanistan	AS	0	0	0	0.0
Albania	EU	89	132	54	4.9
Algeria	AF	25	0	14	0.7
Andorra	EU	245	138	312	12.4
Angola	AF	217	57	45	5.9
...	...	...	...	...	...
Venezuela	SA	333	100	3	7.7
Vietnam	AS	111	2	1	2.0
Yemen	AS	6	0	0	0.1
Zambia	AF	32	19	4	2.5
Zimbabwe	AF	64	18	4	4.7
```

```python
>>> df.sort_index(ascending=False)

>>> df.sort_index(ascending=[False, True])

>>> df.index.names
FrozenList(['continent', 'country'])
>>> df.index[0], df.index[1]
(('AS', 'Afghanistan'), ('EU', 'Albania'))
>>> df.index.get_level_values(0)  # identical to `df.index.get_level_values('continent')`
Index(['AS', 'EU', 'AF', 'EU', 'AF',  nan, 'SA', 'EU', 'OC', 'EU',
       ...
       'AF',  nan, 'SA', 'AS', 'OC', 'SA', 'AS', 'AS', 'AF', 'AF'],
      dtype='object', name='continent', length=193)
>>> df.index.get_level_values(1)  # identical to `df.index.get_level_values('country')`
Index(['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
       'Antigua & Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
       ...
       'Tanzania', 'USA', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela',
       'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'],
      dtype='object', name='country', length=193)
```

Change index names:
```python
>>> df.index.set_names(['CONTINENT', 'COUNTRY'], inplace=True)
>>> df.index = df.index.set_names(['CONTINENT', 'COUNTRY'])
```

### Fetch data from multi-index dataframe
```python
>>> df.loc['AS']
        beer_servings	spirit_servings	wine_servings	total_litres_of_pure_alcohol
Country
Albania	89	132	54	4.9
Andorra	245	138	312	12.4
Armenia	21	179	11	3.8
Austria	279	75	191	9.7
Azerbaijan	21	46	5	1.3
        ...
Sweden	152	60	186	7.2
Switzerland	185	100	280	10.2
Macedonia	106	27	86	3.9
Ukraine	206	237	45	8.9
United Kingdom	219	126	195	10.4
>>> df.loc['AS', 'China']
beer_servings                    79.0
spirit_servings                 192.0
wine_servings                     8.0
total_litres_of_pure_alcohol      5.0
Name: (AS, China), dtype: float64
>>> df.loc[('AS', 'China')]
beer_servings                    79.0
spirit_servings                 192.0
wine_servings                     8.0
total_litres_of_pure_alcohol      5.0
Name: (AS, China), dtype: float64
>>> df.loc[('AS', 'China'), 'beer_servings']
79.0
```