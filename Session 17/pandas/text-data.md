# Pandas

## Text Data
Series and Index are equipped with a set of string processing methods that make it easy to operate on each element of the array. These are accessed via the `str` attribute.

```python
>>> df = pd.read_csv('datasets/SMSSpamCollection', header=None, names=['label', 'message'])
>>> df.head()
	label	message
0	ham	Go until jurong point, crazy.. Available only ...
1	ham	Ok lar... Joking wif u oni...
2	spam	Free entry in 2 a wkly comp to win FA Cup fina...
3	ham	U dun say so early hor... U c already then say...
4	ham	Nah I don't think he goes to usf, he lives aro...
```

### `upper`, `lower`, `title`, `len`
```python
>>> df.label.str.upper()
0        HAM
1        HAM
2       SPAM
3        HAM
4        HAM
        ... 
5567    SPAM
5568     HAM
5569     HAM
5570     HAM
5571     HAM
Name: label, Length: 5572, dtype: object
>>> df.label.str.upper().str.lower()
0        ham
1        ham
2       spam
3        ham
4        ham
        ... 
5567    spam
5568     ham
5569     ham
5570     ham
5571     ham
Name: label, Length: 5572, dtype: object
>>> df.label.str.len()
0       3
1       3
2       4
3       3
4       3
       ..
5567    4
5568    3
5569    3
5570    3
5571    3
Name: label, Length: 5572, dtype: int64
```

### `replace`, `strip`
```python
>>> df['message'].iloc[3]
'U dun say so early hor... U c already then say...'
>>> df['message'].iloc[3].replace('...', ' ').strip().replace('so', '').replace('the', '')
'U dun say  early hor  U c already n say'
```

### `startswith`, `endswith`
```python
>>> df[df.message.str.startswith('hi')]
        label	message
288	    ham	hi baby im cruisin with my girl friend what r ...
2164	ham	hi my darlin im on my way to London and we hav...
4569	ham	hiya hows it going in sunny africa? hope u r a...
4952	ham	hi baby im sat on the bloody bus at the mo and...
>>> df[df.message.str.endswith('bye')]
    label	message
185	ham	Going on nothing great.bye
464	ham	Sorry, I'll call later ok bye
```

### Filtering with string
```python
>>> df[df.label == 'spam']
label	message
2	spam	Free entry in 2 a wkly comp to win FA Cup fina...
5	spam	FreeMsg Hey there darling it's been 3 week's n...
8	spam	WINNER!! As a valued network customer you have...
9	spam	Had your mobile 11 months or more? U R entitle...
11	spam	SIX chances to win CASH! From 100 to 20,000 po...
...	...	...
5537	spam	Want explicit SEX in 30 secs? Ring 02073162414...
5540	spam	ASKED 3MOBILE IF 0870 CHATLINES INCLU IN FREE ...
5547	spam	Had your contract mobile 11 Mnths? Latest Moto...
5566	spam	REMINDER FROM O2: To get 2.50 pounds free call...
5567	spam	This is the 2nd time we have tried 2 contact u...
747 rows × 2 columns
>>> df[df.message.str.contains('Sorry')]
label	message
57	ham	Sorry, I'll call later in meeting.
63	ham	Sorry my roommates took forever, it ok if I co...
80	ham	Sorry, I'll call later
91	ham	Sorry to be a pain. Is it ok if we meet anothe...
223	ham	Sorry, I'll call later
...	...	...
5135	ham	Sorry * was at the grocers.
5191	ham	Sorry, I'll call later
5423	ham	Sorry, I'll call later
5458	ham	Sorry, I'll call later
5558	ham	Sorry, I'll call later
111 rows × 2 columns
>>> df[df.message.str.contains('Sorry')].label.value_counts()  # `sorry` could be a signal for spam detection!
ham     108
spam      3
Name: label, dtype: int64
>>> df[df.message.str.lower().str.contains('sorry')].label.value_counts()  # lower case helps for a better result
ham     148
spam      3
Name: label, dtype: int64
```

### `split`
```python
>>> df.message.str.split()
0       [Go, until, jurong, point,, crazy.., Available...
1                    [Ok, lar..., Joking, wif, u, oni...]
2       [Free, entry, in, 2, a, wkly, comp, to, win, F...
3       [U, dun, say, so, early, hor..., U, c, already...
4       [Nah, I, don't, think, he, goes, to, usf,, he,...
                              ...                        
5567    [This, is, the, 2nd, time, we, have, tried, 2,...
5568        [Will, ü, b, going, to, esplanade, fr, home?]
5569    [Pity,, *, was, in, mood, for, that., So...any...
5570    [The, guy, did, some, bitching, but, I, acted,...
5571                    [Rofl., Its, true, to, its, name]
Name: message, Length: 5572, dtype: object
>>> df.message.str.split().iloc[0]
['Go',
 'until',
 'jurong',
 'point,',
 'crazy..',
 'Available',
 'only',
 'in',
 'bugis',
 'n',
 'great',
 'world',
 'la',
 'e',
 'buffet...',
 'Cine',
 'there',
 'got',
 'amore',
 'wat...']
```

### Processing Column Names
`df.columns` is a Series data type. Therefore, all the aforementioned operations can be applied on `df.columns`.

```python
>>> df.columns.str.title()
Index(['Label', 'Message'], dtype='object')
>>> df.columns = df.columns.str.title()
```
